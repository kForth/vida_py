# vida_py

[![GitHub](https://img.shields.io/badge/github-repo-blue?logo=github)](https://github.com/kForth/vida_py)
[![GitHub License](https://img.shields.io/github/license/kforth/vida_py)](https://github.com/kForth/vida_py/blob/main/LICENSE)
[![GitHub Forks](https://img.shields.io/github/forks/kforth/vida_py)](https://github.com/kForth/vida_py/forks)
[![GitHub Stars](https://img.shields.io/github/stars/kforth/vida_py)](https://github.com/kForth/vida_py/stargazers)

[![PyPI Version](https://img.shields.io/pypi/v/vida_py?logo=python&logoColor=white)](https://pypi.org/p/vida_py)
![Pepy Total Downloads](https://img.shields.io/pepy/dt/vida_py)
![PyPI Downloads](https://img.shields.io/pypi/dm/vida_py)

Python interface Volvo's VIDA databases.

## Installation

You can install `vida_py` using pip.

```
  pip install vida-py
```

## Dependencies

`vida_py` depends on a few python modules, these modules will be installed automatically when installing with `pip`.

`vida_py` is compatible with python 3.13 and up.

## Database Configuration

`vida_py` uses SQLAlchemy database connection URIs from environment variables.

Required environment variables:

- `VIDA_ACCESS_DB_URI`
- `VIDA_BASEDATA_DB_URI`
- `VIDA_CARCOM_DB_URI`
- `VIDA_DIAG_DB_URI`
- `VIDA_EPC_DB_URI`
- `VIDA_IMAGES_DB_URI`
- `VIDA_SERVICE_DB_URI`
- `VIDA_SESSION_DB_URI`
- `VIDA_TIMING_DB_URI`

Each value must be a valid SQLAlchemy database URI:

```bash
"mssql+pyodbc://user:password@localhost/basedata?driver=ODBC+Driver+17+for+SQL+Server"
```

Explicit setup is also available for every database module. For example:

```python
from vida_py.basedata import create_engine_from_url, create_session_factory

engine = create_engine_from_url(
  "mssql+pyodbc://user:password@localhost/basedata?driver=ODBC+Driver+17+for+SQL+Server"
)
Session = create_session_factory(engine=engine)

with Session() as session:
  ...
```

## VIDA Database Files

Please note that VIDA database files are not supplied with this package. Users must obtain these files separately, typically from an existing VIDA installation.

The easiest way to access Volvo's VIDA databases is to extract the `.mdf` and `.ldf` files from the VIDA installer, then attached them to a database using the `Microsoft SQL Server Management Studio`

## Contributing

Contributions are welcome! Please submit a pull request or open and issue to discuss changes or report bugs.

## License

vida_py (C) 2026 Kestin Goforth.

This project is licensed under the BSD 3-Clause License - see the [license file](LICENSE) for details.
