"""SQL function wrapper helpers for the basedata VIDA database."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from sqlalchemy import Row
from sqlalchemy.orm import Session

from vida_py.util import require_scalar, run_func, run_func_scalar


def get_profile_full_title(session: Session, fk_profile: str) -> str:
    value = require_scalar(
        run_func_scalar(session, "getProfileFullTitle", fk_profile),
        "getProfileFullTitle",
    )
    return str(value)


def get_profile_model_year_desc(session: Session, fk_profile: str) -> str:
    value = require_scalar(
        run_func_scalar(session, "getProfileModelYearDesc", fk_profile),
        "getProfileModelYearDesc",
    )
    return str(value)


def get_profile_nav_title(session: Session, fk_profile: str) -> str:
    value = require_scalar(
        run_func_scalar(session, "getProfileNavTitle", fk_profile),
        "getProfileNavTitle",
    )
    return str(value)


def get_profiles_full_title(session: Session, selected_profiles: str) -> str:
    value = require_scalar(
        run_func_scalar(session, "getProfilesFullTitle", selected_profiles),
        "getProfilesFullTitle",
    )
    return str(value)


def get_profile_vehicle_model_desc(session: Session, fk_profile: str) -> str:
    value = require_scalar(
        run_func_scalar(session, "getProfileVehicleModelDesc", fk_profile),
        "getProfileVehicleModelDesc",
    )
    return str(value)


def get_valid_profile_manager(session: Session, selected_profiles: str) -> list[Row]:
    return list(run_func(session, "GetValidProfileManager", selected_profiles).all())


def get_valid_profiles_for_selected(session: Session, selected_profiles: str) -> list[Row]:
    return list(run_func(session, "GetValidProfilesForSelected", selected_profiles).all())


def parse_string(session: Session, value: str) -> list[Row]:
    return list(run_func(session, "ParseString", value).all())
