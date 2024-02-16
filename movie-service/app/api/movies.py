from typing import List
from fastapi import APIRouter, HTTPException

from app.api.models import MovieOut, MovieIn, MovieUpdate
from app.api.service import is_cast_present
from app.api.db import repository

movies = APIRouter()


@movies.post("/", response_model=MovieOut, status_code=201)
async def create_movie(payload: MovieIn):
    for cast_id in payload.casts_id:
        if not is_cast_present(cast_id):
            raise HTTPException(
                status_code=404, detail=f"Cast with id:{cast_id} not found"
            )

    movie_id = await repository.create(payload)
    response = {"id": movie_id, **payload.dict()}

    return response


@movies.get("/", response_model=List[MovieOut])
async def get_movies():
    return await repository.find_many()


@movies.get("/{id}", response_model=MovieOut)
async def get_movie(id: int):
    movie = await repository.find_one(id)

    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")
    return movie


@movies.put("/{id}", response_model=MovieOut)
async def update_movie(id: int, payload: MovieUpdate):
    movie = await repository.find_one(id)

    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    update_data = payload.dict(exclude_unset=True)

    if "casts_id" in update_data:
        for cast_id in payload.casts_id:
            if not is_cast_present(cast_id):
                raise HTTPException(
                    status_code=404, detail=f"Cast with given id:{cast_id} not found"
                )

    movie_in_db = MovieIn(**movie)

    updated_movie = movie_in_db.copy(update=update_data)

    return await repository.update(id, updated_movie)


@movies.delete("/{id}", response_model=None)
async def delete_movie(id: int):
    movie = await repository.find_one(id)

    if not movie:
        raise HTTPException(status_code=404, detail="Movie not found")

    return await repository.delete_one(id)
