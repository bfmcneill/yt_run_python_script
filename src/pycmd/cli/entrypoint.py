import click 
from pycmd.services import db_service as dbs

@click.group()
@click.option('--debug/--no-debug', default=False)
def cli(debug):
    click.echo(f"Debug mode is {'on' if debug else 'off'}")

@cli.command()  # @cli, not @click!
def sync():
    """Sync the database"""
    dbs.sync_db()


@cli.command()
def drop_db():
    """Drop the database"""
    dbs.drop_db()

if __name__ == '__main__':
    cli()