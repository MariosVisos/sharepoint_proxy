import click
from ds4.sharepoint import config
from ds4.sharepoint.sites.sites import read_site


@click.command()
@click.argument("host_name")
@click.argument("site_collection_id")
@click.argument("site_id")
def get_document_libraries(host_name: str, site_collection_id: str, site_id: str):
    """Get all SharePoint document libraries by host name, site collection ID and site ID"""
    config.init()
    click.echo("Get all SharePoint document libraries")
    site = read_site(host_name, site_collection_id, site_id)
    if site is None:
        click.echo("Site not found")
        return
    result = site.list_document_libraries()
    click.echo(f"Document libraries: {result}")


@click.command()
@click.argument("document_library_id")
@click.argument("host_name")
@click.argument("site_collection_id")
@click.argument("site_id")
def get_document_library(
    document_library_id: str, host_name: str, site_collection_id: str, site_id: str
):
    """Get SharePoint document library by host name, site collection ID and site ID"""
    config.init()
    click.echo("Get SharePoint document library")
    site = read_site(host_name, site_collection_id, site_id)
    if site is None:
        click.echo("Site not found")
        return
    result = site.get_document_library(document_library_id)
    click.echo(f"Result document library: {result}")
