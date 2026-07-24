"""Stored procedure wrapper functions for the session VIDA database."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

from datetime import datetime

from sqlalchemy import Row
from sqlalchemy.orm import Session

from vida_py.util import run_script


def clean_up(session: Session) -> list[Row]:
    return list(run_script(session, "CleanUp").all())


def so__clear_history(session: Session, user_id: str) -> list[Row]:
    return list(run_script(session, "so_ClearHistory", userId=user_id).all())


def so__create_download_confirmation(
    session: Session, vehicle_id: int, vehicle_config: bytes, vehicle_codes: bytes
) -> list[Row]:
    return list(
        run_script(
            session,
            "so_CreateDownloadConfirmation",
            vehicleId=vehicle_id,
            vehicleConfig=vehicle_config,
            vehicleCodes=vehicle_codes,
        ).all()
    )


def so__create_pending_pie_confirmation(
    session: Session, vehicle_id: int, pie_order_id: int, xml_data: bytes
) -> list[Row]:
    return list(
        run_script(
            session,
            "so_CreatePendingPieConfirmation",
            vehicleId=vehicle_id,
            pieOrderId=pie_order_id,
            xmlData=xml_data,
        ).all()
    )


def so__create_pie_download_confirmation(
    session: Session, vehicle_id: int, pie_order_id: int
) -> list[Row]:
    return list(
        run_script(
            session,
            "so_CreatePieDownloadConfirmation",
            vehicleId=vehicle_id,
            pieOrderId=pie_order_id,
        ).all()
    )


def so__create_pie_download_confirmation_error(
    session: Session, vehicle_id: int, pie_order_id: int, error_code: int
) -> list[Row]:
    return list(
        run_script(
            session,
            "so_CreatePieDownloadConfirmationError",
            vehicleId=vehicle_id,
            pieOrderId=pie_order_id,
            errorCode=error_code,
        ).all()
    )


def so__create_pie_order_attempt(session: Session, vehicle_list: str) -> list[Row]:
    return list(run_script(session, "so_CreatePieOrderAttempt", vehicleList=vehicle_list).all())


def so__create_update_order_attempt(session: Session, vehicle_id: int) -> list[Row]:
    return list(run_script(session, "so_CreateUpdateOrderAttempt", vehicleId=vehicle_id).all())


def so__create_vehicle_order(
    session: Session,
    user_id: str,
    vin: str,
    model: int,
    model_year: str,
    chassis_no: str,
    order_ref: str,
    order_id: int,
    sw_product_ids: str,
) -> list[Row]:
    return list(
        run_script(
            session,
            "so_CreateVehicleOrder",
            userId=user_id,
            vin=vin,
            model=model,
            modelYear=model_year,
            chassisNo=chassis_no,
            orderRef=order_ref,
            orderId=order_id,
            swProductIds=sw_product_ids,
        ).all()
    )


def so__delete_vehicle_order_items(
    session: Session, vehicle_id: int, sw_product_ids: str
) -> list[Row]:
    return list(
        run_script(
            session,
            "so_DeleteVehicleOrderItems",
            vehicleId=vehicle_id,
            swProductIds=sw_product_ids,
        ).all()
    )


def so__get_crypt_key(session: Session, version: int) -> list[Row]:
    return list(run_script(session, "so_GetCryptKey", version=version).all())


def so__get_crypt_key_for_vbf(session: Session, pie_order_id: int, part_number: int) -> list[Row]:
    return list(
        run_script(
            session, "so_GetCryptKeyForVbf", pieOrderId=pie_order_id, partNumber=part_number
        ).all()
    )


def so__get_crypt_key_last(session: Session) -> list[Row]:
    return list(run_script(session, "so_GetCryptKeyLast").all())


def so__get_crypt_key_version_current(session: Session) -> list[Row]:
    return list(run_script(session, "so_GetCryptKeyVersionCurrent").all())


def so__get_crypt_key_version_next(session: Session) -> list[Row]:
    return list(run_script(session, "so_GetCryptKeyVersionNext").all())


def so__get_diagnostic_scripts(session: Session, pie_order_id: int) -> list[Row]:
    return list(run_script(session, "so_GetDiagnosticScripts", pieOrderId=pie_order_id).all())


def so__get_download_package(session: Session, vehicle_id: int) -> list[Row]:
    return list(run_script(session, "so_GetDownloadPackage", vehicleId=vehicle_id).all())


def so__get_file_name(session: Session, partsid: str) -> list[Row]:
    return list(run_script(session, "so_GetFileName", partsid=partsid).all())


def so__get_gbl(session: Session, pie_order_id: int) -> list[Row]:
    return list(run_script(session, "so_GetGbl", pieOrderId=pie_order_id).all())


def so__get_history(session: Session) -> list[Row]:
    return list(run_script(session, "so_GetHistory").all())


def so__get_key_value(session: Session, key: str) -> list[Row]:
    return list(run_script(session, "so_GetKeyValue", key=key).all())


def so__get_missing_large_files_for_order(session: Session, pie_order_id: int) -> list[Row]:
    return list(
        run_script(session, "so_GetMissingLargeFilesForOrder", PieOrderId=pie_order_id).all()
    )


def so__get_pending_pie_confirmations(session: Session) -> list[Row]:
    return list(run_script(session, "so_GetPendingPieConfirmations").all())


def so__get_pie_transaction_id(session: Session, vehicle_id: int) -> list[Row]:
    return list(run_script(session, "so_GetPieTransactionId", vehicleId=vehicle_id).all())


def so__get_update_pie_order_id(session: Session, vehicle_id: int) -> list[Row]:
    return list(run_script(session, "so_GetUpdatePieOrderId", vehicleId=vehicle_id).all())


def so__get_update_pie_transaction_id(session: Session, vehicle_id: int) -> list[Row]:
    return list(run_script(session, "so_GetUpdatePieTransactionId", vehicleId=vehicle_id).all())


def so__get_vbf(session: Session, sw_part_number: int, pie_order_id: int) -> list[Row]:
    return list(
        run_script(session, "so_GetVbf", swPartNumber=sw_part_number, pieOrderId=pie_order_id).all()
    )


def so__get_vbfs(session: Session, pie_order_id: int) -> list[Row]:
    return list(run_script(session, "so_GetVbfs", pieOrderId=pie_order_id).all())


def so__get_vehicle_orders(session: Session, user_id: str) -> list[Row]:
    return list(run_script(session, "so_GetVehicleOrders", userId=user_id).all())


def so__get_vehicle_orders_for(session: Session, vehicle_list: str) -> list[Row]:
    return list(run_script(session, "so_GetVehicleOrdersFor", vehicleList=vehicle_list).all())


def so__is_installed_in_eswdl_archive(session: Session, vbf_number: int) -> list[Row]:
    return list(run_script(session, "so_IsInstalledInEswdlArchive", vbfNumber=vbf_number).all())


def so__move_to_history(
    session: Session, vehicle_id: int, final_status: str, history_item: int
) -> list[Row]:
    return list(
        run_script(
            session,
            "so_MoveToHistory",
            vehicleId=vehicle_id,
            finalStatus=final_status,
            historyItem=history_item,
        ).all()
    )


def so__remove_everything(session: Session) -> list[Row]:
    return list(run_script(session, "so_RemoveEverything").all())


def so__set_key_value(session: Session, key: str, value: str) -> list[Row]:
    return list(run_script(session, "so_SetKeyValue", key=key, value=value).all())


def so__set_pie_order_error(session: Session, pie_order_id: int, error_code: int) -> list[Row]:
    return list(
        run_script(
            session, "so_SetPieOrderError", pieOrderId=pie_order_id, errorCode=error_code
        ).all()
    )


def so__set_retrieveable(session: Session, vehicle_id: int) -> list[Row]:
    return list(run_script(session, "so_SetRetrieveable", vehicleId=vehicle_id).all())


def so__set_update_order_error(session: Session, vehicle_id: int, error_code: int) -> list[Row]:
    return list(
        run_script(
            session,
            "so_SetUpdateOrderError",
            vehicleId=vehicle_id,
            errorCode=error_code,
        ).all()
    )


def so__set_vehicle_order_error(
    session: Session, vehicle_id: int, error_code: int, error_details: str
) -> list[Row]:
    return list(
        run_script(
            session,
            "so_SetVehicleOrderError",
            vehicleId=vehicle_id,
            errorCode=error_code,
            errorDetails=error_details,
        ).all()
    )


def so__store_crypt_key(session: Session, key_data: bytes) -> list[Row]:
    return list(run_script(session, "so_StoreCryptKey", keyData=key_data).all())


def so__store_customer_param(
    session: Session, pie_order_id: int, param_name: str, param_value: str
) -> list[Row]:
    return list(
        run_script(
            session,
            "so_StoreCustomerParam",
            pieOrderId=pie_order_id,
            paramName=param_name,
            paramValue=param_value,
        ).all()
    )


def so__store_diagnostic_script(
    session: Session, pie_order_id: int, script_id: str, script_data: bytes
) -> list[Row]:
    return list(
        run_script(
            session,
            "so_StoreDiagnosticScript",
            pieOrderId=pie_order_id,
            scriptId=script_id,
            scriptData=script_data,
        ).all()
    )


def so__store_gbl(
    session: Session, pie_order_id: int, sw_part_number: int, vbf_data: bytes, veh_code: bytes
) -> list[Row]:
    return list(
        run_script(
            session,
            "so_StoreGbl",
            pieOrderId=pie_order_id,
            swPartNumber=sw_part_number,
            vbfData=vbf_data,
            vehCode=veh_code,
        ).all()
    )


def so__store_loaded_ecus(session: Session, history_item_id: int, list_of_ecus: str) -> list[Row]:
    return list(
        run_script(
            session,
            "so_StoreLoadedEcus",
            historyItemId=history_item_id,
            listOfEcus=list_of_ecus,
        ).all()
    )


def so__store_pie_order(
    session: Session, attempt_id: int, pie_order_id: int, vcp_order_number: str
) -> list[Row]:
    return list(
        run_script(
            session,
            "so_StorePieOrder",
            attemptId=attempt_id,
            pieOrderId=pie_order_id,
            vcpOrderNumber=vcp_order_number,
        ).all()
    )


def so__store_update_order(session: Session, vehicle_id: int, pie_transaction_id: int) -> list[Row]:
    return list(
        run_script(
            session,
            "so_StoreUpdateOrder",
            vehicleId=vehicle_id,
            pieTransactionId=pie_transaction_id,
        ).all()
    )


def so__store_update_package(
    session: Session,
    vehicle_id: int,
    fyon: int,
    sp_script: bytes,
    veh_config: bytes,
    veh_codes: bytes,
    verify_time: int,
    confirm_time: int,
) -> list[Row]:
    return list(
        run_script(
            session,
            "so_StoreUpdatePackage",
            vehicleId=vehicle_id,
            fyon=fyon,
            spScript=sp_script,
            vehConfig=veh_config,
            vehCodes=veh_codes,
            verifyTime=verify_time,
            confirmTime=confirm_time,
        ).all()
    )


def so__store_vbf(
    session: Session,
    pie_order_id: int,
    sw_part_number: int,
    vbf_data: bytes,
    fk_crypt_key_version: int,
) -> list[Row]:
    return list(
        run_script(
            session,
            "so_StoreVbf",
            pieOrderId=pie_order_id,
            swPartNumber=sw_part_number,
            vbfData=vbf_data,
            fkCryptKeyVersion=fk_crypt_key_version,
        ).all()
    )


def so__store_vehicle_package(
    session: Session,
    vehicle_id: int,
    vin: str,
    fyon: int,
    sp_script: bytes,
    veh_config: bytes,
    veh_codes: bytes,
    verify_time: int,
    confirm_time: int,
) -> list[Row]:
    return list(
        run_script(
            session,
            "so_StoreVehiclePackage",
            vehicleId=vehicle_id,
            vin=vin,
            fyon=fyon,
            spScript=sp_script,
            vehConfig=veh_config,
            vehCodes=veh_codes,
            verifyTime=verify_time,
            confirmTime=confirm_time,
        ).all()
    )


def so__update_order_ref(session: Session, vehicle_id: int, order_ref: str) -> list[Row]:
    return list(
        run_script(
            session,
            "so_UpdateOrderRef",
            vehicleId=vehicle_id,
            orderRef=order_ref,
        ).all()
    )


def so__update_pie_download_confirmation_lock(
    session: Session, vehicle_id: int, pie_order_id: int
) -> list[Row]:
    return list(
        run_script(
            session,
            "so_UpdatePieDownloadConfirmationLock",
            vehicleId=vehicle_id,
            pieOrderId=pie_order_id,
        ).all()
    )


def so__update_pie_order_attempt_lock(session: Session, attempt_id: int) -> list[Row]:
    return list(run_script(session, "so_UpdatePieOrderAttemptLock", attemptId=attempt_id).all())


def so__update_pie_order_lock(session: Session, pie_order_id: int) -> list[Row]:
    return list(run_script(session, "so_UpdatePieOrderLock", pieOrderId=pie_order_id).all())


def so__update_update_order_attempt_lock(session: Session, vehicle_id: int) -> list[Row]:
    return list(run_script(session, "so_UpdateUpdateOrderAttemptLock", vehicleId=vehicle_id).all())


def so__update_update_order_lock(session: Session, vehicle_id: int) -> list[Row]:
    return list(run_script(session, "so_UpdateUpdateOrderLock", vehicleId=vehicle_id).all())


def update_eswdl_file(
    session: Session, partsid: str, filename: str, status: str, checksum: str, installed: bool
) -> list[Row]:
    return list(
        run_script(
            session,
            "UpdateESWDLFile",
            partsid=partsid,
            filename=filename,
            status=status,
            checksum=checksum,
            installed=installed,
        ).all()
    )


def update_key_value(session: Session, key: str, value: str, description: str) -> list[Row]:
    return list(
        run_script(session, "UpdateKeyValue", key=key, value=value, description=description).all()
    )


def workshop_session__add_car_config_param(
    session: Session, session_id: int, param_name: str, param_value: str, type_: int
) -> list[Row]:
    return list(
        run_script(
            session,
            "workshopSession_AddCarConfigParam",
            sessionId=session_id,
            paramName=param_name,
            paramValue=param_value,
            type=type_,
        ).all()
    )


def workshop_session__add_dynamic_params(
    session: Session, session_id: int, param_name: str, param_value: str
) -> list[Row]:
    return list(
        run_script(
            session,
            "workshopSession_AddDynamicParams",
            sessionId=session_id,
            paramName=param_name,
            paramValue=param_value,
        ).all()
    )


def workshop_session__add_slave_ecu(
    session: Session,
    fk_ecu_info_id: int,
    serial_number: str,
    part_number: str,
    serial_number_name: str,
    part_number_name: str,
) -> list[Row]:
    return list(
        run_script(
            session,
            "workshopSession_AddSlaveEcu",
            fkEcuInfoId=fk_ecu_info_id,
            serialNumber=serial_number,
            partNumber=part_number,
            serialNumberName=serial_number_name,
            partNumberName=part_number_name,
        ).all()
    )


def workshop_session__add_software_number(
    session: Session, fk_ecu_info_id: int, part_number: str
) -> list[Row]:
    return list(
        run_script(
            session,
            "workshopSession_AddSoftwareNumber",
            fkEcuInfoId=fk_ecu_info_id,
            partNumber=part_number,
        ).all()
    )


def workshop_session__add_veh_config(
    session: Session,
    session_id: int,
    vin: str,
    fyon: str,
    veh_type: str,
    chassis: str,
    factory_code: str,
    structure_week: str,
) -> list[Row]:
    return list(
        run_script(
            session,
            "workshopSession_AddVehConfig",
            sessionId=session_id,
            VIN=vin,
            Fyon=fyon,
            VehType=veh_type,
            Chassis=chassis,
            FactoryCode=factory_code,
            StructureWeek=structure_week,
        ).all()
    )


def workshop_session__clean_session_data(session: Session, erase_before: datetime) -> list[Row]:
    return list(
        run_script(session, "workshopSession_CleanSessionData", eraseBefore=erase_before).all()
    )


def workshop_session__create_session(session: Session, vehicle_id: str) -> list[Row]:
    return list(run_script(session, "workshopSession_CreateSession", vehicleId=vehicle_id).all())


def workshop_session__fetch_restorable_parameters(session: Session, vin: str) -> list[Row]:
    return list(run_script(session, "workshopSession_FetchRestorableParameters", vin=vin).all())


def workshop_session__fetch_vehicle_parameters(
    session: Session, session_id: int, type_: int
) -> list[Row]:
    return list(
        run_script(
            session,
            "workshopSession_FetchVehicleParameters",
            sessionId=session_id,
            type=type_,
        ).all()
    )


def workshop_session__get_car_config_params(session: Session, session_id: int) -> list[Row]:
    return list(
        run_script(session, "workshopSession_GetCarConfigParams", sessionId=session_id).all()
    )


def workshop_session__get_diag_number(
    session: Session, session_id: int, system_code: int
) -> list[Row]:
    return list(
        run_script(
            session,
            "workshopSession_GetDiagNumber",
            sessionId=session_id,
            systemCode=system_code,
        ).all()
    )


def workshop_session__get_ecu_info(session: Session, session_id: int) -> list[Row]:
    return list(run_script(session, "workshopSession_GetEcuInfo", sessionId=session_id).all())


def workshop_session__get_ecu_slave_nodes(session: Session, fk_ecu_info_id: int) -> list[Row]:
    return list(
        run_script(session, "workshopSession_GetEcuSlaveNodes", fkEcuInfoId=fk_ecu_info_id).all()
    )


def workshop_session__get_ecu_software(session: Session, fk_ecu_info_id: int) -> list[Row]:
    return list(
        run_script(session, "workshopSession_GetEcuSoftware", fkEcuInfoId=fk_ecu_info_id).all()
    )


def workshop_session__get_observed_symptoms(session: Session, session_id: int) -> list[Row]:
    return list(
        run_script(session, "workshopSession_GetObservedSymptoms", sessionId=session_id).all()
    )


def workshop_session__get_session_id(session: Session, vin: str) -> list[Row]:
    return list(run_script(session, "workshopSession_GetSessionId", VIN=vin).all())


def workshop_session__get_session_readout_time(session: Session, session_id: int) -> list[Row]:
    return list(
        run_script(session, "workshopSession_GetSessionReadoutTime", sessionId=session_id).all()
    )


def workshop_session__get_veh_config(session: Session, session_id: int) -> list[Row]:
    return list(run_script(session, "workshopSession_GetVehConfig", sessionId=session_id).all())


def workshop_session__read_observed_symptoms(
    session: Session, session_id: int, language: str
) -> list[Row]:
    return list(
        run_script(
            session,
            "workshopSession_ReadObservedSymptoms",
            sessionId=session_id,
            language=language,
        ).all()
    )


def workshop_session__read_observed_symptoms_list_note(
    session: Session, session_id: int
) -> list[Row]:
    return list(
        run_script(
            session,
            "workshopSession_ReadObservedSymptomsListNote",
            sessionId=session_id,
        ).all()
    )


def workshop_session__remove_dtc_readout(session: Session, dtc_readout_id: int) -> list[Row]:
    return list(
        run_script(session, "workshopSession_RemoveDtcReadout", dtcReadoutId=dtc_readout_id).all()
    )


def workshop_session__remove_observed_symptoms(session: Session, session_id: int) -> list[Row]:
    return list(
        run_script(session, "workshopSession_RemoveObservedSymptoms", sessionId=session_id).all()
    )


def workshop_session__remove_software_numbers(session: Session, fk_ecu_info_id: int) -> list[Row]:
    return list(
        run_script(
            session,
            "workshopSession_RemoveSoftwareNumbers",
            fkEcuInfoId=fk_ecu_info_id,
        ).all()
    )


def workshop_session__store_dro_log_item(
    session: Session, session_id: int, ecu_address: int, request: bytes, response: bytes
) -> list[Row]:
    return list(
        run_script(
            session,
            "workshopSession_StoreDroLogItem",
            sessionId=session_id,
            ecuAddress=ecu_address,
            request=request,
            response=response,
        ).all()
    )


def workshop_session__store_ecu_info(
    session: Session,
    session_id: int,
    diag_no: str,
    part_no: str,
    serial_no: str,
    ecu_type: int,
    ecu_address: int,
    ecu_status: int,
    ecu_identifier: str,
    ecu_variant_id: str,
) -> list[Row]:
    return list(
        run_script(
            session,
            "workshopSession_StoreEcuInfo",
            sessionId=session_id,
            diagNo=diag_no,
            partNo=part_no,
            serialNo=serial_no,
            ecuType=ecu_type,
            ecuAddress=ecu_address,
            ecuStatus=ecu_status,
            ecuIdentifier=ecu_identifier,
            ecuVariantId=ecu_variant_id,
        ).all()
    )


def workshop_session__store_observed_symptom(
    session: Session, session_id: int, symptom_id: int, note: str
) -> list[Row]:
    return list(
        run_script(
            session,
            "workshopSession_StoreObservedSymptom",
            sessionId=session_id,
            symptomId=symptom_id,
            note=note,
        ).all()
    )


def workshop_session__store_observed_symptoms_list_note(
    session: Session, session_id: int, note: str
) -> list[Row]:
    return list(
        run_script(
            session,
            "workshopSession_StoreObservedSymptomsListNote",
            sessionId=session_id,
            note=note,
        ).all()
    )


def workshop_session__store_restorable_parameter(
    session: Session, session_id: int, ecu_type: int, identifier: str, response: str
) -> list[Row]:
    return list(
        run_script(
            session,
            "workshopSession_StoreRestorableParameter",
            sessionId=session_id,
            ecuType=ecu_type,
            identifier=identifier,
            response=response,
        ).all()
    )


def workshop_session__store_vehicle_parameter(
    session: Session, session_id: int, param_name: str, param_value: str, type_: int
) -> list[Row]:
    return list(
        run_script(
            session,
            "workshopSession_StoreVehicleParameter",
            sessionId=session_id,
            paramName=param_name,
            paramValue=param_value,
            type=type_,
        ).all()
    )


def workshop_session__remove_counters(session: Session, dtc_id: int) -> list[Row]:
    return list(run_script(session, "workshopSession_RemoveCounters", dtcId=dtc_id).all())


def workshop_session__set_intermittent_dtc_to_ok(session: Session, dtc_id: int) -> list[Row]:
    return list(run_script(session, "workshopSession_SetIntermittentDtcToOK", dtcID=dtc_id).all())


def workshop_session__remove_freeze_frames(session: Session, dtc_id: int) -> list[Row]:
    return list(run_script(session, "workshopSession_RemoveFreezeFrames", dtcId=dtc_id).all())


def workshop_session__update_dtc(
    session: Session,
    dtc_id: int,
    status: str,
    first_time_set: int,
    permanent: int,
    mileage_kilometres: int,
    mileage_miles: int,
    show_always: bool,
    ok_if_intermittent: bool,
    calculate_using_counters: bool,
    is_active: bool,
) -> list[Row]:
    return list(
        run_script(
            session,
            "workshopSession_UpdateDtc",
            dtcId=dtc_id,
            status=status,
            firstTimeSet=first_time_set,
            permanent=permanent,
            mileageKilometres=mileage_kilometres,
            mileageMiles=mileage_miles,
            showAlways=show_always,
            okIfIntermittent=ok_if_intermittent,
            calculateUsingCounters=calculate_using_counters,
            isActive=is_active,
        ).all()
    )


def workshop_session__add_freeze_frame_parameter(
    session: Session, dtc_id: int, name: str, value: str, id_: int, block_id: int
) -> list[Row]:
    return list(
        run_script(
            session,
            "workshopSession_AddFreezeFrameParameter",
            dtcId=dtc_id,
            name=name,
            value=value,
            id=id_,
            blockId=block_id,
        ).all()
    )


def workshop_session__get_freeze_frames(session: Session, dtc_id: int) -> list[Row]:
    return list(run_script(session, "workshopSession_GetFreezeFrames", dtcId=dtc_id).all())


def workshop_session__add_fault_counter(
    session: Session, dtc_id: int, counter_name: str, counter_value: int, counter_text_id: int
) -> list[Row]:
    return list(
        run_script(
            session,
            "workshopSession_AddFaultCounter",
            dtcId=dtc_id,
            counterName=counter_name,
            counterValue=counter_value,
            counterTextId=counter_text_id,
        ).all()
    )


def workshop_session__add_action_item(
    session: Session,
    customer_symptom_id: int,
    workshop_session_id: int,
    occurance_date: datetime,
    action: str,
    result_ok: bool,
    action_skipped: bool,
    symptom_ie_map_id: int,
    info_type: str,
    user_choice: bool,
    dtc_readout_conclusion: int,
) -> list[Row]:
    return list(
        run_script(
            session,
            "workshopSession_AddActionItem",
            customerSymptomId=customer_symptom_id,
            workshopSessionId=workshop_session_id,
            occuranceDate=occurance_date,
            action=action,
            resultOK=result_ok,
            actionSkipped=action_skipped,
            symptomIEMapId=symptom_ie_map_id,
            infoType=info_type,
            userChoice=user_choice,
            dtcReadoutConclusion=dtc_readout_conclusion,
        ).all()
    )


def workshop_session__set_dtc_show_always(session: Session, dtc_id: int) -> list[Row]:
    return list(run_script(session, "workshopSession_SetDtcShowAlways", dtcID=dtc_id).all())


def workshop_session__remove_status_identifiers(session: Session, dtc_id: int) -> list[Row]:
    return list(run_script(session, "workshopSession_RemoveStatusIdentifiers", dtcId=dtc_id).all())


def workshop_session__get_dtc_readouts(session: Session, session_id: int) -> list[Row]:
    return list(run_script(session, "workshopSession_GetDtcReadouts", sessionId=session_id).all())


def workshop_session__add_dtc(
    session: Session,
    dtc_read_out_id: int,
    ecu_type: int,
    text: str,
    hexvalue: str,
    rawvalue: str,
    status: str,
    symptom_id: int,
    first_time_set: int,
    permanent: int,
    mileage_kilometres: int,
    mileage_miles: int,
    show_always: bool,
    ok_if_intermittent: bool,
    calculate_using_counters: bool,
    is_active: bool,
) -> list[Row]:
    return list(
        run_script(
            session,
            "workshopSession_AddDtc",
            dtcReadOutId=dtc_read_out_id,
            ecuType=ecu_type,
            text=text,
            hexvalue=hexvalue,
            rawvalue=rawvalue,
            status=status,
            symptomId=symptom_id,
            firstTimeSet=first_time_set,
            permanent=permanent,
            mileageKilometres=mileage_kilometres,
            mileageMiles=mileage_miles,
            showAlways=show_always,
            okIfIntermittent=ok_if_intermittent,
            calculateUsingCounters=calculate_using_counters,
            isActive=is_active,
        ).all()
    )


def workshop_session__add_dtc_readout(
    session: Session, session_id: int, global_time: int, ecu_type: int, is_first: bool
) -> list[Row]:
    return list(
        run_script(
            session,
            "workshopSession_AddDtcReadout",
            sessionId=session_id,
            globalTime=global_time,
            ecuType=ecu_type,
            isFirst=is_first,
        ).all()
    )


def workshop_session__get_fault_counters(session: Session, dtc_id: int) -> list[Row]:
    return list(run_script(session, "workshopSession_GetFaultCounters", dtcId=dtc_id).all())


def workshop_session__get_dtcs(session: Session, dtc_readout_id: int) -> list[Row]:
    return list(run_script(session, "workshopSession_GetDtcs", dtcReadoutId=dtc_readout_id).all())


def workshop_session__get_action_items(
    session: Session, customer_symptom_id: int, workshop_session_id: int
) -> list[Row]:
    return list(
        run_script(
            session,
            "workshopSession_GetActionItems",
            customerSymptomId=customer_symptom_id,
            workshopSessionId=workshop_session_id,
        ).all()
    )


def workshop_session__get_status_identifiers(session: Session, dtc_id: int) -> list[Row]:
    return list(run_script(session, "workshopSession_GetStatusIdentifiers", dtcId=dtc_id).all())


def workshop_session__add_status_identifier(
    session: Session,
    dtc_id: int,
    status_identifier_id: int,
    status_identifier_name: str,
    status_identifier_text: str,
    status_identifier_value: int,
) -> list[Row]:
    return list(
        run_script(
            session,
            "workshopSession_AddStatusIdentifier",
            dtcId=dtc_id,
            statusIdentifierId=status_identifier_id,
            statusIdentifierName=status_identifier_name,
            statusIdentifierText=status_identifier_text,
            statusIdentifierValue=status_identifier_value,
        ).all()
    )


def workshop_session__update_dtc_readout(
    session: Session, readout_id: int, is_first: bool
) -> list[Row]:
    return list(
        run_script(
            session,
            "workshopSession_UpdateDtcReadout",
            readoutId=readout_id,
            isFirst=is_first,
        ).all()
    )


STORED_PROCEDURES = {
    "CleanUp": clean_up,
    "so_ClearHistory": so__clear_history,
    "so_CreateDownloadConfirmation": so__create_download_confirmation,
    "so_CreatePendingPieConfirmation": so__create_pending_pie_confirmation,
    "so_CreatePieDownloadConfirmation": so__create_pie_download_confirmation,
    "so_CreatePieDownloadConfirmationError": so__create_pie_download_confirmation_error,
    "so_CreatePieOrderAttempt": so__create_pie_order_attempt,
    "so_CreateUpdateOrderAttempt": so__create_update_order_attempt,
    "so_CreateVehicleOrder": so__create_vehicle_order,
    "so_DeleteVehicleOrderItems": so__delete_vehicle_order_items,
    "so_GetCryptKey": so__get_crypt_key,
    "so_GetCryptKeyForVbf": so__get_crypt_key_for_vbf,
    "so_GetCryptKeyLast": so__get_crypt_key_last,
    "so_GetCryptKeyVersionCurrent": so__get_crypt_key_version_current,
    "so_GetCryptKeyVersionNext": so__get_crypt_key_version_next,
    "so_GetDiagnosticScripts": so__get_diagnostic_scripts,
    "so_GetDownloadPackage": so__get_download_package,
    "so_GetFileName": so__get_file_name,
    "so_GetGbl": so__get_gbl,
    "so_GetHistory": so__get_history,
    "so_GetKeyValue": so__get_key_value,
    "so_GetMissingLargeFilesForOrder": so__get_missing_large_files_for_order,
    "so_GetPendingPieConfirmations": so__get_pending_pie_confirmations,
    "so_GetPieTransactionId": so__get_pie_transaction_id,
    "so_GetUpdatePieOrderId": so__get_update_pie_order_id,
    "so_GetUpdatePieTransactionId": so__get_update_pie_transaction_id,
    "so_GetVbf": so__get_vbf,
    "so_GetVbfs": so__get_vbfs,
    "so_GetVehicleOrders": so__get_vehicle_orders,
    "so_GetVehicleOrdersFor": so__get_vehicle_orders_for,
    "so_IsInstalledInEswdlArchive": so__is_installed_in_eswdl_archive,
    "so_MoveToHistory": so__move_to_history,
    "so_RemoveEverything": so__remove_everything,
    "so_SetKeyValue": so__set_key_value,
    "so_SetPieOrderError": so__set_pie_order_error,
    "so_SetRetrieveable": so__set_retrieveable,
    "so_SetUpdateOrderError": so__set_update_order_error,
    "so_SetVehicleOrderError": so__set_vehicle_order_error,
    "so_StoreCryptKey": so__store_crypt_key,
    "so_StoreCustomerParam": so__store_customer_param,
    "so_StoreDiagnosticScript": so__store_diagnostic_script,
    "so_StoreGbl": so__store_gbl,
    "so_StoreLoadedEcus": so__store_loaded_ecus,
    "so_StorePieOrder": so__store_pie_order,
    "so_StoreUpdateOrder": so__store_update_order,
    "so_StoreUpdatePackage": so__store_update_package,
    "so_StoreVbf": so__store_vbf,
    "so_StoreVehiclePackage": so__store_vehicle_package,
    "so_UpdateOrderRef": so__update_order_ref,
    "so_UpdatePieDownloadConfirmationLock": so__update_pie_download_confirmation_lock,
    "so_UpdatePieOrderAttemptLock": so__update_pie_order_attempt_lock,
    "so_UpdatePieOrderLock": so__update_pie_order_lock,
    "so_UpdateUpdateOrderAttemptLock": so__update_update_order_attempt_lock,
    "so_UpdateUpdateOrderLock": so__update_update_order_lock,
    "UpdateESWDLFile": update_eswdl_file,
    "UpdateKeyValue": update_key_value,
    "workshopSession_AddCarConfigParam": workshop_session__add_car_config_param,
    "workshopSession_AddDynamicParams": workshop_session__add_dynamic_params,
    "workshopSession_AddSlaveEcu": workshop_session__add_slave_ecu,
    "workshopSession_AddSoftwareNumber": workshop_session__add_software_number,
    "workshopSession_AddVehConfig": workshop_session__add_veh_config,
    "workshopSession_CleanSessionData": workshop_session__clean_session_data,
    "workshopSession_CreateSession": workshop_session__create_session,
    "workshopSession_FetchRestorableParameters": workshop_session__fetch_restorable_parameters,
    "workshopSession_FetchVehicleParameters": workshop_session__fetch_vehicle_parameters,
    "workshopSession_GetCarConfigParams": workshop_session__get_car_config_params,
    "workshopSession_GetDiagNumber": workshop_session__get_diag_number,
    "workshopSession_GetEcuInfo": workshop_session__get_ecu_info,
    "workshopSession_GetEcuSlaveNodes": workshop_session__get_ecu_slave_nodes,
    "workshopSession_GetEcuSoftware": workshop_session__get_ecu_software,
    "workshopSession_GetObservedSymptoms": workshop_session__get_observed_symptoms,
    "workshopSession_GetSessionId": workshop_session__get_session_id,
    "workshopSession_GetSessionReadoutTime": workshop_session__get_session_readout_time,
    "workshopSession_GetVehConfig": workshop_session__get_veh_config,
    "workshopSession_ReadObservedSymptoms": workshop_session__read_observed_symptoms,
    "workshopSession_ReadObservedSymptomsListNote": (
        workshop_session__read_observed_symptoms_list_note
    ),
    "workshopSession_RemoveDtcReadout": workshop_session__remove_dtc_readout,
    "workshopSession_RemoveObservedSymptoms": workshop_session__remove_observed_symptoms,
    "workshopSession_RemoveSoftwareNumbers": workshop_session__remove_software_numbers,
    "workshopSession_StoreDroLogItem": workshop_session__store_dro_log_item,
    "workshopSession_StoreEcuInfo": workshop_session__store_ecu_info,
    "workshopSession_StoreObservedSymptom": workshop_session__store_observed_symptom,
    "workshopSession_StoreObservedSymptomsListNote": (
        workshop_session__store_observed_symptoms_list_note
    ),
    "workshopSession_StoreRestorableParameter": workshop_session__store_restorable_parameter,
    "workshopSession_StoreVehicleParameter": workshop_session__store_vehicle_parameter,
    "workshopSession_RemoveCounters": workshop_session__remove_counters,
    "workshopSession_SetIntermittentDtcToOK": workshop_session__set_intermittent_dtc_to_ok,
    "workshopSession_RemoveFreezeFrames": workshop_session__remove_freeze_frames,
    "workshopSession_UpdateDtc": workshop_session__update_dtc,
    "workshopSession_AddFreezeFrameParameter": workshop_session__add_freeze_frame_parameter,
    "workshopSession_GetFreezeFrames": workshop_session__get_freeze_frames,
    "workshopSession_AddFaultCounter": workshop_session__add_fault_counter,
    "workshopSession_AddActionItem": workshop_session__add_action_item,
    "workshopSession_SetDtcShowAlways": workshop_session__set_dtc_show_always,
    "workshopSession_RemoveStatusIdentifiers": workshop_session__remove_status_identifiers,
    "workshopSession_GetDtcReadouts": workshop_session__get_dtc_readouts,
    "workshopSession_AddDtc": workshop_session__add_dtc,
    "workshopSession_AddDtcReadout": workshop_session__add_dtc_readout,
    "workshopSession_GetFaultCounters": workshop_session__get_fault_counters,
    "workshopSession_GetDtcs": workshop_session__get_dtcs,
    "workshopSession_GetActionItems": workshop_session__get_action_items,
    "workshopSession_GetStatusIdentifiers": workshop_session__get_status_identifiers,
    "workshopSession_AddStatusIdentifier": workshop_session__add_status_identifier,
    "workshopSession_UpdateDtcReadout": workshop_session__update_dtc_readout,
}
