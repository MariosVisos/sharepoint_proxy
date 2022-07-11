import click
from ds4.sharepoint import config
from ds4.sharepoint.auth import authenticate
from ds4.sharepoint.scripts.folders import create_folder, read_folders
from ds4.sharepoint.scripts.sites import search_site

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass


# cli.add_command(create_folder)
# cli.add_command(read_folders)
cli.add_command(search_site)


@cli.command()
@click.option("-i", "--client_id", help="APP (Client) ID")
@click.option("-s", "--secret", help="Client secret value of the application")
def oauth(client_id, secret):
    """Authenticate to SharePoint"""
    config.init()

    account = authenticate(client_id, secret)
    if account is not None:
        print("Authenticated!")
    else:
        print("Authentication failed!")
