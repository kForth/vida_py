from typing import List

from sqlalchemy import Row
from sqlalchemy.orm import Session

from vida_py.scripts import runScript


def clean_up(session: Session) -> List[Row]:
    return runScript(session, "CleanUp").all()


def get_request_timeout_and_resend(
    session: Session, ecu: int, b1: int, b2: int, b3: int
) -> List[Row]:
    return runScript(
        session, "GetRequestTimeoutAndResend", ECU=ecu, B1=b1, B2=b2, B3=b3
    ).all()


def get_request_timing(
    session: Session, ecu: int, b1: int, b2: int, b3: int
) -> List[Row]:
    return runScript(session, "GetRequestTiming", ECU=ecu, B1=b1, B2=b2, B3=b3).all()


def so__clear_history(session: Session, user_id: str) -> List[Row]:
    return runScript(session, "so_ClearHistory", userId=user_id).all()


def so__create_download_confirmation(
    session: Session, vehicle_id: int, vehicle_config: bytes, vehicle_codes: bytes
) -> List[Row]:
    return runScript(
        session,
        "so_CreateDownloadConfirmation",
        vehicleId=vehicle_id,
        vehicleConfig=vehicle_config,
        vehicleCodes=vehicle_codes,
    ).all()


def so__create_pending_pie_confirmation(
    session: Session, vehicle_id: int, pie_order_id: int, xml_data: bytes
) -> List[Row]:
    return runScript(
        session,
        "so_CreatePendingPieConfirmation",
        vehicleId=vehicle_id,
        pieOrderId=pie_order_id,
        xmlData=xml_data,
    ).all()


def so__create_pie_download_confirmation(
    session: Session, vehicle_id: int, pie_order_id: int
) -> List[Row]:
    return runScript(
        session,
        "so_CreatePieDownloadConfirmation",
        vehicleId=vehicle_id,
        pieOrderId=pie_order_id,
    ).all()


def so__create_pie_download_confirmation_error(
    session: Session, vehicle_id: int, pie_order_id: int, error_code: int
) -> List[Row]:
    return runScript(
        session,
        "so_CreatePieDownloadConfirmationError",
        vehicleId=vehicle_id,
        pieOrderId=pie_order_id,
        errorCode=error_code,
    ).all()


def so__create_pie_order_attempt(session: Session, vehicle_list: str) -> List[Row]:
    return runScript(session, "so_CreatePieOrderAttempt", vehicleList=vehicle_list).all()


def so__create_update_order_attempt(session: Session, vehicle_id: int) -> List[Row]:
    return runScript(session, "so_CreateUpdateOrderAttempt", vehicleId=vehicle_id).all()


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
) -> List[Row]:
    return runScript(
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


def so__delete_vehicle_order_items(
    session: Session, vehicle_id: int, sw_product_ids: str
) -> List[Row]:
    return runScript(
        session,
        "so_DeleteVehicleOrderItems",
        vehicleId=vehicle_id,
        swProductIds=sw_product_ids,
    ).all()


def so__get_crypt_key(session: Session, version: int) -> List[Row]:
    return runScript(session, "so_GetCryptKey", version=version).all()


def so__get_crypt_key_for_vbf(
    session: Session, pie_order_id: int, part_number: int
) -> List[Row]:
    return runScript(
        session, "so_GetCryptKeyForVbf", pieOrderId=pie_order_id, partNumber=part_number
    ).all()


def so__get_crypt_key_last(session: Session) -> List[Row]:
    return runScript(session, "so_GetCryptKeyLast").all()


def so__get_crypt_key_version_current(session: Session) -> List[Row]:
    return runScript(session, "so_GetCryptKeyVersionCurrent").all()


def so__get_crypt_key_version_next(session: Session) -> List[Row]:
    return runScript(session, "so_GetCryptKeyVersionNext").all()


def so__get_diagnostic_scripts(session: Session, pie_order_id: int) -> List[Row]:
    return runScript(session, "so_GetDiagnosticScripts", pieOrderId=pie_order_id).all()


def so__get_download_package(session: Session, vehicle_id: int) -> List[Row]:
    return runScript(session, "so_GetDownloadPackage", vehicleId=vehicle_id).all()


def so__get_file_name(session: Session, partsid: str) -> List[Row]:
    return runScript(session, "so_GetFileName", partsid=partsid).all()


def so__get_gbl(session: Session, pie_order_id: int) -> List[Row]:
    return runScript(session, "so_GetGbl", pieOrderId=pie_order_id).all()


def so__get_history(session: Session) -> List[Row]:
    return runScript(session, "so_GetHistory").all()


def so__get_key_value(session: Session, key: str) -> List[Row]:
    return runScript(session, "so_GetKeyValue", key=key).all()


def so__get_missing_large_files_for_order(
    session: Session, pie_order_id: int
) -> List[Row]:
    return runScript(
        session, "so_GetMissingLargeFilesForOrder", PieOrderId=pie_order_id
    ).all()


def so__get_pending_pie_confirmations(session: Session) -> List[Row]:
    return runScript(session, "so_GetPendingPieConfirmations").all()


def so__get_pie_transaction_id(session: Session, vehicle_id: int) -> List[Row]:
    return runScript(session, "so_GetPieTransactionId", vehicleId=vehicle_id).all()


def so__get_update_pie_order_id(session: Session, vehicle_id: int) -> List[Row]:
    return runScript(session, "so_GetUpdatePieOrderId", vehicleId=vehicle_id).all()


def so__get_update_pie_transaction_id(session: Session, vehicle_id: int) -> List[Row]:
    return runScript(session, "so_GetUpdatePieTransactionId", vehicleId=vehicle_id).all()


def so__get_vbf(session: Session, sw_part_number: int, pie_order_id: int) -> List[Row]:
    return runScript(
        session, "so_GetVbf", swPartNumber=sw_part_number, pieOrderId=pie_order_id
    ).all()


def so__get_vbfs(session: Session, pie_order_id: int) -> List[Row]:
    return runScript(session, "so_GetVbfs", pieOrderId=pie_order_id).all()


def so__get_vehicle_orders(session: Session, user_id: str) -> List[Row]:
    return runScript(session, "so_GetVehicleOrders", userId=user_id).all()


def so__get_vehicle_orders_for(session: Session, vehicle_list: str) -> List[Row]:
    return runScript(session, "so_GetVehicleOrdersFor", vehicleList=vehicle_list).all()


def so__is_installed_in_eswdl_archive(session: Session, vbf_number: int) -> List[Row]:
    return runScript(session, "so_IsInstalledInEswdlArchive", vbfNumber=vbf_number).all()


def so__move_to_history(
    session: Session, vehicle_id: int, final_status: str, history_item: int
) -> List[Row]:
    return runScript(
        session,
        "so_MoveToHistory",
        vehicleId=vehicle_id,
        finalStatus=final_status,
        historyItem=history_item,
    ).all()


def so__remove_everything(session: Session) -> List[Row]:
    return runScript(session, "so_RemoveEverything").all()
