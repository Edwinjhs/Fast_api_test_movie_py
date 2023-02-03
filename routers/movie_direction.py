from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from fastapi.security import HTTPBearer
from config.database import Session


from service.movie_direction import MovieDirectionService as DirectionService
from schemas.movie_direction import MovieDirectionSchemas as DirectionSchemas

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

movie_direction_router = APIRouter()


#@app.get('/movies',tags=['movies'],response_model=List[Movie],status_code=200, dependencies=[Depends(JWYBearer())])
@movie_direction_router.get('/movie_direction',tags=['MOVIE-DIRECTION'],response_model=List[DirectionSchemas],status_code=200)
def get_movie_direction() -> movie_direction_router:
    db = Session()
    result = DirectionService(db).get_movie_direction()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@movie_direction_router.get('/movie_direction/dir_id/',tags=['MOVIE-DIRECTION'])
def get_movie_direction_by_dir_id(id:int = Path(ge=1,le=2000)):
    db = Session()
    result = DirectionService(db).get_movie_direction_by_dir_id(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)
    
    
@movie_direction_router.get('/movies/mov_id/',tags=['MOVIE-DIRECTION'],response_model=List[DirectionSchemas],status_code=200)
def get_movie_direction_by_mov_id(id:int = Path(ge=1,le=2000)):
    db = Session()
    result = DirectionService(db).get_movie_direction_by_mov_id(id)
    if not result:
        return JSONResponse(status_code=404,content={"message":"No found"})
    return JSONResponse(content=jsonable_encoder(result), status_code=200)





@movie_direction_router.post('/movie_direction',tags=['MOVIE-DIRECTION'],status_code=201,response_model=dict)
def create_movie_direction(movie_direction:DirectionSchemas)->dict:
    db = Session()
    DirectionService(db).create_movie_direction(movie_direction)
    return JSONResponse(content={"message":"Se ha registrado el director de pelicula","status_code":201})

@movie_direction_router.put('/movie_direction/{id}',tags=['MOVIE-DIRECTION'])
def update_movie_direction(id:int,movie_direction:DirectionSchemas):
    db =  Session()
    result = DirectionService(db).get_movie_direction_by_dir_id(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado ningun director","status_code":"404"})
    DirectionService(db).update_movie_direction(id,movie_direction)
    return JSONResponse(content={"message":"Se ha modificado el director con id: {id}"})



@movie_direction_router.delete('/movie_direction/{id}',tags=['MOVIE-DIRECTION'])
def delete_movie_direction(id:int):
        db = Session()
        success = DirectionService(db).delete_movie_direction(id)
        if success:
            return JSONResponse(status_code=202,content={"message":"Delete director"})
        else:
            return JSONResponse(content="Director not found", status_code=404)
    