
from typing import Optional
from pydantic import BaseModel, Field



class MovieGenres(BaseModel):
        gen_id: int
        mov_id: int

        class Config:
            schema_extra = {
                "example":{
                    "movie_id": 1,
                    "gen_id":1,
                }
            }