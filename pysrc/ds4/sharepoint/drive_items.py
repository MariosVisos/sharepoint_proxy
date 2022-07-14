from ds4.sharepoint.auth import get_account
from O365.drive import Drive


def get_drive_item(item_id: str, drive_id: str):
    """Get a drive(document_library) item by item ID"""
    account = get_account()
    if not account.is_authenticated:
        raise Exception("Not authenticated")
    site_storage = account.storage()
    drive = Drive(
        con=site_storage.con,
        protocol=site_storage.protocol,
        main_resource=site_storage.main_resource,
        **{site_storage._cloud_data_key: {"id": drive_id}},
    )
    if drive is None:
        raise Exception("Document library not found")
    result = drive.get_item(item_id)
    return result
