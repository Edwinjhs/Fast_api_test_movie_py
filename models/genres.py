from sqlalchemy import Column, Integer, String

from config.database import Base


class Genres(Base):

    __tablename__ = "genres"

    gen_id = Column(Integer, primary_key = True)
    gen_title= Column(String)
    
    
    
    