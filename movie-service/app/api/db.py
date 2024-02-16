import os

from sqlalchemy import (
    Column,
    DateTime,
    Integer,
    MetaData,
    String,
    Table,
    create_engine,
    ARRAY,
    dialects,
    schema
)

from databases import Database
from app import config
from app.logger import logger

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

async def create_tables():
    if config.ENV == "development":
        logger.debug(f"==== Creating tables for environment: {config.ENV} ====")

        await database.connect()
        
        for table in metadata.tables.values():
            db_schema = schema.CreateTable(table, if_not_exists=True)
            query = str(db_schema.compile(dialect=dialect))
            await database.execute(query=query)
    
        await database.disconnect()
