from ds4.sharepoint.auth import get_account
from O365.drive import Drive, Folder


def get_drive_item(item_id: str, drive_id: str):
    """Get a drive(document_library) item by item ID"""
    account = get_account()
    if not account.is_authenticated:
        raise Exception("Not authenticated")
    storage = account.storage()
    drive = Drive(
        con=storage.con,
        protocol=storage.protocol,
        main_resource=storage.main_resource,
        **{storage._cloud_data_key: {"id": drive_id}},
    )
    if drive is None:
        raise Exception("Document library not found")
    result = drive.get_item(item_id)
    return result


def get_items_from_folder(folder_id: str, drive_id: str):
    """Get a collection of drive(document_library) items from the folder"""
    account = get_account()
    if not account.is_authenticated:
        raise Exception("Not authenticated")
    storage = account.storage()
    drive = Drive(
        con=storage.con,
        protocol=storage.protocol,
        main_resource=storage.main_resource,
        **{storage._cloud_data_key: {"id": drive_id}},
    )
    folder = Folder(parent=drive, **{drive._cloud_data_key: {"id": folder_id}})
    items_in_folder = folder.get_items()
    for drive_item in items_in_folder:
        print(f"Result item: {drive_item}")
        print(drive_item.object_id)
    result = list(items_in_folder)
    return result


def upload_file_to_folder(file: str, folder_id: str, drive_id: str):
    """Upload a file to a folder"""
    account = get_account()
    if not account.is_authenticated:
        raise Exception("Not authenticated")
    storage = account.storage()
    drive = Drive(
        con=storage.con,
        protocol=storage.protocol,
        main_resource=storage.main_resource,
        **{storage._cloud_data_key: {"id": drive_id}},
    )
    folder = Folder(parent=drive, **{drive._cloud_data_key: {"id": folder_id}})
    #  conflict_handling: How to handle conflicts.
    #  NOTE: works for chunk upload only (>4MB or upload_in_chunks is True)
    #  None to use default (overwrite). Options: fail | replace | rename
    result = folder.upload_file(
        file, conflict_handling="replace", upload_in_chunks=False
    )
    return result
