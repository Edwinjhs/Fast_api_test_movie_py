from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base
from models.reviewer import Reviewers
from models.movie import Movie

class RatingReviewers(Base):
    
    __tablename__= "rating_reviewers"
    
    id = Column(Integer,primary_key = True)
    mov_id = Column (Integer, ForeignKey("movie.id"))
    rev_id = Column (Integer, ForeignKey("reviewers.rev_id"))
    rev_stars = Column (Integer)
    num_o_ratings = Column (Integer)