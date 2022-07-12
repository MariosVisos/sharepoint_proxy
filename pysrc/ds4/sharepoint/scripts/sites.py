import click
from ds4.sharepoint import config
from ds4.sharepoint.sites.sites import read_site, search_sites


@click.command()
@click.argument("keyword", default="")
def search_site(keyword=""):
    """Search SharePoint sites"""
    config.init()
    click.echo("Search SharePoint sites")
    result = search_sites(keyword)
    click.echo(f"Result sites: {result}")


@click.command()
def get_all_sites():
    """Get all SharePoint sites"""
    # At the moment search is used to get all sites
    config.init()
    click.echo("Get all SharePoint sites")
    result = search_sites()
    click.echo(f"Result sites; {result}")


@click.command()
@click.argument("host_name")
@click.argument("site_collection_id")
@click.argument("site_id")
def get_site(host_name: str, site_collection_id: str, site_id: str):
    """Get SharePoint site by host name, site collection ID and site ID"""
    config.init()
    click.echo("Get SharePoint site")
    result = read_site(host_name, site_collection_id, site_id)
    click.echo(f"Result site: {result}")
