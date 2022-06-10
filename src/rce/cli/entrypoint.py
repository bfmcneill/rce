import click


@click.group()
def cli():
    """cli entrypoint"""


@cli.command()
def drop():
    click.echo("dropping")
