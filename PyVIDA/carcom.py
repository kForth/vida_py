from datetime import datetime

from sqlalchemy.orm import Session

from PyVIDA.util import runScript


def CleanUp(session: Session):
    return runScript(session, "CleanUp").all()


def general_GetBlockTypes(session: Session):
    return runScript(session, "general_GetBlockTypes").all()


def general_GetEcuId(session: Session, ecuIdentifier: str):
    return runScript(session, "general_GetEcuId", ecuIdentifier=ecuIdentifier).all()


def general_GetText(session: Session, textId: int):
    return runScript(session, "general_GetText", textId=textId).all()


def nevis_DeleteEcuType(session: Session, identifier: str):
    return runScript(session, "nevis_DeleteEcuType", identifier=identifier).all()


def nevis_GetEcuVariantsByProfile(session: Session, ProfileIdentifier: str):
    return runScript(
        session, "nevis_GetEcuVariantsByProfile", ProfileIdentifier=ProfileIdentifier
    ).all()


def nevis_GetLanguageId(session: Session, identifier: str, id: int):
    return runScript(session, "nevis_GetLanguageId", identifier=identifier, id=id).all()


def nevis_GetParametersByEcuVariant(session: Session, ECUVariantIdentifier: str):
    return runScript(
        session,
        "nevis_GetParametersByEcuVariant",
        ECUVariantIdentifier=ECUVariantIdentifier,
    ).all()


def nevis_GetPhrases(session: Session, lastCall: datetime):
    return runScript(session, "nevis_GetPhrases", lastCall=lastCall).all()


def nevis_GetProfileId(session: Session, profileIdentifier: str, id: int):
    return runScript(
        session, "nevis_GetProfileId", profileIdentifier=profileIdentifier, id=id
    ).all()


def nevis_GetSymptomCategories(session: Session, lastCall: datetime):
    return runScript(session, "nevis_GetSymptomCategories", lastCall=lastCall).all()


def nevis_GetSymptoms(session: Session, lastCall: datetime):
    return runScript(session, "nevis_GetSymptoms", lastCall=lastCall).all()


def nevis_GetSymptomSections(session: Session, lastCall: datetime):
    return runScript(session, "nevis_GetSymptomSections", lastCall=lastCall).all()


def nevis_GetSymptomTypes(session: Session, lastCall: datetime):
    return runScript(session, "nevis_GetSymptomTypes", lastCall=lastCall).all()


def nevis_GetTextCategoryId(session: Session, tcIdentifier: str, id: int):
    return runScript(
        session, "nevis_GetTextCategoryId", tcIdentifier=tcIdentifier, id=id
    ).all()


def nevis_ImportProfile(
    session: Session,
    identifier: str,
    value: str,
    type: str,
    note: str,
    modifiedBy: str,
    id: int,
):
    return runScript(
        session,
        "nevis_ImportProfile",
        identifier=identifier,
        value=value,
        type=type,
        note=note,
        modifiedBy=modifiedBy,
        id=id,
    ).all()


def nevis_InsertProfileParent(
    session: Session, identifier: str, parent: str, note: str, modifiedBy: str
):
    return runScript(
        session,
        "nevis_InsertProfileParent",
        identifier=identifier,
        parent=parent,
        note=note,
        modifiedBy=modifiedBy,
    ).all()


def nevis_InsertProfileValue(
    session: Session, value: str, type: str, note: str, modifiedBy: str, id: int
):
    return runScript(
        session,
        "nevis_InsertProfileValue",
        value=value,
        type=type,
        note=note,
        modifiedBy=modifiedBy,
        id=id,
    ).all()


def nevis_InsertProfileValueType(
    session: Session, description: str, note: str, modifiedBy: str, id: int
):
    return runScript(
        session,
        "nevis_InsertProfileValueType",
        description=description,
        note=note,
        modifiedBy=modifiedBy,
        id=id,
    ).all()


def nevis_RemoveParentsFromProfile(session: Session, identifier: str):
    return runScript(
        session, "nevis_RemoveParentsFromProfile", identifier=identifier
    ).all()


def nevis_RemoveValuesFromProfile(session: Session, identifier: str):
    return runScript(
        session, "nevis_RemoveValuesFromProfile", identifier=identifier
    ).all()


def nevis_UpdateEcuTypeText(
    session: Session,
    textId: int,
    text: str,
    LanguageIdentifier: str,
    modifiedBy: str,
    note: str,
):
    return runScript(
        session,
        "nevis_UpdateEcuTypeText",
        textId=textId,
        text=text,
        LanguageIdentifier=LanguageIdentifier,
        modifiedBy=modifiedBy,
        note=note,
    ).all()


def SearchCSC(session: Session, Data: str, language: str, all: int, maxcount: int):
    return runScript(
        session, "SearchCSC", Data=Data, language=language, all=all, maxcount=maxcount
    ).all()


def service_GetInitTimingValue(
    session: Session, i_fkT100_EcuVariant: int, i_service: str, i_subFunction: str
):
    return runScript(
        session,
        "service_GetInitTimingValue",
        i_fkT100_EcuVariant=i_fkT100_EcuVariant,
        i_service=i_service,
        i_subFunction=i_subFunction,
    ).all()


def service_GetInitTimingValueAll(session: Session, i_fkT100_EcuVariant: int):
    return runScript(
        session, "service_GetInitTimingValueAll", i_fkT100_EcuVariant=i_fkT100_EcuVariant
    ).all()


def service_GetParameters(session: Session, ecuId: int, parentId: int):
    return runScript(
        session, "service_GetParameters", ecuId=ecuId, parentId=parentId
    ).all()


def service_GetParameterValues(session: Session, ecuVariant: str, parameterTextId: int):
    return runScript(
        session,
        "service_GetParameterValues",
        ecuVariant=ecuVariant,
        parameterTextId=parameterTextId,
    ).all()


def service_GetService(session: Session, service: int):
    return runScript(session, "service_GetService", service=service).all()


def service__GetBlocks(session: Session, ecuIdList: str):
    return runScript(session, "service__GetBlocks", ecuIdList=ecuIdList).all()


def service__GetStructure(session: Session, ecuIdList: str):
    return runScript(session, "service__GetStructure", ecuIdList=ecuIdList).all()


def service__GetSymptoms(session: Session, ecuIdList: str):
    return runScript(session, "service__GetSymptoms", ecuIdList=ecuIdList).all()


def service__GetTexts(session: Session, ecuIdList: str, language: str):
    return runScript(
        session, "service__GetTexts", ecuIdList=ecuIdList, language=language
    ).all()


def se_browser_GetBlock(session: Session, blockId: int):
    return runScript(session, "se_browser_GetBlock", blockId=blockId).all()


def se_browser_GetBlockChildren(session: Session, ecuId: int, parentId: int):
    return runScript(
        session, "se_browser_GetBlockChildren", ecuId=ecuId, parentId=parentId
    ).all()


def se_browser_GetBlockValues(session: Session, blockId: int):
    return runScript(session, "se_browser_GetBlockValues", blockId=blockId).all()


def se_browser_GetEcus(session: Session):
    return runScript(session, "se_browser_GetEcus").all()


def se_GetBlockTypes(session: Session):
    return runScript(session, "se_GetBlockTypes").all()


def se_GetEcuAddresses(session: Session):
    return runScript(session, "se_GetEcuAddresses").all()


def se_GetEcuTypes(session: Session):
    return runScript(session, "se_GetEcuTypes").all()


def se_GetIdentifiers(session: Session, ecuType: int, blockType: int):
    return runScript(
        session, "se_GetIdentifiers", ecuType=ecuType, blockType=blockType
    ).all()


def se_GetIdentifiersByEcuAddress(session: Session, ecuAddress: str, blockType: int):
    return runScript(
        session,
        "se_GetIdentifiersByEcuAddress",
        ecuAddress=ecuAddress,
        blockType=blockType,
    ).all()


def se_GetIdentifiersByEcuType(session: Session, ecuType: int, blockType: int):
    return runScript(
        session, "se_GetIdentifiersByEcuType", ecuType=ecuType, blockType=blockType
    ).all()


def se_GetParameters(session: Session, ecuType: int, blockType: int, identifier: str):
    return runScript(
        session,
        "se_GetParameters",
        ecuType=ecuType,
        blockType=blockType,
        identifier=identifier,
    ).all()


def se_GetParametersByEcuAddress(
    session: Session, ecuAddress: str, blockType: int, identifier: str
):
    return runScript(
        session,
        "se_GetParametersByEcuAddress",
        ecuAddress=ecuAddress,
        blockType=blockType,
        identifier=identifier,
    ).all()


def se_GetParametersByEcuType(
    session: Session, ecuType: int, blockType: int, identifier: str
):
    return runScript(
        session,
        "se_GetParametersByEcuType",
        ecuType=ecuType,
        blockType=blockType,
        identifier=identifier,
    ).all()


def se_GetParameterValuesByEcuType(session: Session, ecuType: int, parameterTextId: int):
    return runScript(
        session,
        "se_GetParameterValuesByEcuType",
        ecuType=ecuType,
        parameterTextId=parameterTextId,
    ).all()


def se_GetProfileDescription(session: Session, profileIdentifier: str):
    return runScript(
        session, "se_GetProfileDescription", profileIdentifier=profileIdentifier
    ).all()


def se_GetProfiles(
    session: Session,
    folderLevel: int,
    model: int,
    year: int,
    engine: int,
    transmission: int,
    body: int,
    steering: int,
    market: int,
    unit: int,
    chassisFrom: int,
    chassisTo: int,
):
    return runScript(
        session,
        "se_GetProfiles",
        folderLevel=folderLevel,
        model=model,
        year=year,
        engine=engine,
        transmission=transmission,
        body=body,
        steering=steering,
        market=market,
        unit=unit,
        chassisFrom=chassisFrom,
        chassisTo=chassisTo,
    ).all()


def se_GetProfileValues(session: Session, type: int):
    return runScript(session, "se_GetProfileValues", type=type).all()


def se_GetProfileValueTypes(session: Session):
    return runScript(session, "se_GetProfileValueTypes").all()


def se_GetServices(session: Session):
    return runScript(session, "se_GetServices").all()


def se_GetText(session: Session, id: int, language: int):
    return runScript(session, "se_GetText", id=id, language=language).all()


def se_GetTexts(session: Session, searchCriteria: str, language: int):
    return runScript(
        session, "se_GetTexts", searchCriteria=searchCriteria, language=language
    ).all()


def se_GetTexts2(session: Session, searchCriteria: str, language: str):
    return runScript(
        session, "se_GetTexts2", searchCriteria=searchCriteria, language=language
    ).all()


def vadis_GetAllCustomerSymptoms(session: Session, languageCode: str):
    return runScript(
        session, "vadis_GetAllCustomerSymptoms", languageCode=languageCode
    ).all()


def vadis_GetAllEcuDataForProfile(session: Session, profile: str):
    return runScript(session, "vadis_GetAllEcuDataForProfile", profile=profile).all()


def vadis_GetAllowedFFForEcuVariant(session: Session, ecuVariant: int):
    return runScript(
        session, "vadis_GetAllowedFFForEcuVariant", ecuVariant=ecuVariant
    ).all()


def vadis_GetAllPossibleDtcsOnEcu(session: Session, ecuIdentifier: str):
    return runScript(
        session, "vadis_GetAllPossibleDtcsOnEcu", ecuIdentifier=ecuIdentifier
    ).all()


def vadis_GetComponent(
    session: Session,
    languageCode: str,
    symptomType: int,
    functionGroup1: int,
    functionGroup2: int,
):
    return runScript(
        session,
        "vadis_GetComponent",
        languageCode=languageCode,
        symptomType=symptomType,
        functionGroup1=functionGroup1,
        functionGroup2=functionGroup2,
    ).all()


def vadis_GetCSC(
    session: Session,
    languageCode: str,
    symptomType: int,
    functionGroup1: int,
    functionGroup2: int,
    component: int,
):
    return runScript(
        session,
        "vadis_GetCSC",
        languageCode=languageCode,
        symptomType=symptomType,
        functionGroup1=functionGroup1,
        functionGroup2=functionGroup2,
        component=component,
    ).all()


def vadis_GetCSCByID(session: Session, cscID: int, languageCode: str):
    return runScript(
        session, "vadis_GetCSCByID", cscID=cscID, languageCode=languageCode
    ).all()


def vadis_GetCustomerSymptomCode(session: Session, customerSymptomId: int):
    return runScript(
        session, "vadis_GetCustomerSymptomCode", customerSymptomId=customerSymptomId
    ).all()


def vadis_GetCustomerSymptomComment1(
    session: Session, customerSymptomId: int, languageCode: str
):
    return runScript(
        session,
        "vadis_GetCustomerSymptomComment1",
        customerSymptomId=customerSymptomId,
        languageCode=languageCode,
    ).all()


def vadis_GetCustomerSymptomComment2(
    session: Session, customerSymptomId: int, languageCode: str
):
    return runScript(
        session,
        "vadis_GetCustomerSymptomComment2",
        customerSymptomId=customerSymptomId,
        languageCode=languageCode,
    ).all()


def vadis_GetCustomerSymptomComponentName(
    session: Session, customerSymptomId: int, languageCode: str
):
    return runScript(
        session,
        "vadis_GetCustomerSymptomComponentName",
        customerSymptomId=customerSymptomId,
        languageCode=languageCode,
    ).all()


def vadis_GetCustomerSymptomDeviation(
    session: Session, customerSymptomId: int, languageCode: str
):
    return runScript(
        session,
        "vadis_GetCustomerSymptomDeviation",
        customerSymptomId=customerSymptomId,
        languageCode=languageCode,
    ).all()


def vadis_GetCustomerSymptomIdsFromDtcSymptomIds(session: Session, dtcSymptomIds: str):
    return runScript(
        session,
        "vadis_GetCustomerSymptomIdsFromDtcSymptomIds",
        dtcSymptomIds=dtcSymptomIds,
    ).all()


def vadis_GetDefaultCode(session: Session, identifier: str, vehicleProfile: str):
    return runScript(
        session,
        "vadis_GetDefaultCode",
        identifier=identifier,
        vehicleProfile=vehicleProfile,
    ).all()


def vadis_GetDefaultEcuVariants(session: Session, profileId: str):
    return runScript(session, "vadis_GetDefaultEcuVariants", profileId=profileId).all()


def vadis_GetDiagInit(session: Session, configId: int):
    return runScript(session, "vadis_GetDiagInit", configId=configId).all()


def vadis_GetDiagTimings(session: Session, configId: int):
    return runScript(session, "vadis_GetDiagTimings", configId=configId).all()


def vadis_GetDtcSymptomIdsFromCustomerSymptomId(session: Session, customerSymptomId: int):
    return runScript(
        session,
        "vadis_GetDtcSymptomIdsFromCustomerSymptomId",
        customerSymptomId=customerSymptomId,
    ).all()


def vadis_GetDtcSymptomsForEcu(session: Session, ecuId: int):
    return runScript(session, "vadis_GetDtcSymptomsForEcu", ecuId=ecuId).all()


def vadis_GetEcuInitFromConfigId(session: Session, ecuConfigId: int):
    return runScript(
        session, "vadis_GetEcuInitFromConfigId", ecuConfigId=ecuConfigId
    ).all()


def vadis_GetEcuTypeDescriptions(session: Session):
    return runScript(session, "vadis_GetEcuTypeDescriptions").all()


def vadis_GetEcuTypesAndDtcCodesForCustomerSymptomIdsAndDiagnosticNumbers(
    session: Session, customerSymptomIds: str, diagnosticNumbers: str
):
    return runScript(
        session,
        "vadis_GetEcuTypesAndDtcCodesForCustomerSymptomIdsAndDiagnosticNumbers",
        customerSymptomIds=customerSymptomIds,
        diagnosticNumbers=diagnosticNumbers,
    ).all()


def vadis_GetEcuVariantData(session: Session, ecuVariantId: int):
    return runScript(session, "vadis_GetEcuVariantData", ecuVariantId=ecuVariantId).all()


def vadis_GetEcuVariantIDsByCSCID(session: Session, cscID: int):
    return runScript(session, "vadis_GetEcuVariantIDsByCSCID", cscID=cscID).all()


def vadis_GetEcuVariantIDsBySymptomIDs(session: Session, symptomIds: str):
    return runScript(
        session, "vadis_GetEcuVariantIDsBySymptomIDs", symptomIds=symptomIds
    ).all()


def vadis_GetFunctionGroup1(session: Session, languageCode: str, symptomType: int):
    return runScript(
        session,
        "vadis_GetFunctionGroup1",
        languageCode=languageCode,
        symptomType=symptomType,
    ).all()


def vadis_GetFunctionGroup2(
    session: Session, languageCode: str, symptomType: int, functionGroup1: int
):
    return runScript(
        session,
        "vadis_GetFunctionGroup2",
        languageCode=languageCode,
        symptomType=symptomType,
        functionGroup1=functionGroup1,
    ).all()


def vadis_GetHwSettings(session: Session, vehicleProfile: str):
    return runScript(session, "vadis_GetHwSettings", vehicleProfile=vehicleProfile).all()


def vadis_GetNumberOfDtcsOnEcu(session: Session, ecuId: int):
    return runScript(session, "vadis_GetNumberOfDtcsOnEcu", ecuId=ecuId).all()


def vadis_GetParameterData(
    session: Session, ecuId: int, textId: int, languageCode: str, identifier: str
):
    return runScript(
        session,
        "vadis_GetParameterData",
        ecuId=ecuId,
        textId=textId,
        languageCode=languageCode,
        identifier=identifier,
    ).all()


def vadis_GetProtocolsForProfile(session: Session, profile: str):
    return runScript(session, "vadis_GetProtocolsForProfile", profile=profile).all()


def vadis_GetSecurityCodeFromEcuType(session: Session, ecuType: int):
    return runScript(session, "vadis_GetSecurityCodeFromEcuType", ecuType=ecuType).all()


def vadis_GetSymptom(session: Session, blockValueId: int):
    return runScript(session, "vadis_GetSymptom", blockValueId=blockValueId).all()


def vadis_GetSymptomStatusText(
    session: Session, symptomId: int, ecuVariantIdentifier: str, languageCode: str
):
    return runScript(
        session,
        "vadis_GetSymptomStatusText",
        symptomId=symptomId,
        ecuVariantIdentifier=ecuVariantIdentifier,
        languageCode=languageCode,
    ).all()


def vadis_GetSymptomType(session: Session, languageCode: str):
    return runScript(session, "vadis_GetSymptomType", languageCode=languageCode).all()


def vadis_GetText(session: Session, textId: int, languageCode: str):
    return runScript(
        session, "vadis_GetText", textId=textId, languageCode=languageCode
    ).all()
