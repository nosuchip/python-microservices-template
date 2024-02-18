from app import config
from databases import Database
from sqlalchemy import ARRAY, Column, Integer, MetaData, String, Table, dialects

from python_microservices_shared import Repository, create_tables  # noqa: F401

from app.api.models import MovieIn, MovieUpdate


database = Database(config.DATABASE_URI)
metadata = MetaData()
dialect = dialects.postgresql.dialect()

movies = Table(
    "movies",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("plot", String(250)),
    Column("genres", ARRAY(String)),
    Column("casts_id", ARRAY(Integer)),
)

repository = Repository[MovieIn, MovieUpdate, MovieUpdate, MovieUpdate](
    database, movies
)
