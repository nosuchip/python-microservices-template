from typing import Union

from databases import Database
from sqlalchemy import Table

# from app.api.models import MovieIn, MovieOut, MovieUpdate
# from app.api.db import movies, database


class Repository:
    def __init__(self, database: Database, table: Table):
        self.database = database
        self.table = table

    async def create(self, payload):
        query = self.table.insert().values(**payload.dict())
        return await self.database.execute(query=query)

    async def find_one(self, id: Union[int, str]):
        query = self.table.select(self.table.c.id == id)
        return await self.database.fetch_one(query=query)

    async def find_many(self, query=None):
        query = self.table.select(**query.dict() if query else {})
        return await self.database.fetch_all(query=query)

    async def delete_one(self, id: Union[int, str]):
        query = self.table.delete().where(self.table.c.id == id)
        return await self.database.execute(query=query)

    async def delete_many(self, query):
        query = self.table.delete().where(**query.dict())
        return await self.database.execute(query=query)

    async def update(self, id: Union[int, str], payload):
        query = (
            self.table.update().where(self.table.c.id == id).values(**payload.dict())
        )
        return await self.database.execute(query=query)
