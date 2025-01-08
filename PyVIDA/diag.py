from dataclasses import dataclass
from typing import List

from sqlalchemy import Row
from sqlalchemy.orm import Session

from PyVIDA.util import runScript


def GetAvailableSWProducts(session: Session, model_id: int, language: str) -> List[Row]:
    return runScript(
        session, "GetAvailableSWProducts", modelId=model_id, language=language
    ).all()


def GetComponentsFromProfile(session: Session, profile: str) -> List[Row]:
    return runScript(session, "GetComponentsFromProfile", profile=profile).all()


def GetCSCIDForSelectedIEID(session: Session, ie_id: str, profile_list: str) -> List[Row]:
    return runScript(
        session, "GetCSCIDForSelectedIEID", ieId=ie_id, profileList=profile_list
    ).all()


def GetDeliveryCheckIEs(
    session: Session,
    language_code: str,
    profile_list: str,
    symptom_ids: str,
) -> List[Row]:
    return runScript(
        session,
        "GetDeliveryCheckIEs",
        languageCode=language_code,
        profileList=profile_list,
        symptomIds=symptom_ids,
    ).all()


def GetDtcIEs(
    session: Session,
    language_code: str,
    profile_list: str,
    symptom_ids: str,
) -> List[Row]:
    return runScript(
        session,
        "GetDtcIEs",
        languageCode=language_code,
        profileList=profile_list,
        symptomIds=symptom_ids,
    ).all()


def GetEcuDescription(
    session: Session,
    ecu_type: int,
    language_code: str,
) -> List[Row]:
    return runScript(
        session,
        "GetEcuDescription",
        ecuType=ecu_type,
        languageCode=language_code,
    ).all()


def GetEcuIEs(
    session: Session,
    ecu_type: int,
    language_code: str,
    profile_list: str,
) -> List[Row]:
    return runScript(
        session,
        "GetEcuIEs",
        ecuType=ecu_type,
        languageCode=language_code,
        profileList=profile_list,
    ).all()


def GetEcus(session: Session) -> List[Row]:
    return runScript(session, "GetEcus").all()


def GetFirstTestGroup(
    session: Session,
    ie_id: str,
) -> List[Row]:
    return runScript(
        session,
        "GetFirstTestGroup",
        ieID=ie_id,
    ).all()


def GetIE(
    session: Session,
    symptom_id: int,
    language_code: str,
    profile_list: str,
) -> List[Row]:
    return runScript(
        session,
        "GetIE",
        symptomid=symptom_id,
        languageCode=language_code,
        profileList=profile_list,
    ).all()


def GetIEFromSymptom(
    session: Session,
    symptom_id: int,
    symptom_type: str,
    profile_list: str,
) -> List[Row]:
    return runScript(
        session,
        "GetIEFromSymptom",
        symptomid=symptom_id,
        symptomType=symptom_type,
        profileList=profile_list,
    ).all()


def GetMatchedValidProfilesByIeID(
    session: Session,
    profiles: str,
    ie_id: int,
) -> List[Row]:
    return runScript(
        session,
        "GetMatchedValidProfilesByIeID",
        profiles=profiles,
        IEID=ie_id,
    ).all()


def GetModelAndModelYearFromVIN(session: Session, vin: str) -> Row:
    return runScript(session, "GetModelAndModelYearFromVIN", vin=vin).first()


def GetModelName(session: Session, model_id: int) -> Row:
    return runScript(session, "GetModelName", modelid=model_id).first()


def GetNavImage(session: Session, profile: str) -> Row:
    return runScript(session, "GetNavImage", profile=profile).first()


def GetObservableSymptomsFromDtcSymptom(
    session: Session,
    dtc_symptom_id: int,
    language_code: str,
) -> List[Row]:
    return runScript(
        session,
        "GetObservableSymptomsFromDtcSymptom",
        dtcSymptomId=dtc_symptom_id,
        langCode=language_code,
    ).all()


def GetProfilesFromModelId(session: Session, model_id: int) -> List[Row]:
    return runScript(session, "GetProfilesFromModelId", modelId=model_id).all()


def GetProfileString(session: Session, profile: str) -> List[Row]:
    return runScript(session, "GetProfileString", profile=profile).all()


def GetReferenceIE(
    session: Session,
    symptom_id: int,
    profile_list: str,
    language: int,
) -> List[Row]:
    return runScript(
        session,
        "GetReferenceIE",
        symptomId=symptom_id,
        profileList=profile_list,
        language=language,
    ).all()


def GetRelatedIEs(
    session: Session,
    symptom_id: int,
    profile_list: str,
    language: int,
) -> List[Row]:
    return runScript(
        session,
        "GetRelatedIEs",
        symptomId=symptom_id,
        profileList=profile_list,
        language=language,
    ).all()


def GetRelatedIEsForCustomerSymptomId(
    session: Session,
    customer_symptom_id: int,
    profile_list: str,
    language: int,
) -> List[Row]:
    return runScript(
        session,
        "GetRelatedIEsForCustomerSymptomId",
        customerSymptomId=customer_symptom_id,
        profileList=profile_list,
        language=language,
    ).all()


def GetRelatedObservableSymptomIds(
    session: Session, dtc_symptoms_list: str, profile_list: str
) -> List[Row]:
    return runScript(
        session,
        "GetRelatedObservableSymptomIds",
        dtcSymptomsList=dtc_symptoms_list,
        profileList=profile_list,
    ).all()


def GetScript(
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


def GetScriptVariantAndVersion(session: Session, resource_id: str) -> List[Row]:
    return runScript(session, "GetScriptVariantAndVersion", resourceId=resource_id).all()


def GetSmartToolScript(
    session: Session,
    smart_tool_id: str,
    profile_list: str,
    language_code: str,
) -> List[Row]:
    return runScript(
        session,
        "GetSmartToolScript",
        smartToolId=smart_tool_id,
        profileList=profile_list,
        languageCode=language_code,
    ).all()


def GetSWDLSupportedVehicleModels(session: Session) -> List[Row]:
    return runScript(session, "GetSWDLSupportedVehicleModels").all()


def GetSWProduct(
    session: Session,
    sw_product_id: int,
    language: str,
) -> List[Row]:
    return runScript(
        session,
        "GetSWProduct",
        swProductId=sw_product_id,
        language=language,
    ).all()


def GetSWProductNotes(session: Session, sw_product_id: int) -> List[Row]:
    return runScript(session, "GetSWProductNotes", swProductId=sw_product_id).all()


def GetSymptomDescriptions(
    session: Session,
    symptom_ids: str,
    language_code: str,
) -> List[Row]:
    return runScript(
        session,
        "GetSymptomDescriptions",
        symptomIds=symptom_ids,
        languageCode=language_code,
    ).all()


def GetSymptomIDsForSelectedIEID(session: Session, ie_id: str) -> List[Row]:
    return runScript(session, "GetSymptomIDsForSelectedIEID", ieId=ie_id).all()


def GetSymptoms(
    session: Session,
    profile_list: str,
    language: str,
) -> List[Row]:
    return runScript(
        session,
        "GetSymptoms",
        profileList=profile_list,
        language=language,
    ).all()


def GetSymptomsWithTests(
    session: Session,
    profile_list: str,
    language: str,
) -> List[Row]:
    return runScript(
        session,
        "GetSymptomsWithTests",
        profileList=profile_list,
        language=language,
    ).all()


def GetValidLinksForSelected(
    session: Session,
    profile_list: str,
    project_document_id: str,
    language: str,
) -> List[Row]:
    return runScript(
        session,
        "GetValidLinksForSelected",
        profileList=profile_list,
        projectDocumentId=project_document_id,
        language=language,
    ).all()


def GetVariant(session: Session, chronicle_id: str) -> List[Row]:
    return runScript(session, "GetVariant", chronicleId=chronicle_id).all()


@dataclass
class VINcomponents:
    model_id: int
    model: str
    year: str
    engine_id: int
    engine: str
    transmission_id: int
    transmission: str


def GetVINcomponents(session: Session, vin: str) -> VINcomponents:
    return VINcomponents(*runScript(session, "GetVINcomponents", vin=vin).first())


def GetYearModels(session: Session, model_id: str) -> List[str]:
    return sorted(
        [e[0] for e in runScript(session, "GetYearModels", modelId=model_id).all()]
    )


def GetValidProfilesForSelected(session: Session, profile_list: str) -> List[Row]:
    return runScript(
        session, "script_GetValidProfilesForSelected", profileList=profile_list
    ).all()
