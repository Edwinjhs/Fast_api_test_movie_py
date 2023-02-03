from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder

from fastapi.security import HTTPBearer
from config.database import Session


from service.rating import RatingService as ratingService
from schemas.rating import RatingSchemas as ratingSchemas

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

rating_router = APIRouter()


#@app.get('/movies',tags=['movies'],response_model=List[Movie],status_code=200, dependencies=[Depends(JWYBearer())])
@rating_router.get('/rating',tags=['RATING'],response_model=List[ratingSchemas],status_code=200)
def get_rating() -> rating_router:
    db = Session()
    result = ratingService(db).get_rating()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)



@rating_router.post('/rating',tags=['RATING'],status_code=201,response_model=dict)
def create_rating(rating:ratingSchemas)->dict:
    db = Session()
    ratingService.create_rating(db, rating)
    return JSONResponse(content={"message":"Se ha registrado un rating","status_code":201})


@rating_router.put('/rating/{id}',tags=['RATING'])
def update_rating(id:int,rating:ratingSchemas):
    db =  Session
    result = ratingService(db).update_rating(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado ningun rating","status_code":"404"})
    ratingService(db).update_rating(id,rating)
    return JSONResponse(content={"message":"Se ha modificado el rating con id: {id}"})



@rating_router.delete('/rating/{id}',tags=['RATING'])
def delete_rating(id:int):
        db = Session()
        success = ratingService(db).delete_rating(id)
        if success:
            return JSONResponse(status_code=202,content={"message":"Delete genre"})
        else:
            return JSONResponse(content="genre not found", status_code=404)
    