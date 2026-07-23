"""Stored procedure wrapper functions for the session VIDA database."""

__author__ = "Kestin Goforth"
__copyright__ = "Copyright 2026"
__license__ = "BSD-3-Clause"

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


def workshop_session__remove_counters(session: Session) -> list[Row]:
    return list(run_script(session, "workshopSession_RemoveCounters").all())


def workshop_session__set_intermittent_dtc_to_ok(session: Session) -> list[Row]:
    return list(run_script(session, "workshopSession_SetIntermittentDtcToOK").all())


def workshop_session__remove_freeze_frames(session: Session) -> list[Row]:
    return list(run_script(session, "workshopSession_RemoveFreezeFrames").all())


def workshop_session__update_dtc(session: Session) -> list[Row]:
    return list(run_script(session, "workshopSession_UpdateDtc").all())


def workshop_session__add_freeze_frame_parameter(session: Session) -> list[Row]:
    return list(run_script(session, "workshopSession_AddFreezeFrameParameter").all())


def workshop_session__get_freeze_frames(session: Session) -> list[Row]:
    return list(run_script(session, "workshopSession_GetFreezeFrames").all())


def workshop_session__add_fault_counter(session: Session) -> list[Row]:
    return list(run_script(session, "workshopSession_AddFaultCounter").all())


def workshop_session__add_action_item(session: Session) -> list[Row]:
    return list(run_script(session, "workshopSession_AddActionItem").all())


def workshop_session__set_dtc_show_always(session: Session) -> list[Row]:
    return list(run_script(session, "workshopSession_SetDtcShowAlways").all())


def workshop_session__remove_status_identifiers(session: Session) -> list[Row]:
    return list(run_script(session, "workshopSession_RemoveStatusIdentifiers").all())


def workshop_session__get_dtc_readouts(session: Session) -> list[Row]:
    return list(run_script(session, "workshopSession_GetDtcReadouts").all())


def workshop_session__add_dtc(session: Session) -> list[Row]:
    return list(run_script(session, "workshopSession_AddDtc").all())


def workshop_session__add_dtc_readout(session: Session) -> list[Row]:
    return list(run_script(session, "workshopSession_AddDtcReadout").all())


def workshop_session__get_fault_counters(session: Session) -> list[Row]:
    return list(run_script(session, "workshopSession_GetFaultCounters").all())


def workshop_session__get_dtcs(session: Session) -> list[Row]:
    return list(run_script(session, "workshopSession_GetDtcs").all())


def workshop_session__get_action_items(session: Session) -> list[Row]:
    return list(run_script(session, "workshopSession_GetActionItems").all())


def workshop_session__get_status_identifiers(session: Session) -> list[Row]:
    return list(run_script(session, "workshopSession_GetStatusIdentifiers").all())


def workshop_session__add_status_identifier(session: Session) -> list[Row]:
    return list(run_script(session, "workshopSession_AddStatusIdentifier").all())


def workshop_session__update_dtc_readout(session: Session) -> list[Row]:
    return list(run_script(session, "workshopSession_UpdateDtcReadout ").all())


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
