from typing import Optional
from pydantic import BaseModel, Field



class MovieDirectionSchemas(BaseModel):
        dir_id: int
        mov_id: int

        class Config:
            schema_extra = {
                "example":{
                    "dir_id": 2,
                    "mov_id": 1,
                }
            }