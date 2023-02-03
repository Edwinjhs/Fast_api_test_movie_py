from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from fastapi.security import HTTPBearer
from config.database import Session


from service.movie_genres import MovieGenresService as MovieGenresService
from schemas.movie_genres import MovieGenres as MovieGenresSchemas

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

movie_genres_router = APIRouter()


#@app.get('/movies',tags=['movies'],response_model=List[Movie],status_code=200, dependencies=[Depends(JWYBearer())])
@movie_genres_router.get('/movie_genres',tags=['MOVIE-GENRES'],response_model=List[MovieGenresSchemas],status_code=200)
def get_movie_genres() -> movie_genres_router:
    db = Session()
    result = MovieGenresService(db).get_movie_genres()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)



@movie_genres_router.post('/movie_genres',tags=['MOVIE-GENRES'],status_code=201,response_model=dict)
def create_movie_genres(movie_genres:MovieGenresSchemas)->dict:
    db = Session(db)
    MovieGenresService.create_movie_genres(db, movie_genres)
    return JSONResponse(content={"message":"Se ha registrado el genero de pelicula","status_code":201})



@movie_genres_router.put('/movie_genres/{id}',tags=['MOVIE-GENRES'])
def update_movie_genres(id:int,movie_genres:MovieGenresSchemas):
    db =  Session
    result = MovieGenresService(db).update_movie_genres(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado ningun genero","status_code":"404"})
    MovieGenresService(db).update_movie_direction(id,movie_genres)
    return JSONResponse(content={"message":"Se ha modificado el genero con id: {id}"})



@movie_genres_router.delete('/movie_genres/{id}',tags=['MOVIE-GENRES'])
def delete_movie_genres(id:int):
        db = Session()
        success = MovieGenresService(db).delete_movie_genres(id)
        if success:
            return JSONResponse(status_code=202,content={"message":"Delete genre"})
        else:
            return JSONResponse(content="genre not found", status_code=404)
    