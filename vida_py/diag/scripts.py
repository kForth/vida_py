"""Stored procedure wrapper functions for the diag VIDA database."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from sqlalchemy import Row
from sqlalchemy.orm import Session

from vida_py.util import run_script


def clean_up(session: Session) -> list[Row]:
    return list(run_script(session, "CleanUp").all())


def get_available_sw_products(session: Session, model_id: int, language: str) -> list[Row]:
    return list(
        run_script(session, "GetAvailableSWProducts", modelId=model_id, language=language).all()
    )


def get_components_from_profile(session: Session, profile: str) -> list[Row]:
    return list(run_script(session, "GetComponentsFromProfile", profile=profile).all())


def get_csc_id_for_selected_ie_id(session: Session, ie_id: str, profile_list: str) -> list[Row]:
    return list(
        run_script(session, "GetCSCIDForSelectedIEID", ieId=ie_id, profileList=profile_list).all()
    )


def get_delivery_check_ies(
    session: Session, language_code: str, symptom_ids: str, profile_list: str
) -> list[Row]:
    return list(
        run_script(
            session,
            "GetDeliveryCheckIEs",
            languageCode=language_code,
            symptomIds=symptom_ids,
            profileList=profile_list,
        ).all()
    )


def get_dtc_ies(
    session: Session, language_code: str, symptom_ids: str, profile_list: str
) -> list[Row]:
    return list(
        run_script(
            session,
            "GetDtcIEs",
            languageCode=language_code,
            symptomIds=symptom_ids,
            profileList=profile_list,
        ).all()
    )


def get_ecu_description(session: Session, ecu_type: int, language_code: str) -> list[Row]:
    return list(
        run_script(session, "GetEcuDescription", ecuType=ecu_type, languageCode=language_code).all()
    )


def get_ecu_ies(session: Session, ecu_type: int, language: str, profile_list: str) -> list[Row]:
    return list(
        run_script(
            session,
            "GetEcuIEs",
            ecuType=ecu_type,
            language=language,
            profileList=profile_list,
        ).all()
    )


def get_ecus(session: Session) -> list[Row]:
    return list(run_script(session, "GetEcus").all())


def get_first_test_group(session: Session, ie_id: str) -> list[Row]:
    return list(run_script(session, "GetFirstTestGroup", ieID=ie_id).all())


def get_ie(session: Session, symptomid: int, profile_list: str, language: str) -> list[Row]:
    return list(
        run_script(
            session, "GetIE", symptomid=symptomid, profileList=profile_list, language=language
        ).all()
    )


def get_ie_from_symptom(
    session: Session, symptom_id: int, symptom_type: str, profile_list: str
) -> list[Row]:
    return list(
        run_script(
            session,
            "GetIEFromSymptom",
            symptomId=symptom_id,
            symptomType=symptom_type,
            profileList=profile_list,
        ).all()
    )


def get_matched_valid_profiles_by_ie_id(session: Session, profiles: str, ieid: str) -> list[Row]:
    return list(
        run_script(session, "GetMatchedValidProfilesByIeID", profiles=profiles, IEID=ieid).all()
    )


def get_model_and_model_year_from_vin(session: Session, vin: str) -> list[Row]:
    return list(run_script(session, "GetModelAndModelYearFromVIN", vin=vin).all())


def get_model_name(session: Session, modelid: int) -> list[Row]:
    return list(run_script(session, "GetModelName", modelid=modelid).all())


def get_nav_image(session: Session, vehicle_profile: str) -> list[Row]:
    return list(run_script(session, "GetNavImage", vehicleProfile=vehicle_profile).all())


def get_observable_symptoms_from_dtc_symptom(
    session: Session, dtc_symptom_id: int, lang_code: str
) -> list[Row]:
    return list(
        run_script(
            session,
            "GetObservableSymptomsFromDtcSymptom",
            dtcSymptomId=dtc_symptom_id,
            langCode=lang_code,
        ).all()
    )


def get_profile_from_components(
    session: Session, model: int, year_description: str, engine: int, transm: int
) -> list[Row]:
    return list(
        run_script(
            session,
            "GetProfileFromComponents",
            model=model,
            yearDescription=year_description,
            engine=engine,
            transm=transm,
        ).all()
    )


def get_profiles_from_model_id(session: Session, model_id: int) -> list[Row]:
    return list(run_script(session, "GetProfilesFromModelId", modelId=model_id).all())


def get_profile_string(session: Session, profile: str) -> list[Row]:
    return list(run_script(session, "GetProfileString", profile=profile).all())


def get_reference_ie(
    session: Session, symptomid: int, profile_list: str, language: str
) -> list[Row]:
    return list(
        run_script(
            session,
            "GetReferenceIE",
            symptomid=symptomid,
            profileList=profile_list,
            language=language,
        ).all()
    )


def get_related_ies(
    session: Session, symptomid: int, profile_list: str, language: str
) -> list[Row]:
    return list(
        run_script(
            session,
            "GetRelatedIEs",
            symptomid=symptomid,
            profileList=profile_list,
            language=language,
        ).all()
    )


def get_related_ies_for_customer_symptom_id(
    session: Session, customersymptomid: int, profile_list: str, language: str
) -> list[Row]:
    return list(
        run_script(
            session,
            "GetRelatedIEsForCustomerSymptomId",
            customersymptomid=customersymptomid,
            profileList=profile_list,
            language=language,
        ).all()
    )


def get_related_observable_symptom_ids(
    session: Session, dtc_symptoms_list: str, profile_list: str
) -> list[Row]:
    return list(
        run_script(
            session,
            "GetRelatedObservableSymptomIds",
            dtcSymptomsList=dtc_symptoms_list,
            profileList=profile_list,
        ).all()
    )


def get_script(
    session: Session,
    script_type: str,
    profile_list: str,
    script_id: str,
    language_code: str,
    ecu_type: int,
) -> list[Row]:
    return list(
        run_script(
            session,
            "GetScript",
            scriptType=script_type,
            profileList=profile_list,
            scriptId=script_id,
            languageCode=language_code,
            ecuType=ecu_type,
        ).all()
    )


def get_script_variant_and_version(session: Session, resource_id: str) -> list[Row]:
    return list(run_script(session, "GetScriptVariantAndVersion", resourceId=resource_id).all())


def get_smart_tool_script(
    session: Session, smart_tool_id: str, profile_list: str, language_code: str
) -> list[Row]:
    return list(
        run_script(
            session,
            "GetSmartToolScript",
            smartToolId=smart_tool_id,
            profileList=profile_list,
            languageCode=language_code,
        ).all()
    )


def get_swdl_supported_vehicle_models(session: Session) -> list[Row]:
    return list(run_script(session, "GetSWDLSupportedVehicleModels").all())


def get_sw_product(session: Session, sw_product_id: int, language: str) -> list[Row]:
    return list(
        run_script(session, "GetSWProduct", swProductId=sw_product_id, language=language).all()
    )


def get_sw_product_notes(session: Session, sw_product_id: int) -> list[Row]:
    return list(run_script(session, "GetSWProductNotes", swProductId=sw_product_id).all())


def get_symptom_descriptions(session: Session, symptom_ids: str, language_code: str) -> list[Row]:
    return list(
        run_script(
            session,
            "GetSymptomDescriptions",
            symptomIds=symptom_ids,
            languageCode=language_code,
        ).all()
    )


def get_symptom_ids_for_selected_ie_id(session: Session, ie_id: str) -> list[Row]:
    return list(run_script(session, "GetSymptomIDsForSelectedIEID", ieId=ie_id).all())


def get_symptoms(session: Session, profile_list: str, language: str) -> list[Row]:
    return list(
        run_script(session, "GetSymptoms", profileList=profile_list, language=language).all()
    )


def get_symptoms_with_tests(session: Session, profile_list: str, language: str) -> list[Row]:
    return list(
        run_script(
            session, "GetSymptomsWithTests", profileList=profile_list, language=language
        ).all()
    )


def get_valid_links_for_selected(
    session: Session, profile_list: str, project_document_id: str, language_code: str
) -> list[Row]:
    return list(
        run_script(
            session,
            "GetValidLinksForSelected",
            profileList=profile_list,
            projectDocumentId=project_document_id,
            languageCode=language_code,
        ).all()
    )


def get_variant(session: Session, chronicle_id: str) -> list[Row]:
    return list(run_script(session, "GetVariant", chronicleId=chronicle_id).all())


def get_vin_components(session: Session, vin: str) -> list[Row]:
    return list(run_script(session, "GetVINcomponents", vin=vin).all())


def get_year_models(session: Session, modelid: int) -> list[Row]:
    return list(run_script(session, "GetYearModels", modelid=modelid).all())


def script__get_valid_profiles_for_selected(session: Session, profile_list: str) -> list[Row]:
    return list(
        run_script(session, "script_GetValidProfilesForSelected", profileList=profile_list).all()
    )


STORED_PROCEDURES = {
    "CleanUp": clean_up,
    "GetAvailableSWProducts": get_available_sw_products,
    "GetComponentsFromProfile": get_components_from_profile,
    "GetCSCIDForSelectedIEID": get_csc_id_for_selected_ie_id,
    "GetDeliveryCheckIEs": get_delivery_check_ies,
    "GetDtcIEs": get_dtc_ies,
    "GetEcuDescription": get_ecu_description,
    "GetEcuIEs": get_ecu_ies,
    "GetEcus": get_ecus,
    "GetFirstTestGroup": get_first_test_group,
    "GetIE": get_ie,
    "GetIEFromSymptom": get_ie_from_symptom,
    "GetMatchedValidProfilesByIeID": get_matched_valid_profiles_by_ie_id,
    "GetModelAndModelYearFromVIN": get_model_and_model_year_from_vin,
    "GetModelName": get_model_name,
    "GetNavImage": get_nav_image,
    "GetObservableSymptomsFromDtcSymptom": get_observable_symptoms_from_dtc_symptom,
    "GetProfileFromComponents": get_profile_from_components,
    "GetProfilesFromModelId": get_profiles_from_model_id,
    "GetProfileString": get_profile_string,
    "GetReferenceIE": get_reference_ie,
    "GetRelatedIEs": get_related_ies,
    "GetRelatedIEsForCustomerSymptomId": get_related_ies_for_customer_symptom_id,
    "GetRelatedObservableSymptomIds": get_related_observable_symptom_ids,
    "GetScript": get_script,
    "GetScriptVariantAndVersion": get_script_variant_and_version,
    "GetSmartToolScript": get_smart_tool_script,
    "GetSWDLSupportedVehicleModels": get_swdl_supported_vehicle_models,
    "GetSWProduct": get_sw_product,
    "GetSWProductNotes": get_sw_product_notes,
    "GetSymptomDescriptions": get_symptom_descriptions,
    "GetSymptomIDsForSelectedIEID": get_symptom_ids_for_selected_ie_id,
    "GetSymptoms": get_symptoms,
    "GetSymptomsWithTests": get_symptoms_with_tests,
    "GetValidLinksForSelected": get_valid_links_for_selected,
    "GetVariant": get_variant,
    "GetVINcomponents": get_vin_components,
    "GetYearModels": get_year_models,
    "script_GetValidProfilesForSelected": script__get_valid_profiles_for_selected,
}
