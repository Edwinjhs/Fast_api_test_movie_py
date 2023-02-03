from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base
from models.genres import Genres


class MovieGenres(Base):

    __tablename__ = "movie_genres"

    id = Column(Integer,primary_key = True)
    mov_id = Column(Integer, ForeignKey("movie.id"))
    gen_id = Column(Integer, ForeignKey("genres.gen_id"))

    # movies = relationship("Movie", back_populates = "movies_casts")    
    # actors = relationship("Actor",back_populates = "movie_casts")
