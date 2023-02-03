from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base
from models.director import Director 
from models.movie import Movie

class MovdirectionDirector(Base):
    
    __tablename__= "MovieDirection_Director"
    
    id = Column(Integer,primary_key = True)
    mov_id = Column (Integer, ForeignKey("movie.id"))
    dir_id = Column (Integer, ForeignKey("director.dir_id"))
