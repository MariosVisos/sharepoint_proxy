import click
from ds4.sharepoint.scripts.folders import create_folder, read_folders

CONTEXT_SETTINGS = dict(help_option_names=["-h", "--help"])


@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass


cli.add_command(create_folder)
cli.add_command(read_folders)


@cli.command()
@click.option("-s", "--string", default="World", help="String used after hello")
@click.option("-r", "--repeat", default=1, help="How many times to repeat")
@click.argument("out", type=click.File("w"), default="-", required="false")
def say(string, repeat, out):
    """Read a string"""
    for _ in range(repeat):
        # click.echo(f"Hello {string}", file=out)
        click.echo(f"Hello {string}")
