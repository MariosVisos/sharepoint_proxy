"""Authenticate to SharePoint using O365 API."""

from ds4.sharepoint import config
from O365 import Account, FileSystemTokenBackend

TOKEN_PATH = "o365_token"
TOKEN_FILENAME = "token.txt"

def authenticate(app_id: str, client_secret_value: str):
    """
    Authenticate to SharePoint using O365 API and return
    the Account object if successful or None otherwise.
    """
    client_id = config.config.CLIENT_ID
    client_secret = config.config.CLIENT_SECRET
    if app_id is None and client_secret_value is None:
        if client_id is None or client_secret is None:
            raise ValueError("Missing client_id or client_secret")
        app_id = client_id
        client_secret_value = client_secret

    credentials = (app_id, client_secret_value)
    token_backend = FileSystemTokenBackend(
        token_path=TOKEN_PATH, token_filename=TOKEN_FILENAME
    )
    account = Account(credentials, token_backend=token_backend)
    if account.authenticate(scopes=["basic", "sharepoint"]):
        return account
    else:
        return None


#  scopes
# 'basic' adds: 'offline_access' and 'https://graph.microsoft.com/User.Read'
# 'sharepoint' adds: 'https://graph.microsoft.com/Sites.Read.All'
