"""SQL function wrapper helpers for the basedata VIDA database."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from sqlalchemy import Row
from sqlalchemy.orm import Session

from vida_py.util import run_func, run_func_scalar


def get_profile_full_title(session: Session, fk_profile: str) -> str:
    return run_func_scalar(session, "getProfileFullTitle", fk_profile)


def get_profile_model_year_desc(session: Session, fk_profile: str) -> str:
    return run_func_scalar(session, "getProfileModelYearDesc", fk_profile)


def get_profile_nav_title(session: Session, fk_profile: str) -> str:
    return run_func_scalar(session, "getProfileNavTitle", fk_profile)


def get_profiles_full_title(session: Session, selected_profiles: str) -> str:
    return run_func_scalar(session, "getProfilesFullTitle", selected_profiles)


def get_profile_vehicle_model_desc(session: Session, fk_profile: str) -> str:
    return run_func_scalar(session, "getProfileVehicleModelDesc", fk_profile)


def get_valid_profile_manager(session: Session, selected_profiles: str) -> list[Row]:
    return list(run_func(session, "GetValidProfileManager", selected_profiles).all())


def get_valid_profiles_for_selected(session: Session, selected_profiles: str) -> list[Row]:
    return list(run_func(session, "GetValidProfilesForSelected", selected_profiles).all())


def parse_string(session: Session, value: str) -> list[Row]:
    return list(run_func(session, "ParseString", value).all())


FUNCTIONS = {
    "getProfileFullTitle": get_profile_full_title,
    "getProfileModelYearDesc": get_profile_model_year_desc,
    "getProfileNavTitle": get_profile_nav_title,
    "getProfilesFullTitle": get_profiles_full_title,
    "getProfileVehicleModelDesc": get_profile_vehicle_model_desc,
    "GetValidProfileManager": get_valid_profile_manager,
    "GetValidProfilesForSelected": get_valid_profiles_for_selected,
    "ParseString": parse_string,
}
