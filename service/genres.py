from models.genres import Genres as GenresModel
from pydantic import BaseModel, Field

class GenresService():
    def __init__(self,db) -> None:
        self.db = db

    def get_genres(self) -> GenresModel:
        result = self.db.query(GenresModel).all()
        return result
    
    def get_genres_id(self,id:int):
        result = self.db.query(GenresModel).filter(GenresModel.gen_id == id).first()
        return result
    
    def create_genre(self,genre:GenresModel):
            new_genre = GenresModel(
                gen_id = genre.gen_id,
                gen_title = genre.gen_title,    
            )
            self.db.add(new_genre)
            self.db.commit()
            return
        
    def update_genres(self,id:int, data:GenresModel):
        genres = self.db.query(GenresModel).get(id)
        if genres:
            genres.gen_title = data.gen_title
            self.db.commit()
            return True
        return False

    def delete_genres(self,id:int):
        genres = self.db.query(GenresModel).get(id)
        if genres:
            self.db.delete(genres)
            self.db.commit()
            return True
        return False
    