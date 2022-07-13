import click
from ds4.sharepoint.scripts.auth import oauth
from ds4.sharepoint.scripts.document_libraries import (
    get_document_libraries,
    get_document_library,
    get_document_library_items,
)
from ds4.sharepoint.scripts.drive_items import (
    download_file,
    get_item,
    get_items_in_folder,
    upload_file,
)
from ds4.sharepoint.scripts.folders import create_folder, read_folders
from ds4.sharepoint.scripts.sites import get_all_sites, get_site, search_site

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    """CLI for SharePoint"""


# cli.add_command(create_folder)
# cli.add_command(read_folders)
cli.add_command(oauth)
cli.add_command(search_site)
cli.add_command(get_all_sites)
cli.add_command(get_site)
cli.add_command(get_document_libraries)
cli.add_command(get_document_library)
cli.add_command(get_document_library_items)
cli.add_command(get_item)
cli.add_command(get_items_in_folder)
cli.add_command(upload_file)
cli.add_command(download_file)
