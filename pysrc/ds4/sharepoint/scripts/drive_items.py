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
