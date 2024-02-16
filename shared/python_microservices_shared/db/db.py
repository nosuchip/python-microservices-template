from databases import Database
from sqlalchemy import MetaData, schema, dialects


async def create_tables(env: str, database: Database, metadata: MetaData):
    if env == "development":
        dialect = dialects.postgresql.dialect()

        await database.connect()

        for table in metadata.tables.values():
            db_schema = schema.CreateTable(table, if_not_exists=True)
            query = str(db_schema.compile(dialect=dialect))
            await database.execute(query=query)

        await database.disconnect()
