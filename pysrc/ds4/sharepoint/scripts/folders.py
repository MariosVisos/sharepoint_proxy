import click
from ds4.sharepoint.folders.create import create_folders
from ds4.sharepoint.folders.read import get_folders


@click.command()
@click.argument("name")
def create_folder(name):
    click.echo(f"input: {name}")
    result = create_folders([name])
    click.echo(f"folder created. Result {result}")


@click.command()
def read_folders():
    click.echo(f"get_folders")
    result = get_folders()
    # click.echo(f"get_folders. Result {result}")
