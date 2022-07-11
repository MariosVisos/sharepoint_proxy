from ds4.sharepoint.auth import get_account


def search_sites(keyword: str = " "):
    """
    Search for sites in SharePoint site collection
    by keyword and return a list of sites found.
    """
    account = get_account()
    if not account.is_authenticated:
        raise Exception("Not authenticated")
    if keyword == "":
        raise Exception("Keyword is empty")

    sites = account.sharepoint().search_site(keyword)
    return sites
