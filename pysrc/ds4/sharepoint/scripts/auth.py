import click
from ds4.sharepoint import config
from ds4.sharepoint.auth import authenticate


@click.command()
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
