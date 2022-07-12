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


def read_site(host_name: str, site_collection_id: str, site_id: str):
    """
    Get a site from SharePoint site collection
    by site name and return a site found.
    """
    account = get_account()
    if not account.is_authenticated:
        raise Exception("Not authenticated")
    if host_name is None:
        raise Exception("Host name is empty")

    site_result = account.sharepoint().get_site(host_name, site_collection_id, site_id)
    return site_result
