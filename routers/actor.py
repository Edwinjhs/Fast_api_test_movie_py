from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from schemas.actor import Actor as ActorSchema
from config.database import Session
from service.actor import ActorService


actor_router = APIRouter()

@actor_router.get('/actors',tags=['ACTORS'], response_model=ActorSchema, status_code= 200)
def get_actor() ->ActorSchema:   
    db = Session()
    result = ActorService(db).get_actors()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)


@actor_router.post('/actors', tags=['ACTORS'], status_code=201 , response_model=dict)
def create_actor(actor:ActorSchema) ->dict:
    db= Session()
    ActorService(db).create_actor(actor)
    return JSONResponse(content={'message':'actor save in data base'})

@actor_router.put('/actors/{id}',tags=['ACTORS'])
def update_actor(id:int,actor:ActorSchema):
    db =  Session()
    result = ActorService(db).get_actor_id(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado ningun Actor","status_code":"404"})
    ActorService(db).update_director(id,actor)
    return JSONResponse(content={"message":"Se ha modificado el Actor con id: {id}"})



@actor_router.delete('/actors/{id}',tags=['ACTORS'])
def delete_actor(id:int):
        db = Session()
        success = ActorService(db).delete_actor(id)
        if success:
            return JSONResponse(status_code=202,content={"message":"Delete Actor"})
        else:
            return JSONResponse(content="Actor not found", status_code=404)
    