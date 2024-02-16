from fastapi import FastAPI
from app.api.casts import casts
from app.api.db import database, create_tables, metadata
from app import config
from app.logger import logger

app = FastAPI()


@app.on_event("startup")
async def startup():
    logger.debug("==== API started, connecting to database ====")
    await create_tables(config.ENV, database, metadata)
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    logger.info("==== API stopped, disconnecting from database ====")
    await database.disconnect()


app.include_router(casts, prefix=config.API_PREFIX, tags=config.API_TAGS)
