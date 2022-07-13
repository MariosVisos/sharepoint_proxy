import click
from ds4.sharepoint import config
from ds4.sharepoint.sites.sites import read_site


@click.command()
@click.argument("item_id")
@click.argument("document_library_id")
@click.argument("host_name")
@click.argument("site_collection_id")
@click.argument("site_id")
def get_item(
    item_id: str,
    document_library_id: str,
    host_name: str,
    site_collection_id: str,
    site_id: str,
):
    """Get a drive(document_library) item by item ID"""
    config.init()
    click.echo("Get SharePoint document library")
    site = read_site(host_name, site_collection_id, site_id)
    if site is None:
        click.echo("Site not found")
        return
    document_library = site.get_document_library(document_library_id)
    result = document_library.get_item(item_id)
    click.echo(f"Result document library item: {result}")


@click.command()
@click.argument("folder_id")
@click.argument("document_library_id")
@click.argument("host_name")
@click.argument("site_collection_id")
@click.argument("site_id")
def get_items_in_folder(
    folder_id: str,
    document_library_id: str,
    host_name: str,
    site_collection_id: str,
    site_id: str,
):
    """Get a collection of drive(document_library) items from the folder"""
    config.init()
    click.echo("Get SharePoint document library items from the folder")
    site = read_site(host_name, site_collection_id, site_id)
    if site is None:
        click.echo("Site not found")
        return
    document_library = site.get_document_library(document_library_id)
    item = document_library.get_item(folder_id)
    if not item.is_folder:
        click.echo(f"Item is not a folder: {item}")
        return
    for drive_item in item.get_items():
        click.echo(f"Result item: {drive_item}")
        print(drive_item.object_id)
    result = list(item.get_items())
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
