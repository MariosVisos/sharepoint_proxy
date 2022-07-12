"""Authenticate to SharePoint using O365 API."""

from typing import Optional

from ds4.sharepoint import config
from O365 import Account, FileSystemTokenBackend

TOKEN_PATH = "o365_token"
TOKEN_FILENAME = "token.txt"

#  scopes
#  scope helpers
#  https://github.com/O365/python-o365/blob/master/O365/connection.py#L34
# 'basic' adds: 'offline_access' and 'https://graph.microsoft.com/User.Read'
# 'sharepoint' adds: 'https://graph.microsoft.com/Sites.Read.All'
# 'sharepoint_dl' adds: 'https://graph.microsoft.com/Sites.ReadWrite.All'
scopes = ["basic", "sharepoint", "sharepoint_dl"]


def build_credentials(
    app_id: Optional[str] = None, client_secret_value: Optional[str] = None
) -> tuple:
    """Build credentials for O365 API."""
    client_id = config.config.CLIENT_ID
    client_secret = config.config.CLIENT_SECRET
    if app_id is None and client_secret_value is None:
        if client_id is None or client_secret is None:
            raise ValueError("Missing client_id or client_secret")
        app_id = client_id
        client_secret_value = client_secret

    credentials = (app_id, client_secret_value)
    return credentials


def authenticate(
    app_id: Optional[str] = None, client_secret_value: Optional[str] = None
):
    """
    Authenticate to SharePoint using O365 API and return
    the Account object if successful or None otherwise.
    """
    account = get_account(app_id, client_secret_value)
    if not account.is_authenticated:
        # console-based oauth
        if not account.authenticate(scopes=scopes):
            return None

    return account


def get_account(
    app_id: Optional[str] = None, client_secret_value: Optional[str] = None
) -> Account:
    """Get the Account object for the O365 API."""
    credentials = build_credentials(app_id, client_secret_value)
    token_backend = FileSystemTokenBackend(
        token_path=TOKEN_PATH, token_filename=TOKEN_FILENAME
    )
    account = Account(credentials, token_backend=token_backend)
    return account
