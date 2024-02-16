from fastapi import APIRouter, HTTPException

from app.api.models import CastOut, CastIn
from app.api.db import repository

from typing import List

casts = APIRouter()


@casts.post("/", response_model=CastOut, status_code=201)
async def create_cast(payload: CastIn):
    cast_id = await repository.create(payload)

    response = {"id": cast_id, **payload.dict()}

    return response


@casts.get("/{id}", response_model=CastOut)
async def get_cast(id: int):
    cast = await repository.find_one(id)

    if not cast:
        raise HTTPException(status_code=404, detail="Cast not found")
    return cast


@casts.get("/", response_model=List[CastOut])
async def get_all_casts():
    casts = await repository.find_many()

    return casts
