import click
from ds4.sharepoint import config
from ds4.sharepoint.drive_items import (
    get_drive_item,
    get_items_from_folder,
    upload_file_to_folder,
)
from ds4.sharepoint.sites.sites import read_site


@click.command()
@click.argument("item_id")
@click.argument("drive_id")
def get_item(
    item_id: str,
    drive_id: str,
):
    """Get a drive(document_library) item by item ID"""
    config.init()
    click.echo("Get SharePoint document library")
    result = get_drive_item(item_id, drive_id)
    click.echo(f"Result document library item: {result}")


@click.command()
@click.argument("folder_id")
@click.argument("drive_id")
def get_items_in_folder(
    folder_id: str,
    drive_id: str,
):
    """Get a collection of drive(document_library) items from the folder"""
    config.init()
    click.echo("Get SharePoint document library items from the folder")
    result = get_items_from_folder(
        folder_id,
        drive_id,
    )
    click.echo(f"Result document library items: {result}")
    click.echo(f"Result items: {result}")


@click.command()
@click.argument("file")
@click.argument("folder_id")
@click.argument("document_library_id")
@click.argument("host_name")
@click.argument("site_collection_id")
@click.argument("site_id")
def upload_file(
    file: str,
    folder_id: str,
    document_library_id: str,
    host_name: str,
    site_collection_id: str,
    site_id: str,
):
    """Upload a file to a drive(document_library) folder"""
    config.init()
    click.echo("Upload a file to a drive(document_library) folder")
    site = read_site(host_name, site_collection_id, site_id)
    if site is None:
        click.echo("Site not found")
        return
    document_library = site.get_document_library(document_library_id)
    folder = document_library.get_item(folder_id)
    if not folder.is_folder:
        click.echo(f"Item is not a folder: {folder}")
        return
    click.echo(f"Uploading file: {file}")
    #  conflict_handling: How to handle conflicts.
    #  NOTE: works for chunk upload only (>4MB or upload_in_chunks is True)
    #  None to use default (overwrite). Options: fail | replace | rename
    result = folder.upload_file(file, conflict_handling="fail", upload_in_chunks=False)
    click.echo(f"Result upload: {result}")
    click.echo(f"Result upload.object_id: {result.object_id}")
    click.echo(f"Result upload.name: {result.name}")
    versions = result.get_versions()
    print("result.get_versions(): ", versions)


@click.command()
@click.argument("item_id")
@click.argument("document_library_id")
@click.argument("host_name")
@click.argument("site_collection_id")
@click.argument("site_id")
def download_file(
    item_id: str,
    document_library_id: str,
    host_name: str,
    site_collection_id: str,
    site_id: str,
):
    """Download a drive(document_library) item"""
    config.init()
    click.echo("Download a drive(document_library) item")
    site = read_site(host_name, site_collection_id, site_id)
    if site is None:
        click.echo("Site not found")
        return
    document_library = site.get_document_library(document_library_id)
    item = document_library.get_item(item_id)
    if not item.is_file:
        click.echo(f"Item is not a file: {item}")
        return
    click.echo(f"Downloading file: {item}")
    # open io object to write to
    with open("download.jpg", "wb") as f:
        # download the file to the io object
        item.download(output=f)
    click.echo(f"Downloaded file: {item}")
