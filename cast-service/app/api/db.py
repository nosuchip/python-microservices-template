from app import config
from databases import Database
from python_microservices_shared import Repository, create_tables
from sqlalchemy import Column, Integer, MetaData, String, Table, dialects

database = Database(config.DATABASE_URI)
metadata = MetaData()
dialect = dialects.postgresql.dialect()

casts = Table(
    "casts",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String(50)),
    Column("nationality", String(20)),
)

repository = Repository(database, casts)
