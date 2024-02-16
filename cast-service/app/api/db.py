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

casts = Table(
    'casts',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50)),
    Column('nationality', String(20)),
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
