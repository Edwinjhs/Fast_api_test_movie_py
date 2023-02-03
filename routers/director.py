from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder
from config.database import Session


from models.director import Director as DirectorModel
from schemas.director import Director as DirectorSchema
from service.director  import DirectorService as DirectorService


director_router = APIRouter()

@director_router.get('/director',tags=['DIRECTOR'], response_model=DirectorSchema, status_code= 200)
def get_director() -> DirectorSchema:   
    db = Session()
    result = DirectorService(db).get_director()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@director_router.post('/director',tags=['DIRECTOR'], status_code= 201, response_model=dict)
def create_director(director:DirectorSchema) -> dict:
    db = Session()
    DirectorService(db).create_director(director)
    return JSONResponse(content={'message':'Director save in data base'}, status_code=201)



@director_router.put('/director/{id}',tags=['DIRECTOR'])
def update_director(id:int,movie_director:DirectorSchema):
    db =  Session()
    result = DirectorService(db).get_director_id(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado ningun director","status_code":"404"})
    DirectorService(db).update_director(id,movie_director)
    return JSONResponse(content={"message":"Se ha modificado el director con id: {id}"})



@director_router.delete('/director/{id}',tags=['DIRECTOR'])
def delete_director(id:int):
        db = Session()
        success = DirectorService(db).delete_director(id)
        if success:
            return JSONResponse(status_code=202,content={"message":"Delete director"})
        else:
            return JSONResponse(content="Director not found", status_code=404)
    