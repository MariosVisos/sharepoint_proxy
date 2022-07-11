import click
from ds4.sharepoint import config
from ds4.sharepoint.sites.sites import search_sites


@click.command()
@click.argument("keyword", default="")
def search_site(keyword=""):
    """Search SharePoint sites"""
    config.init()
    click.echo("Search SharePoint sites")
    result = search_sites(keyword)
    click.echo(f"get_sites. Result {result}")
