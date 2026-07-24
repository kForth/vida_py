"""Live integration tests for implementation coverage against VIDA databases."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

import ast
import importlib
import inspect as pyinspect
import os
import sys
from collections.abc import Generator
from contextlib import contextmanager
from datetime import datetime
from typing import Any

import pytest
from sqlalchemy import text
from sqlalchemy.orm import Session

pytestmark = pytest.mark.integration

MODULES = (
    "access",
    "basedata",
    "carcom",
    "diag",
    "epc",
    "images",
    "service",
    "session",
    "timing",
)
SUBMODULES: tuple[str, ...] = ("models", "views", "funcs", "scripts")


def _discover_module_components(module_name: str) -> dict[str, str]:
    components: dict[str, str] = {}
    for suffix in SUBMODULES:
        candidate = f"vida_py.{module_name}.{suffix}"
        if importlib.util.find_spec(candidate) is not None:
            components[suffix] = candidate
    return components


MODULE_ENV_VARS = {f"vida_py.{e}": f"VIDA_{e.upper()}_DB_URI" for e in MODULES}

MODULE_COMPONENTS = {f"vida_py.{module}": _discover_module_components(module) for module in MODULES}

# These model-only key columns are intentionally not present in DB objects.
KNOWN_SYNTHETIC_COLUMNS: dict[tuple[str, str], set[str]] = {
    ("vida_py.diag.models", "EcuDescription"): {"id"},
    ("vida_py.diag.models", "IEGenericComponent"): {"id"},
    ("vida_py.diag.models", "SmartToolScript"): {"id"},
    ("vida_py.session.models", "ActionItem"): {"id"},
}

# System tables to ignore missing implementations
SYSTEM_TABLES: set[str] = {"dtproperties", "sysdiagrams"}


def _require_db_uri(module_name: str, env_var: str) -> str:
    value = os.getenv(env_var)
    if not value:
        pytest.skip(f"{env_var} is not configured for live integration tests ({module_name}).")
    return value


def _import_fresh(module_name: str) -> Any:
    sys.modules.pop(module_name, None)
    return importlib.import_module(module_name)


@contextmanager
def _session_for_module(module_name: str, env_var: str) -> Generator[Session]:
    _require_db_uri(module_name, env_var)
    module = _import_fresh(module_name)
    session = module.create_session()
    try:
        yield session
    finally:
        session.close()


def _normalize(names: set[str]) -> set[str]:
    return {name.strip().lower() for name in names}


def _query_names(session: Session, query: str) -> set[str]:
    rows = session.execute(text(query)).all()
    return {str(row[0]) for row in rows if row[0] is not None}


def _iter_model_classes(module: Any) -> list[type[Any]]:
    classes: list[type[Any]] = []
    for _, obj in pyinspect.getmembers(module, pyinspect.isclass):
        if obj.__module__ != module.__name__:
            continue
        if hasattr(obj, "__tablename__") and hasattr(obj, "__table__"):
            classes.append(obj)
    return classes


def _iter_view_classes(module: Any) -> list[type[Any]]:
    classes: list[type[Any]] = []
    for _, obj in pyinspect.getmembers(module, pyinspect.isclass):
        if obj.__module__ != module.__name__:
            continue
        if hasattr(obj, "__viewname__"):
            classes.append(obj)
    return classes


def _extract_wrapped_routines(module: Any, helper_name: str) -> set[str]:
    source = pyinspect.getsource(module)
    tree = ast.parse(source)
    names: set[str] = set()
    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue
        if not isinstance(node.func, ast.Name):
            continue
        if node.func.id != helper_name:
            continue
        if len(node.args) < 2:
            continue
        second_arg = node.args[1]
        if isinstance(second_arg, ast.Constant) and isinstance(second_arg.value, str):
            names.add(second_arg.value)
    return names


def _extract_script_wrapper_bindings(
    module: Any,
) -> dict[str, tuple[str, list[str], list[str]]]:
    source = pyinspect.getsource(module)
    tree = ast.parse(source)
    bindings: dict[str, tuple[str, list[str], list[str]]] = {}

    for node in tree.body:
        if not isinstance(node, ast.FunctionDef):
            continue

        run_script_call: ast.Call | None = None
        for child in ast.walk(node):
            if not isinstance(child, ast.Call):
                continue
            if not isinstance(child.func, ast.Name):
                continue
            if child.func.id != "run_script":
                continue
            run_script_call = child
            break

        if run_script_call is None or len(run_script_call.args) < 2:
            continue

        script_arg = run_script_call.args[1]
        if not isinstance(script_arg, ast.Constant) or not isinstance(script_arg.value, str):
            continue

        sql_param_names: list[str] = []
        python_param_names: list[str] = []
        for keyword in run_script_call.keywords:
            if keyword.arg is None:
                continue
            sql_param_names.append(keyword.arg)
            if isinstance(keyword.value, ast.Name):
                python_param_names.append(keyword.value.id)
            else:
                python_param_names.append("")

        bindings[node.name] = (script_arg.value, sql_param_names, python_param_names)

    return bindings


def _extract_function_wrapper_bindings(
    module: Any,
) -> dict[str, tuple[str, int]]:
    source = pyinspect.getsource(module)
    tree = ast.parse(source)
    bindings: dict[str, tuple[str, int]] = {}
    helper_names = {"run_func", "run_func_scalar"}

    for node in tree.body:
        if not isinstance(node, ast.FunctionDef):
            continue

        run_func_call: ast.Call | None = None
        for child in ast.walk(node):
            if not isinstance(child, ast.Call):
                continue
            if not isinstance(child.func, ast.Name):
                continue
            if child.func.id not in helper_names:
                continue
            run_func_call = child
            break

        if run_func_call is None or len(run_func_call.args) < 2:
            continue

        func_arg = run_func_call.args[1]
        if not isinstance(func_arg, ast.Constant) or not isinstance(func_arg.value, str):
            continue

        num_params_passed = len(run_func_call.args) - 2
        # sql_param_names: list[str] = []
        # python_param_names: list[str] = []
        # for keyword in run_func_call.keywords:
        #     if keyword.arg is None:
        #         continue
        #     sql_param_names.append(keyword.arg)
        #     if isinstance(keyword.value, ast.Name):
        #         python_param_names.append(keyword.value.id)
        #     else:
        #         python_param_names.append("")

        bindings[node.name] = (func_arg.value, num_params_passed)

    return bindings


def _implemented_model_tables(model_module_name: str) -> set[str]:
    module = importlib.import_module(model_module_name)
    return {str(cls.__tablename__) for cls in _iter_model_classes(module)}


def _implemented_view_names(view_module_name: str) -> set[str]:
    module = importlib.import_module(view_module_name)
    return {str(cls.__viewname__) for cls in _iter_view_classes(module)}


def _implemented_procedures(component_map: dict[str, str]) -> set[str]:
    scripts_module_name = component_map.get("scripts")
    if not scripts_module_name:
        return set()
    module = importlib.import_module(scripts_module_name)
    scripts = getattr(module, "STORED_PROCEDURES", None)
    if not isinstance(scripts, dict):
        raise AssertionError(f"{scripts_module_name} must define a STORED_PROCEDURES dictionary")
    return {str(name) for name in scripts}


def _implemented_funcs(component_map: dict[str, str]) -> set[str]:
    funcs_module_name = component_map.get("funcs")
    if not funcs_module_name:
        return set()
    module = importlib.import_module(funcs_module_name)
    funcs = getattr(module, "FUNCTIONS", None)
    if not isinstance(funcs, dict):
        raise AssertionError(f"{funcs_module_name} must define a FUNCTIONS dictionary")
    return {str(name) for name in funcs}


def _annotation_matches_sql_type(annotation: Any, sql_type: str) -> bool:
    if annotation is Any:
        return True

    normalized_sql_type = sql_type.strip().lower()

    if normalized_sql_type in {"int", "bigint", "smallint", "tinyint"}:
        return annotation is int

    if normalized_sql_type in {"float", "real", "decimal", "numeric", "money", "smallmoney"}:
        return annotation in {int, float}

    if normalized_sql_type in {"bit"}:
        return annotation is bool

    if normalized_sql_type in {"char", "nchar", "varchar", "nvarchar", "text", "ntext"}:
        return annotation is str

    if normalized_sql_type in {"binary", "varbinary", "image"}:
        return annotation is bytes

    if normalized_sql_type in {
        "date",
        "time",
        "datetime",
        "datetime2",
        "smalldatetime",
        "datetimeoffset",
    }:
        return annotation is datetime

    return True


def _assert_wrapper_type_annotations_match_db_types(
    wrapper: Any,
    db_param_types: list[str],
    module_name: str,
    routine_name: str,
) -> None:
    signature = pyinspect.signature(wrapper)
    signature_parameters = [
        parameter for parameter in signature.parameters.values() if parameter.name != "session"
    ]

    assert len(signature_parameters) == len(db_param_types), (
        f"Parameter count/type shape mismatch in {module_name} {routine_name}: "
        f"signature parameter count={len(signature_parameters)}, "
        f"db parameter type count={len(db_param_types)}"
    )

    for parameter, db_type in zip(signature_parameters, db_param_types, strict=False):
        assert _annotation_matches_sql_type(parameter.annotation, db_type), (
            f"Type mismatch in {module_name} {routine_name} for parameter "
            f"'{parameter.name}': annotation={parameter.annotation!r}, db_type={db_type!r}"
        )


def _script_wrapper_signature_cases() -> list[Any]:
    cases: list[Any] = []
    for db_module_name, component_map in MODULE_COMPONENTS.items():
        scripts_module_name = component_map.get("scripts")
        if not scripts_module_name:
            continue

        scripts_module = importlib.import_module(scripts_module_name)
        scripts = getattr(scripts_module, "STORED_PROCEDURES", None)
        if not isinstance(scripts, dict):
            raise AssertionError(
                f"{scripts_module_name} must define a STORED_PROCEDURES dictionary"
            )

        for procedure_name in scripts:
            cases.append(
                pytest.param(
                    db_module_name,
                    scripts_module_name,
                    str(procedure_name),
                    id=f"{db_module_name}:{procedure_name}",
                )
            )

    return cases


def _function_wrapper_signature_cases() -> list[Any]:
    cases: list[Any] = []
    for db_module_name, component_map in MODULE_COMPONENTS.items():
        funcs_module_name = component_map.get("funcs")
        if not funcs_module_name:
            continue

        funcs_module = importlib.import_module(funcs_module_name)
        funcs = getattr(funcs_module, "FUNCTIONS", None)
        if not isinstance(funcs, dict):
            raise AssertionError(f"{funcs_module_name} must define a FUNCTIONS dictionary")

        for function_name in funcs:
            cases.append(
                pytest.param(
                    db_module_name,
                    funcs_module_name,
                    str(function_name),
                    id=f"{db_module_name}:{function_name}",
                )
            )

    return cases


@pytest.mark.parametrize(("_db_module_name", "component_map"), MODULE_COMPONENTS.items())
def test_stored_procedure_registry_matches_wrapper_bindings(
    _db_module_name: str, component_map: dict[str, str]
) -> None:
    scripts_module_name = component_map.get("scripts")
    if not scripts_module_name:
        return

    module = importlib.import_module(scripts_module_name)
    scripts = getattr(module, "STORED_PROCEDURES", None)
    assert isinstance(
        scripts, dict
    ), f"{scripts_module_name} must define a STORED_PROCEDURES dictionary"

    expected_scripts = _extract_wrapped_routines(module, "run_script")
    assert _normalize({str(name) for name in scripts}) == _normalize(expected_scripts)


def _db_object_names(session: Session, routine_types: tuple[str, ...]) -> set[str]:
    type_filters = ", ".join(f"'{routine_type}'" for routine_type in routine_types)
    query = (
        "SELECT name "
        "FROM sys.objects "
        "WHERE schema_id = SCHEMA_ID('dbo') "
        f"AND type IN ({type_filters}) "
        "AND is_ms_shipped = 0 "
        "AND create_date < '2016-01-01' "  # This date cut-off is important
        "ORDER BY name"
    )
    return _query_names(session, query)


def _db_procedure_parameter_names(
    session: Session, procedure_name: str
) -> tuple[list[str], list[str]]:
    normalized_procedure_name = procedure_name.strip()
    db_name = str(session.execute(text("SELECT DB_NAME()")).scalar_one())

    all_procedures = _db_object_names(session, ("P",))

    exists_row = session.execute(
        text(
            "SELECT 1 "
            "FROM sys.procedures "
            "WHERE schema_id = SCHEMA_ID('dbo') "
            "AND name = :procedure_name"
        ),
        {"procedure_name": normalized_procedure_name},
    ).first()
    assert exists_row is not None, (
        f"Missing dbo procedure: {procedure_name!r}. "
        f"Connected DB={db_name!r}. "
        f"All procedures in this DB={sorted(set(all_procedures))}"
    )

    rows = session.execute(
        text(
            "SELECT p.name, t.name "
            "FROM sys.procedures sp "
            "JOIN sys.parameters p ON sp.object_id = p.object_id "
            "JOIN sys.types t ON p.system_type_id = t.system_type_id "
            "WHERE sp.schema_id = SCHEMA_ID('dbo') "
            "AND t.name NOT LIKE 'sysname' "
            "AND sp.name = :procedure_name "
            "ORDER BY p.parameter_id"
        ),
        {"procedure_name": normalized_procedure_name},
    ).all()
    return [str(row[0]).lstrip("@") for row in rows], [row[1] for row in rows]


def _db_function_parameter_names(
    session: Session, function_name: str
) -> tuple[list[str], list[str]]:
    normalized_function_name = function_name.strip()
    db_name = str(session.execute(text("SELECT DB_NAME()")).scalar_one())

    all_functions = _db_object_names(session, ("FN", "IF", "TF"))

    exists_row = session.execute(
        text(
            "SELECT 1 "
            "FROM sys.objects "
            "WHERE schema_id = SCHEMA_ID('dbo') "
            "AND type IN ('FN', 'IF', 'TF') "
            "AND name = :function_name"
        ),
        {"function_name": normalized_function_name},
    ).first()
    assert exists_row is not None, (
        f"Missing dbo function: {function_name!r}. "
        f"Connected DB={db_name!r}. "
        f"All functions in this DB={sorted(set(all_functions))}"
    )

    rows = session.execute(
        text(
            "SELECT p.name, t.name "
            "FROM sys.objects o "
            "JOIN sys.parameters p ON o.object_id = p.object_id "
            "JOIN sys.types t ON p.system_type_id = t.system_type_id "
            "WHERE o.schema_id = SCHEMA_ID('dbo') "
            "AND o.type IN ('FN', 'IF', 'TF') "
            "AND p.parameter_id > 0 "
            "AND t.name NOT LIKE 'sysname' "
            "AND o.name = :function_name "
            "ORDER BY p.parameter_id"
        ),
        {"function_name": normalized_function_name},
    ).all()
    return [str(row[0]).lstrip("@") for row in rows], [row[1] for row in rows]


@pytest.mark.parametrize(
    ("db_module_name", "scripts_module_name", "procedure_name"),
    _script_wrapper_signature_cases(),
)
def test_stored_procedure_wrapper_signatures_and_db_parameter_bindings_match_live_procedures(
    db_module_name: str, scripts_module_name: str, procedure_name: str
) -> None:
    env_var = MODULE_ENV_VARS[db_module_name]
    scripts_module = importlib.import_module(scripts_module_name)
    scripts = getattr(scripts_module, "STORED_PROCEDURES", None)
    assert isinstance(
        scripts, dict
    ), f"{scripts_module_name} must define a STORED_PROCEDURES dictionary"

    wrapper_bindings = _extract_script_wrapper_bindings(scripts_module)

    assert (
        procedure_name in scripts
    ), f"{scripts_module_name}.STORED_PROCEDURES is missing expected key {procedure_name!r}"
    wrapper = scripts[procedure_name]

    assert callable(wrapper), (
        f"{scripts_module_name}.STORED_PROCEDURES['{procedure_name}'] " "must map to a callable"
    )

    wrapper_name = str(getattr(wrapper, "__name__", ""))
    assert (
        wrapper_name in wrapper_bindings
    ), f"Could not find run_script call for wrapper {scripts_module_name}.{wrapper_name}"

    bound_procedure_name, wrapper_param_names, python_param_names = wrapper_bindings[wrapper_name]
    assert bound_procedure_name.strip().lower() == procedure_name.strip().lower(), (
        f"{scripts_module_name}.{wrapper_name} calls {bound_procedure_name!r} "
        f"but registry key is {procedure_name!r}"
    )

    signature = pyinspect.signature(wrapper)
    signature_param_names = [
        parameter_name for parameter_name in signature.parameters if parameter_name != "session"
    ]

    assert "" not in python_param_names, (
        f"{scripts_module_name}.{wrapper_name} contains non-name run_script argument "
        "expressions; cannot validate parameter-to-signature mapping"
    )
    assert signature_param_names == python_param_names, (
        f"Signature mismatch in {scripts_module_name}.{wrapper_name}: "
        f"signature params={signature_param_names}, "
        f"run_script bindings={python_param_names}"
    )

    with _session_for_module(db_module_name, env_var) as session:
        db_param_names, db_param_types = _db_procedure_parameter_names(session, procedure_name)
    db_params = list(zip(db_param_names, db_param_types, strict=False))

    assert len(wrapper_param_names) == len(db_param_names), (
        f"run_script parameter count mismatch for {db_module_name} {procedure_name}: "
        f"wrapper binding count={len(wrapper_param_names)}, db count={len(db_param_names)}, "
        f"{db_params=}"
    )

    assert [name.lower() for name in wrapper_param_names] == [
        name.lower() for name in db_param_names
    ], f"Procedure parameter mismatch for {db_module_name} {procedure_name}: {db_params=}"

    _assert_wrapper_type_annotations_match_db_types(
        wrapper,
        db_param_types,
        scripts_module_name,
        procedure_name,
    )


@pytest.mark.parametrize(
    ("db_module_name", "funcs_module_name", "function_name"),
    _function_wrapper_signature_cases(),
)
def test_function_wrapper_signatures_and_db_parameter_bindings_match_live_functions(
    db_module_name: str, funcs_module_name: str, function_name: str
) -> None:
    env_var = MODULE_ENV_VARS[db_module_name]
    funcs_module = importlib.import_module(funcs_module_name)
    funcs = getattr(funcs_module, "FUNCTIONS", None)
    assert isinstance(funcs, dict), f"{funcs_module_name} must define a FUNCTIONS dictionary"

    wrapper_bindings = _extract_function_wrapper_bindings(funcs_module)

    assert (
        function_name in funcs
    ), f"{funcs_module_name}.FUNCTIONS is missing expected key {function_name!r}"
    wrapper = funcs[function_name]

    assert callable(wrapper), (
        f"{funcs_module_name}.FUNCTIONS['{function_name}'] " "must map to a callable"
    )

    wrapper_name = str(getattr(wrapper, "__name__", ""))
    assert wrapper_name in wrapper_bindings, (
        "Could not find run_func/run_func_scalar call for wrapper "
        f"{funcs_module_name} {wrapper_name}"
    )

    bound_function_name, num_params_passed = wrapper_bindings[wrapper_name]
    assert bound_function_name.strip().lower() == function_name.strip().lower(), (
        f"{funcs_module_name} {wrapper_name} calls {bound_function_name!r} "
        f"but registry key is {function_name!r}"
    )

    signature = pyinspect.signature(wrapper)
    num_wrapper_params = len([e for e in signature.parameters if e != "session"])
    assert num_wrapper_params >= num_params_passed, (
        f"Not all wrapper parameters passed in {funcs_module_name} {wrapper_name}: "
        f"wrapper params={num_wrapper_params}, "
        f"parameters passed={num_params_passed}"
    )
    assert num_wrapper_params <= num_params_passed, (
        f"Too many wrapper parameters passed in {funcs_module_name} {wrapper_name}: "
        f"wrapper params={num_wrapper_params}, "
        f"parameters passed={num_params_passed}"
    )

    with _session_for_module(db_module_name, env_var) as session:
        db_param_names, db_param_types = _db_function_parameter_names(session, function_name)
    db_params = list(zip(db_param_names, db_param_types, strict=False))

    assert num_wrapper_params == len(db_param_names), (
        f"Wrapper signature parameter count mismatch for {db_module_name} {function_name}: "
        f"wrapper signature count={num_wrapper_params}, db count={len(db_param_names)}, "
        f"{db_params=}"
    )

    _assert_wrapper_type_annotations_match_db_types(
        wrapper,
        db_param_types,
        funcs_module_name,
        function_name,
    )


@pytest.mark.parametrize(("db_module_name", "component_map"), MODULE_COMPONENTS.items())
def test_model_definitions_include_only_columns_present_in_live_tables(
    db_module_name: str, component_map: dict[str, str]
) -> None:
    model_module_name = component_map.get("models")
    if not model_module_name:
        return

    env_var = MODULE_ENV_VARS[db_module_name]
    model_module = importlib.import_module(model_module_name)
    model_classes = _iter_model_classes(model_module)

    with _session_for_module(db_module_name, env_var) as session:
        for model_class in model_classes:
            table_name = str(model_class.__tablename__)
            class_name = str(model_class.__name__)

            table_columns = _query_names(
                session,
                "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS "
                f"WHERE TABLE_SCHEMA = 'dbo' AND TABLE_NAME = '{table_name}'",
            )
            assert (
                table_columns
            ), f"Missing table dbo.{table_name} for model {model_module_name}.{class_name}"

            expected_columns = {str(column.name) for column in model_class.__table__.columns}
            expected_columns = expected_columns - KNOWN_SYNTHETIC_COLUMNS.get(
                (model_module_name, class_name),
                set(),
            )
            missing = _normalize(expected_columns) - _normalize(table_columns)
            assert not missing, (
                f"Missing columns in dbo.{table_name} for {model_module_name}.{class_name}: "
                f"{sorted(missing)}"
            )


@pytest.mark.parametrize(("db_module_name", "component_map"), MODULE_COMPONENTS.items())
def test_all_implemented_views_exist_in_live_database(
    db_module_name: str, component_map: dict[str, str]
) -> None:
    view_module_name = component_map.get("views")
    if not view_module_name:
        return

    env_var = MODULE_ENV_VARS[db_module_name]
    implemented_views = _implemented_view_names(view_module_name)

    with _session_for_module(db_module_name, env_var) as session:
        db_views = _query_names(
            session,
            "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.VIEWS WHERE TABLE_SCHEMA = 'dbo'",
        )

    missing = _normalize(implemented_views) - _normalize(db_views)
    assert not missing, f"Implemented views missing in DB for {db_module_name}: {sorted(missing)}"


@pytest.mark.parametrize(("db_module_name", "component_map"), MODULE_COMPONENTS.items())
def test_all_live_sql_functions_are_implemented_in_vida_py(
    db_module_name: str, component_map: dict[str, str]
) -> None:
    env_var = MODULE_ENV_VARS[db_module_name]
    implemented_functions = _implemented_funcs(component_map)
    normalized_impl_functions = _normalize(implemented_functions)

    with _session_for_module(db_module_name, env_var) as session:
        db_functions = _db_object_names(session, ("FN", "IF", "TF"))

    missing_functions = {
        e for e in db_functions if e.strip().lower() not in normalized_impl_functions
    }

    assert (
        not missing_functions
    ), f"Unimplemented functions for {db_module_name}: {sorted(missing_functions)}. "


@pytest.mark.parametrize(("db_module_name", "component_map"), MODULE_COMPONENTS.items())
def test_all_live_stored_procedures_are_implemented_in_vida_py(
    db_module_name: str, component_map: dict[str, str]
) -> None:
    env_var = MODULE_ENV_VARS[db_module_name]
    implemented_procedures = _implemented_procedures(component_map)
    normalized_impl_procedures = _normalize(implemented_procedures)

    with _session_for_module(db_module_name, env_var) as session:
        db_procedures = _db_object_names(session, ("P",))

    missing_procedures = {
        e for e in db_procedures if e.strip().lower() not in normalized_impl_procedures
    }

    assert not missing_procedures, (
        f"Unimplemented procedures for {db_module_name}: {sorted(missing_procedures)}."
        f"Found: {implemented_procedures}"
    )


def test_all_live_base_tables_are_implemented_in_vida_py() -> None:
    for db_module_name, component_map in MODULE_COMPONENTS.items():
        env_var = MODULE_ENV_VARS[db_module_name]

        implemented_tables = (
            _implemented_model_tables(component_map["models"])
            if "models" in component_map
            else set()
        )

        with _session_for_module(db_module_name, env_var) as session:
            db_tables = _query_names(
                session,
                "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'dbo' "
                "AND TABLE_TYPE = 'BASE TABLE'",
            )
        missing_tables = (
            _normalize(db_tables) - _normalize(implemented_tables) - _normalize(SYSTEM_TABLES)
        )

        assert (
            not missing_tables
        ), f"Unimplemented tables for {db_module_name}: {sorted(missing_tables)}"
