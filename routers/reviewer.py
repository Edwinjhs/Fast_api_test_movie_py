from fastapi import APIRouter,Path, Query, Depends
from fastapi.responses import  JSONResponse
from typing import  List
from fastapi.encoders import jsonable_encoder
from config.database import Session


from schemas.reviewer import Reviewer as ReviewerSchema
from service.reviewer import ReviewerService as ReviewerService


reviewer_router = APIRouter()

@reviewer_router.get('/reviewers',tags=['REVIEWERS'], response_model=ReviewerSchema, status_code= 200)
def get_reviewer() -> ReviewerSchema:   
    db = Session()
    result = ReviewerService(db).get_reviewers()
    return JSONResponse(content=jsonable_encoder(result),status_code=200)

@reviewer_router.post('/reviewers',tags=['REVIEWERS'], status_code= 201, response_model=dict)
def create_reviewer(reviewer:ReviewerSchema) -> dict:
    db = Session()
    ReviewerService(db).create_reviewer(reviewer)
    return JSONResponse(content={'message':'Reviewer save in data base'}, status_code=201)

@reviewer_router.put('/reviewers/{id}',tags=['REVIEWERS'])
def update_reviewers(id:int,reviewers:ReviewerSchema):
    db =  Session()
    result = ReviewerService(db).get_reviewers_id(id)
    if not result:
        return JSONResponse(content={"message":"No se ha encontrado ningun opinador","status_code":"404"})
    ReviewerService(db).update_reviewers(id,reviewers)
    return JSONResponse(content={"message":"Se ha modificado el opinador con id: {id}"})



@reviewer_router.delete('/reviewers/{id}',tags=['REVIEWERS'])
def delete_reviewers(id:int):
        db = Session()
        success = ReviewerService(db).delete_reviewers(id)
        if success:
            return JSONResponse(status_code=202,content={"message":"Delete reviewer"})
        else:
            return JSONResponse(content="Reviewer not found", status_code=404)
    