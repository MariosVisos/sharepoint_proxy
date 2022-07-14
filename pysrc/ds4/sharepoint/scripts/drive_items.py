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
def get_items_in_folder(folder_id: str, drive_id: str):
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
@click.argument("drive_id")
def upload_file(file: str, folder_id: str, drive_id: str):
    """Upload a file to a drive(document_library) folder"""
    config.init()
    click.echo("Upload a file to a drive(document_library) folder")
    result = upload_file_to_folder(file, folder_id, drive_id)
    click.echo(f"Result upload: {result}")
    click.echo(f"Result upload.object_id: {result.object_id}")
    click.echo(f"Result upload.name: {result.name}")
    versions = result.get_versions()
    print("result.get_versions(): ", versions)


@click.command()
@click.argument("item_id")
@click.argument("drive_id")
def download_file(item_id: str, drive_id: str):
    """Download a file"""
    config.init()
    click.echo("Download a file")
    download_file_item(item_id, drive_id)
    click.echo(f"File downloaded")
