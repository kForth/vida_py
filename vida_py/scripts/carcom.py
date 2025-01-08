from datetime import datetime
from typing import List

from sqlalchemy import Row
from sqlalchemy.orm import Session

from vida_py.scripts import runScript


def clean_up(session: Session) -> List[Row]:
    return runScript(session, "CleanUp").all()


def general__get_block_types(session: Session) -> List[Row]:
    return runScript(session, "general_GetBlockTypes").all()


def general__get_ecu_id(session: Session, ecu_identifier: str) -> List[Row]:
    return runScript(session, "general_GetEcuId", ecuIdentifier=ecu_identifier).all()


def general__get_text(session: Session, text_id: int) -> List[Row]:
    return runScript(session, "general_GetText", textId=text_id).all()


def nevis__delete_ecu_type(session: Session, identifier: str) -> List[Row]:
    return runScript(session, "nevis_DeleteEcuType", identifier=identifier).all()


def nevis__get_ecu_variants_by_profile(
    session: Session, profile_identifier: str
) -> List[Row]:
    return runScript(
        session, "nevis_GetEcuVariantsByProfile", ProfileIdentifier=profile_identifier
    ).all()


def nevis__get_language_id(session: Session, identifier: str, id: int) -> List[Row]:
    return runScript(session, "nevis_GetLanguageId", identifier=identifier, id=id).all()


def nevis__get_parameters_by_ecu_variant(
    session: Session, ecu_variant_identifier: str
) -> List[Row]:
    return runScript(
        session,
        "nevis_GetParametersByEcuVariant",
        ECUVariantIdentifier=ecu_variant_identifier,
    ).all()


def nevis__get_phrases(session: Session, last_call: datetime) -> List[Row]:
    return runScript(session, "nevis_GetPhrases", lastCall=last_call).all()


def nevis__get_profile_id(
    session: Session, profile_identifier: str, id: int
) -> List[Row]:
    return runScript(
        session, "nevis_GetProfileId", profileIdentifier=profile_identifier, id=id
    ).all()


def nevis__get_symptom_categories(session: Session, last_call: datetime) -> List[Row]:
    return runScript(session, "nevis_GetSymptomCategories", lastCall=last_call).all()


def nevis__get_symptoms(session: Session, last_call: datetime) -> List[Row]:
    return runScript(session, "nevis_GetSymptoms", lastCall=last_call).all()


def nevis__get_symptom_sections(session: Session, last_call: datetime) -> List[Row]:
    return runScript(session, "nevis_GetSymptomSections", lastCall=last_call).all()


def nevis__get_symptom_types(session: Session, last_call: datetime) -> List[Row]:
    return runScript(session, "nevis_GetSymptomTypes", lastCall=last_call).all()


def nevis__get_text_category_id(
    session: Session, tc_identifier: str, id: int
) -> List[Row]:
    return runScript(
        session, "nevis_GetTextCategoryId", tcIdentifier=tc_identifier, id=id
    ).all()


def nevis__import_profile(
    session: Session,
    identifier: str,
    value: str,
    type: str,
    note: str,
    modified_by: str,
    id: int,
) -> List[Row]:
    return runScript(
        session,
        "nevis_ImportProfile",
        identifier=identifier,
        value=value,
        type=type,
        note=note,
        modifiedBy=modified_by,
        id=id,
    ).all()


def nevis__insert_profile_parent(
    session: Session, identifier: str, parent: str, note: str, modified_by: str
) -> List[Row]:
    return runScript(
        session,
        "nevis_InsertProfileParent",
        identifier=identifier,
        parent=parent,
        note=note,
        modifiedBy=modified_by,
    ).all()


def nevis__insert_profile_value(
    session: Session, value: str, type: str, note: str, modified_by: str, id: int
) -> List[Row]:
    return runScript(
        session,
        "nevis_InsertProfileValue",
        value=value,
        type=type,
        note=note,
        modifiedBy=modified_by,
        id=id,
    ).all()


def nevis__insert_profile_value_type(
    session: Session, description: str, note: str, modified_by: str, id: int
) -> List[Row]:
    return runScript(
        session,
        "nevis_InsertProfileValueType",
        description=description,
        note=note,
        modifiedBy=modified_by,
        id=id,
    ).all()


def nevis__remove_parents_from_profile(session: Session, identifier: str) -> List[Row]:
    return runScript(
        session, "nevis_RemoveParentsFromProfile", identifier=identifier
    ).all()


def nevis__remove_values_from_profile(session: Session, identifier: str) -> List[Row]:
    return runScript(
        session, "nevis_RemoveValuesFromProfile", identifier=identifier
    ).all()


def nevis__update_ecu_type_text(
    session: Session,
    text_id: int,
    text: str,
    language_identifier: str,
    modified_by: str,
    note: str,
) -> List[Row]:
    return runScript(
        session,
        "nevis_UpdateEcuTypeText",
        textId=text_id,
        text=text,
        LanguageIdentifier=language_identifier,
        modifiedBy=modified_by,
        note=note,
    ).all()


def search_csc(
    session: Session, data: str, language: str, all: int, maxcount: int
) -> List[Row]:
    return runScript(
        session, "SearchCSC", Data=data, language=language, all=all, maxcount=maxcount
    ).all()


def service__get_init_timing_value(
    session: Session, i_fk_t100__ecu_variant: int, i_service: str, i_sub_function: str
) -> List[Row]:
    return runScript(
        session,
        "service_GetInitTimingValue",
        i_fkT100_EcuVariant=i_fk_t100__ecu_variant,
        i_service=i_service,
        i_subFunction=i_sub_function,
    ).all()


def service__get_init_timing_value_all(
    session: Session, i_fk_t100__ecu_variant: int
) -> List[Row]:
    return runScript(
        session,
        "service_GetInitTimingValueAll",
        i_fkT100_EcuVariant=i_fk_t100__ecu_variant,
    ).all()


def service__get_parameters(session: Session, ecu_id: int, parent_id: int) -> List[Row]:
    return runScript(
        session, "service_GetParameters", ecuId=ecu_id, parentId=parent_id
    ).all()


def service__get_parameter_values(
    session: Session, ecu_variant: str, parameter_text_id: int
) -> List[Row]:
    return runScript(
        session,
        "service_GetParameterValues",
        ecuVariant=ecu_variant,
        parameterTextId=parameter_text_id,
    ).all()


def service__get_service(session: Session, service: int) -> List[Row]:
    return runScript(session, "service_GetService", service=service).all()


def service___get_blocks(session: Session, ecu_id_list: str) -> List[Row]:
    return runScript(session, "service__GetBlocks", ecuIdList=ecu_id_list).all()


def service___get_structure(session: Session, ecu_id_list: str) -> List[Row]:
    return runScript(session, "service__GetStructure", ecuIdList=ecu_id_list).all()


def service___get_symptoms(session: Session, ecu_id_list: str) -> List[Row]:
    return runScript(session, "service__GetSymptoms", ecuIdList=ecu_id_list).all()


def service___get_texts(session: Session, ecu_id_list: str, language: str) -> List[Row]:
    return runScript(
        session, "service__GetTexts", ecuIdList=ecu_id_list, language=language
    ).all()


def se_browser__get_block(session: Session, block_id: int) -> List[Row]:
    return runScript(session, "se_browser_GetBlock", blockId=block_id).all()


def se_browser__get_block_children(
    session: Session, ecu_id: int, parent_id: int
) -> List[Row]:
    return runScript(
        session, "se_browser_GetBlockChildren", ecuId=ecu_id, parentId=parent_id
    ).all()


def se_browser__get_block_values(session: Session, block_id: int) -> List[Row]:
    return runScript(session, "se_browser_GetBlockValues", blockId=block_id).all()


def se_browser__get_ecus(session: Session) -> List[Row]:
    return runScript(session, "se_browser_GetEcus").all()


def se__get_block_types(session: Session) -> List[Row]:
    return runScript(session, "se_GetBlockTypes").all()


def se__get_ecu_addresses(session: Session) -> List[Row]:
    return runScript(session, "se_GetEcuAddresses").all()


def se__get_ecu_types(session: Session) -> List[Row]:
    return runScript(session, "se_GetEcuTypes").all()


def se__get_identifiers(session: Session, ecu_type: int, block_type: int) -> List[Row]:
    return runScript(
        session, "se_GetIdentifiers", ecuType=ecu_type, blockType=block_type
    ).all()


def se__get_identifiers_by_ecu_address(
    session: Session, ecu_address: str, block_type: int
) -> List[Row]:
    return runScript(
        session,
        "se_GetIdentifiersByEcuAddress",
        ecuAddress=ecu_address,
        blockType=block_type,
    ).all()


def se__get_identifiers_by_ecu_type(
    session: Session, ecu_type: int, block_type: int
) -> List[Row]:
    return runScript(
        session, "se_GetIdentifiersByEcuType", ecuType=ecu_type, blockType=block_type
    ).all()


def se__get_parameters(
    session: Session, ecu_type: int, block_type: int, identifier: str
) -> List[Row]:
    return runScript(
        session,
        "se_GetParameters",
        ecuType=ecu_type,
        blockType=block_type,
        identifier=identifier,
    ).all()


def se__get_parameters_by_ecu_address(
    session: Session, ecu_address: str, block_type: int, identifier: str
) -> List[Row]:
    return runScript(
        session,
        "se_GetParametersByEcuAddress",
        ecuAddress=ecu_address,
        blockType=block_type,
        identifier=identifier,
    ).all()


def se__get_parameters_by_ecu_type(
    session: Session, ecu_type: int, block_type: int, identifier: str
) -> List[Row]:
    return runScript(
        session,
        "se_GetParametersByEcuType",
        ecuType=ecu_type,
        blockType=block_type,
        identifier=identifier,
    ).all()


def se__get_parameter_values_by_ecu_type(
    session: Session, ecu_type: int, parameter_text_id: int
) -> List[Row]:
    return runScript(
        session,
        "se_GetParameterValuesByEcuType",
        ecuType=ecu_type,
        parameterTextId=parameter_text_id,
    ).all()


def se__get_profile_description(session: Session, profile_identifier: str) -> List[Row]:
    return runScript(
        session, "se_GetProfileDescription", profileIdentifier=profile_identifier
    ).all()


def se__get_profiles(
    session: Session,
    folder_level: int,
    model: int,
    year: int,
    engine: int,
    transmission: int,
    body: int,
    steering: int,
    market: int,
    unit: int,
    chassis_from: int,
    chassis_to: int,
) -> List[Row]:
    return runScript(
        session,
        "se_GetProfiles",
        folderLevel=folder_level,
        model=model,
        year=year,
        engine=engine,
        transmission=transmission,
        body=body,
        steering=steering,
        market=market,
        unit=unit,
        chassisFrom=chassis_from,
        chassisTo=chassis_to,
    ).all()


def se__get_profile_values(session: Session, type: int) -> List[Row]:
    return runScript(session, "se_GetProfileValues", type=type).all()


def se__get_profile_value_types(session: Session) -> List[Row]:
    return runScript(session, "se_GetProfileValueTypes").all()


def se__get_services(session: Session) -> List[Row]:
    return runScript(session, "se_GetServices").all()


def se__get_text(session: Session, id: int, language: int) -> List[Row]:
    return runScript(session, "se_GetText", id=id, language=language).all()


def se__get_texts(session: Session, search_criteria: str, language: int) -> List[Row]:
    return runScript(
        session, "se_GetTexts", searchCriteria=search_criteria, language=language
    ).all()


def se__get_texts2(session: Session, search_criteria: str, language: str) -> List[Row]:
    return runScript(
        session, "se_GetTexts2", searchCriteria=search_criteria, language=language
    ).all()


def vadis__get_all_customer_symptoms(session: Session, language_code: str) -> List[Row]:
    return runScript(
        session, "vadis_GetAllCustomerSymptoms", languageCode=language_code
    ).all()


def vadis__get_all_ecu_data_for_profile(session: Session, profile: str) -> List[Row]:
    return runScript(session, "vadis_GetAllEcuDataForProfile", profile=profile).all()


def vadis__get_allowed_ff_for_ecu_variant(
    session: Session, ecu_variant: int
) -> List[Row]:
    return runScript(
        session, "vadis_GetAllowedFFForEcuVariant", ecuVariant=ecu_variant
    ).all()


def vadis__get_all_possible_dtcs_on_ecu(
    session: Session, ecu_identifier: str
) -> List[Row]:
    return runScript(
        session, "vadis_GetAllPossibleDtcsOnEcu", ecuIdentifier=ecu_identifier
    ).all()


def vadis__get_component(
    session: Session,
    language_code: str,
    symptom_type: int,
    function_group1: int,
    function_group2: int,
) -> List[Row]:
    return runScript(
        session,
        "vadis_GetComponent",
        languageCode=language_code,
        symptomType=symptom_type,
        functionGroup1=function_group1,
        functionGroup2=function_group2,
    ).all()


def vadis__get_csc(
    session: Session,
    language_code: str,
    symptom_type: int,
    function_group1: int,
    function_group2: int,
    component: int,
) -> List[Row]:
    return runScript(
        session,
        "vadis_GetCSC",
        languageCode=language_code,
        symptomType=symptom_type,
        functionGroup1=function_group1,
        functionGroup2=function_group2,
        component=component,
    ).all()


def vadis__get_csc_by_id(session: Session, csc_id: int, language_code: str) -> List[Row]:
    return runScript(
        session, "vadis_GetCSCByID", cscID=csc_id, languageCode=language_code
    ).all()


def vadis__get_customer_symptom_code(
    session: Session, customer_symptom_id: int
) -> List[Row]:
    return runScript(
        session, "vadis_GetCustomerSymptomCode", customerSymptomId=customer_symptom_id
    ).all()


def vadis__get_customer_symptom_comment1(
    session: Session, customer_symptom_id: int, language_code: str
) -> List[Row]:
    return runScript(
        session,
        "vadis_GetCustomerSymptomComment1",
        customerSymptomId=customer_symptom_id,
        languageCode=language_code,
    ).all()


def vadis__get_customer_symptom_comment2(
    session: Session, customer_symptom_id: int, language_code: str
) -> List[Row]:
    return runScript(
        session,
        "vadis_GetCustomerSymptomComment2",
        customerSymptomId=customer_symptom_id,
        languageCode=language_code,
    ).all()


def vadis__get_customer_symptom_component_name(
    session: Session, customer_symptom_id: int, language_code: str
) -> List[Row]:
    return runScript(
        session,
        "vadis_GetCustomerSymptomComponentName",
        customerSymptomId=customer_symptom_id,
        languageCode=language_code,
    ).all()


def vadis__get_customer_symptom_deviation(
    session: Session, customer_symptom_id: int, language_code: str
) -> List[Row]:
    return runScript(
        session,
        "vadis_GetCustomerSymptomDeviation",
        customerSymptomId=customer_symptom_id,
        languageCode=language_code,
    ).all()


def vadis__get_customer_symptom_ids_from_dtc_symptom_ids(
    session: Session, dtc_symptom_ids: str
) -> List[Row]:
    return runScript(
        session,
        "vadis_GetCustomerSymptomIdsFromDtcSymptomIds",
        dtcSymptomIds=dtc_symptom_ids,
    ).all()


def vadis__get_default_code(
    session: Session, identifier: str, vehicle_profile: str
) -> List[Row]:
    return runScript(
        session,
        "vadis_GetDefaultCode",
        identifier=identifier,
        vehicleProfile=vehicle_profile,
    ).all()


def vadis__get_default_ecu_variants(session: Session, profile_id: str) -> List[Row]:
    return runScript(session, "vadis_GetDefaultEcuVariants", profileId=profile_id).all()


def vadis__get_diag_init(session: Session, config_id: int) -> List[Row]:
    return runScript(session, "vadis_GetDiagInit", configId=config_id).all()


def vadis__get_diag_timings(session: Session, config_id: int) -> List[Row]:
    return runScript(session, "vadis_GetDiagTimings", configId=config_id).all()


def vadis__get_dtc_symptom_ids_from_customer_symptom_id(
    session: Session, customer_symptom_id: int
) -> List[Row]:
    return runScript(
        session,
        "vadis_GetDtcSymptomIdsFromCustomerSymptomId",
        customerSymptomId=customer_symptom_id,
    ).all()


def vadis__get_dtc_symptoms_for_ecu(session: Session, ecu_id: int) -> List[Row]:
    return runScript(session, "vadis_GetDtcSymptomsForEcu", ecuId=ecu_id).all()


def vadis__get_ecu_init_from_config_id(session: Session, ecu_config_id: int) -> List[Row]:
    return runScript(
        session, "vadis_GetEcuInitFromConfigId", ecuConfigId=ecu_config_id
    ).all()


def vadis__get_ecu_type_descriptions(session: Session) -> List[Row]:
    return runScript(session, "vadis_GetEcuTypeDescriptions").all()


def vadis__get_ecu_types_and_dtc_codes_for_customer_symptom_ids_and_diagnostic_numbers(
    session: Session, customer_symptom_ids: str, diagnostic_numbers: str
) -> List[Row]:
    return runScript(
        session,
        "vadis_GetEcuTypesAndDtcCodesForCustomerSymptomIdsAndDiagnosticNumbers",
        customerSymptomIds=customer_symptom_ids,
        diagnosticNumbers=diagnostic_numbers,
    ).all()


def vadis__get_ecu_variant_data(session: Session, ecu_variant_id: int) -> List[Row]:
    return runScript(
        session, "vadis_GetEcuVariantData", ecuVariantId=ecu_variant_id
    ).all()


def vadis__get_ecu_variant_i_ds_by_cscid(session: Session, csc_id: int) -> List[Row]:
    return runScript(session, "vadis_GetEcuVariantIDsByCSCID", cscID=csc_id).all()


def vadis__get_ecu_variant_i_ds_by_symptom_i_ds(
    session: Session, symptom_ids: str
) -> List[Row]:
    return runScript(
        session, "vadis_GetEcuVariantIDsBySymptomIDs", symptomIds=symptom_ids
    ).all()


def vadis__get_function_group1(
    session: Session, language_code: str, symptom_type: int
) -> List[Row]:
    return runScript(
        session,
        "vadis_GetFunctionGroup1",
        languageCode=language_code,
        symptomType=symptom_type,
    ).all()


def vadis__get_function_group2(
    session: Session, language_code: str, symptom_type: int, function_group1: int
) -> List[Row]:
    return runScript(
        session,
        "vadis_GetFunctionGroup2",
        languageCode=language_code,
        symptomType=symptom_type,
        functionGroup1=function_group1,
    ).all()


def vadis__get_hw_settings(session: Session, vehicle_profile: str) -> List[Row]:
    return runScript(session, "vadis_GetHwSettings", vehicleProfile=vehicle_profile).all()


def vadis__get_number_of_dtcs_on_ecu(session: Session, ecu_id: int) -> List[Row]:
    return runScript(session, "vadis_GetNumberOfDtcsOnEcu", ecuId=ecu_id).all()


def vadis__get_parameter_data(
    session: Session, ecu_id: int, text_id: int, language_code: str, identifier: str
) -> List[Row]:
    return runScript(
        session,
        "vadis_GetParameterData",
        ecuId=ecu_id,
        textId=text_id,
        languageCode=language_code,
        identifier=identifier,
    ).all()


def vadis__get_protocols_for_profile(session: Session, profile: str) -> List[Row]:
    return runScript(session, "vadis_GetProtocolsForProfile", profile=profile).all()


def vadis__get_security_code_from_ecu_type(session: Session, ecu_type: int) -> List[Row]:
    return runScript(session, "vadis_GetSecurityCodeFromEcuType", ecuType=ecu_type).all()


def vadis__get_symptom(session: Session, block_value_id: int) -> List[Row]:
    return runScript(session, "vadis_GetSymptom", blockValueId=block_value_id).all()


def vadis__get_symptom_status_text(
    session: Session, symptom_id: int, ecu_variant_identifier: str, language_code: str
) -> List[Row]:
    return runScript(
        session,
        "vadis_GetSymptomStatusText",
        symptomId=symptom_id,
        ecuVariantIdentifier=ecu_variant_identifier,
        languageCode=language_code,
    ).all()


def vadis__get_symptom_type(session: Session, language_code: str) -> List[Row]:
    return runScript(session, "vadis_GetSymptomType", languageCode=language_code).all()


def vadis__get_text(session: Session, text_id: int, language_code: str) -> List[Row]:
    return runScript(
        session, "vadis_GetText", textId=text_id, languageCode=language_code
    ).all()
