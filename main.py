from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field
from typing import Optional 

from fastapi.security import HTTPBearer
from config.database import engine,Base

from middlewares.error_handler import Errorhandler
from middlewares.jwt_bearer import JWYBearer
from routers.movie import movie_router
from routers.user import user_router
from routers.actor import actor_router
from routers.movie_cast import movie_cast_router
from routers.genres import genres_router
from routers.reviewer import reviewer_router
from routers.director import director_router
from routers.movie_direction import movie_direction_router
from routers.movie_genres import movie_genres_router
from routers.rating import rating_router


app = FastAPI()
app.title = "Mi app con FastAPI"
app.version = "0.0.1"

app.add_middleware(Errorhandler)
app.include_router(movie_router)
app.include_router(user_router)
app.include_router(actor_router)
app.include_router(movie_cast_router)
app.include_router(genres_router)
app.include_router(reviewer_router)
app.include_router(director_router)
app.include_router(movie_direction_router)
app.include_router(movie_genres_router)
app.include_router(rating_router)




Base.metadata.create_all(bind=engine)

@app.get('/',tags=['home'])


def message():
    return HTMLResponse('<h1>Hello World</h1>')


@app.get('/hola',tags=['home'])

def message():
    return HTMLResponse('<h1>Hello clase</h1>')
