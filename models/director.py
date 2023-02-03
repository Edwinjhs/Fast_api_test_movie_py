from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from config.database import Base

class Director(Base):
    __tablename__ = 'director'
        
    dir_id= Column(Integer, primary_key = True)
    dir_fname = Column(String)
    dir_lname = Column(String)