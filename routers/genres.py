from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from models.genres import Genres as genresModel
from schemas.genres import Genres
from config.database import Session

from service.genres import GenresService


genres_router = APIRouter()

@genres_router.get('/genre',tags=['GENRES'], response_model=Genres, status_code= 200)
def get_genre() -> Genres:   
    db = Session()
    result = GenresService(db).get_genres()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@genres_router.post('/genre',tags=['GENRES'], status_code= 201, response_model=dict)
def create_genre(genres:Genres) ->dict:
    db = Session()
    GenresService(db).create_genre(genres)
    return JSONResponse(content={'message':'Genres save in data base'}, status_code=201)

@genres_router.put('/genre/{id}',tags=['GENRES'])
def update_genres(id:int,genres:genresModel):
    db =  Session()
    result = GenresService(db).get_genres_id(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado ningun genero","status_code":"404"})
    GenresService(db).update_genres(id,genres)
    return JSONResponse(content={"message":'Se ha modificado el genero con id:' + str(id)})


@genres_router.delete('/genre/{id}',tags=['GENRES'])
def delete_genres(id:int):
        db = Session()
        success = GenresService(db).delete_genres(id)
        if success:
            return JSONResponse(status_code=202,content={"message":"Delete genres"})
        else:
            return JSONResponse(content="Genres not found", status_code=404)
        
    
    