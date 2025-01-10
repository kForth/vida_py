from typing import List

from sqlalchemy import Row
from sqlalchemy.orm import Session

from vida_py.funcs import run_func


def get_profile_full_title(session: Session, fk_profile: str) -> str:
    return run_func(session, "getProfileFullTitle", fk_profile).all()


def get_profile_model_year_desc(session: Session, fk_profile: str) -> str:
    return run_func(session, "getProfileModelYearDesc", fk_profile).all()


def get_profile_nav_title(session: Session, fk_profile: str) -> str:
    return run_func(session, "getProfileNavTitle", fk_profile).all()


def get_profiles_full_title(session: Session, selected_profiles: str) -> str:
    return run_func(session, "getProfilesFullTitle", selected_profiles).all()


def get_profile_vehicle_model_desc(session: Session, fk_profile: str) -> str:
    return run_func(session, "getProfileVehicleModelDesc", fk_profile).all()


def get_valid_profile_manager(session: Session, selected_profiles: str) -> List[Row]:
    return run_func(session, "GetValidProfileManager", selected_profiles).all()


def get_valid_profiles_for_selected(
    session: Session, selected_profiles: str
) -> List[Row]:
    return run_func(session, "GetValidProfilesForSelected", selected_profiles).all()


def parse_string(session: Session, parse_string: str) -> List[Row]:
    return run_func(session, "ParseString", parse_string).all()
