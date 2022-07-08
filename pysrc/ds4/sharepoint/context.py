from office365.runtime.auth.user_credential import UserCredential
from office365.sharepoint.client_context import ClientContext

# site_url = "https://planungsdienste.sharepoint.com"
site_url = "https://planungsdienste.sharepoint.com/sites/mpd"

user_name = "hansruedi.meier@planungsdienste.onmicrosoft.com"
password = "****"


def get_context():
    UserCredential(user_name, password)
    ctx = ClientContext(site_url)
    ctx.with_credentials(UserCredential(user_name, password))
    return ctx
