from typing import List

from sqlalchemy import Row
from sqlalchemy.orm import Session

from vida_py.scripts import runScript


def clean_up(session: Session) -> List[Row]:
    return runScript(session, "CleanUp").all()


def get_available_sw_products(
    session: Session, model_id: int, language: str
) -> List[Row]:
    return runScript(
        session, "GetAvailableSWProducts", modelId=model_id, language=language
    ).all()


def get_components_from_profile(session: Session, profile: str) -> List[Row]:
    return runScript(session, "GetComponentsFromProfile", profile=profile).all()


def get_csc_id_for_selected_ie_id(
    session: Session, ie_id: str, profile_list: str
) -> List[Row]:
    return runScript(
        session, "GetCSCIDForSelectedIEID", ieId=ie_id, profileList=profile_list
    ).all()


def get_delivery_check_ies(
    session: Session, language_code: str, symptom_ids: str, profile_list: str
) -> List[Row]:
    return runScript(
        session,
        "GetDeliveryCheckIEs",
        languageCode=language_code,
        symptomIds=symptom_ids,
        profileList=profile_list,
    ).all()


def get_dtc_ies(
    session: Session, language_code: str, symptom_ids: str, profile_list: str
) -> List[Row]:
    return runScript(
        session,
        "GetDtcIEs",
        languageCode=language_code,
        symptomIds=symptom_ids,
        profileList=profile_list,
    ).all()


def get_ecu_description(session: Session, ecu_type: int, language_code: str) -> List[Row]:
    return runScript(
        session, "GetEcuDescription", ecuType=ecu_type, languageCode=language_code
    ).all()


def get_ecu_ies(
    session: Session, ecu_type: int, language: str, profile_list: str
) -> List[Row]:
    return runScript(
        session,
        "GetEcuIEs",
        ecuType=ecu_type,
        language=language,
        profileList=profile_list,
    ).all()


def get_ecus(session: Session) -> List[Row]:
    return runScript(session, "GetEcus").all()


def get_first_test_group(session: Session, ie_id: str) -> List[Row]:
    return runScript(session, "GetFirstTestGroup", ieID=ie_id).all()


def get_ie(
    session: Session, symptomid: int, profile_list: str, language: str
) -> List[Row]:
    return runScript(
        session, "GetIE", symptomid=symptomid, profileList=profile_list, language=language
    ).all()


def get_ie_from_symptom(
    session: Session, symptom_id: int, symptom_type: str, profile_list: str
) -> List[Row]:
    return runScript(
        session,
        "GetIEFromSymptom",
        symptomId=symptom_id,
        symptomType=symptom_type,
        profileList=profile_list,
    ).all()


def get_matched_valid_profiles_by_ie_id(
    session: Session, profiles: str, ieid: str
) -> List[Row]:
    return runScript(
        session, "GetMatchedValidProfilesByIeID", profiles=profiles, IEID=ieid
    ).all()


def get_model_and_model_year_from_vin(session: Session, vin: str) -> List[Row]:
    return runScript(session, "GetModelAndModelYearFromVIN", vin=vin).all()


def get_model_name(session: Session, modelid: int) -> List[Row]:
    return runScript(session, "GetModelName", modelid=modelid).all()


def get_nav_image(session: Session, vehicle_profile: str) -> List[Row]:
    return runScript(session, "GetNavImage", vehicleProfile=vehicle_profile).all()


def get_observable_symptoms_from_dtc_symptom(
    session: Session, dtc_symptom_id: int, lang_code: str
) -> List[Row]:
    return runScript(
        session,
        "GetObservableSymptomsFromDtcSymptom",
        dtcSymptomId=dtc_symptom_id,
        langCode=lang_code,
    ).all()


def get_profile_from_components(
    session: Session, model: int, year_description: str, engine: int, transm: int
) -> List[Row]:
    return runScript(
        session,
        "GetProfileFromComponents",
        model=model,
        yearDescription=year_description,
        engine=engine,
        transm=transm,
    ).all()


def get_profiles_from_model_id(session: Session, model_id: int) -> List[Row]:
    return runScript(session, "GetProfilesFromModelId", modelId=model_id).all()


def get_profile_string(session: Session, profile: str) -> List[Row]:
    return runScript(session, "GetProfileString", profile=profile).all()


def get_reference_ie(
    session: Session, symptomid: int, profile_list: str, language: str
) -> List[Row]:
    return runScript(
        session,
        "GetReferenceIE",
        symptomid=symptomid,
        profileList=profile_list,
        language=language,
    ).all()


def get_related_ies(
    session: Session, symptomid: int, profile_list: str, language: str
) -> List[Row]:
    return runScript(
        session,
        "GetRelatedIEs",
        symptomid=symptomid,
        profileList=profile_list,
        language=language,
    ).all()


def get_related_ies_for_customer_symptom_id(
    session: Session, customersymptomid: int, profile_list: str, language: str
) -> List[Row]:
    return runScript(
        session,
        "GetRelatedIEsForCustomerSymptomId",
        customersymptomid=customersymptomid,
        profileList=profile_list,
        language=language,
    ).all()


def get_related_observable_symptom_ids(
    session: Session, dtc_symptoms_list: str, profile_list: str
) -> List[Row]:
    return runScript(
        session,
        "GetRelatedObservableSymptomIds",
        dtcSymptomsList=dtc_symptoms_list,
        profileList=profile_list,
    ).all()


def get_script(
    session: Session,
    script_type: str,
    profile_list: str,
    script_id: str,
    language_code: str,
    ecu_type: int,
) -> List[Row]:
    return runScript(
        session,
        "GetScript",
        scriptType=script_type,
        profileList=profile_list,
        scriptId=script_id,
        languageCode=language_code,
        ecuType=ecu_type,
    ).all()


def get_script_variant_and_version(session: Session, resource_id: str) -> List[Row]:
    return runScript(session, "GetScriptVariantAndVersion", resourceId=resource_id).all()


def get_smart_tool_script(
    session: Session, smart_tool_id: str, profile_list: str, language_code: str
) -> List[Row]:
    return runScript(
        session,
        "GetSmartToolScript",
        smartToolId=smart_tool_id,
        profileList=profile_list,
        languageCode=language_code,
    ).all()


def get_swdl_supported_vehicle_models(session: Session) -> List[Row]:
    return runScript(session, "GetSWDLSupportedVehicleModels").all()


def get_sw_product(session: Session, sw_product_id: int, language: str) -> List[Row]:
    return runScript(
        session, "GetSWProduct", swProductId=sw_product_id, language=language
    ).all()


def get_sw_product_notes(session: Session, sw_product_id: int) -> List[Row]:
    return runScript(session, "GetSWProductNotes", swProductId=sw_product_id).all()


def get_symptom_descriptions(
    session: Session, symptom_ids: str, language_code: str
) -> List[Row]:
    return runScript(
        session,
        "GetSymptomDescriptions",
        symptomIds=symptom_ids,
        languageCode=language_code,
    ).all()


def get_symptom_ids_for_selected_ie_id(session: Session, ie_id: str) -> List[Row]:
    return runScript(session, "GetSymptomIDsForSelectedIEID", ieId=ie_id).all()


def get_symptoms(session: Session, profile_list: str, language: str) -> List[Row]:
    return runScript(
        session, "GetSymptoms", profileList=profile_list, language=language
    ).all()


def get_symptoms_with_tests(
    session: Session, profile_list: str, language: str
) -> List[Row]:
    return runScript(
        session, "GetSymptomsWithTests", profileList=profile_list, language=language
    ).all()


def get_valid_links_for_selected(
    session: Session, profile_list: str, project_document_id: str, language_code: str
) -> List[Row]:
    return runScript(
        session,
        "GetValidLinksForSelected",
        profileList=profile_list,
        projectDocumentId=project_document_id,
        languageCode=language_code,
    ).all()


def get_variant(session: Session, chronicle_id: str) -> List[Row]:
    return runScript(session, "GetVariant", chronicleId=chronicle_id).all()


def get_vin_components(session: Session, vin: str) -> List[Row]:
    return runScript(session, "GetVINcomponents", vin=vin).all()


def get_year_models(session: Session, modelid: int) -> List[Row]:
    return runScript(session, "GetYearModels", modelid=modelid).all()


def script__get_valid_profiles_for_selected(
    session: Session, profile_list: str
) -> List[Row]:
    return runScript(
        session, "script_GetValidProfilesForSelected", profileList=profile_list
    ).all()
