import logging
import time
import click
import sqlalchemy as sa
from rce.database.sqlalchemybase import SqlAlchemyBase
from rce import settings
from rce.secret.database_secret import DatabaseSecret
from rce import service
from rce import dt

logger = logging.getLogger(__name__)


@click.group()
def cli():
    """cli entrypoint"""


@cli.command()
def create_tables():
    dbs = DatabaseSecret.from_json_config(settings.config_json_path)
    engine = sa.create_engine(dbs.uri)
    SqlAlchemyBase.metadata.create_all(engine)


@cli.command()
@click.option("--subreddit", "-s", required=True)
@click.option("--after", "-a", default=None)
@click.option("--before", "-b", default=None)
@click.option("--tz", default="America/Denver")
def comments(subreddit, after, before, tz):
    dr = dt.date_range(after, before, tz)
    start = time.time()
    service.comments(
        subreddit=subreddit,
        after=int(dr["after"].timestamp()),
        before=int(dr["before"].timestamp()),
    )
    end = time.time()
    duration = int(end - start)
    logger.warning(f"duration: {duration} s")
    click.echo(f"duration: {duration} s")


if __name__ == "__main__":
    cli()
