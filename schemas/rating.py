from typing import Optional
from pydantic import BaseModel, Field



class RatingSchemas(BaseModel):
        rev_id: int
        mov_id: int
        rev_stars: int
        num_o_rating: int

        class Config:
            schema_extra = {
                "example":{
                    "rev_stars": 1,
                    "num_o_rating": 2
                }
            }
