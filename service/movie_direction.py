from models.movie_direction import MovdirectionDirector as MovieDirectionModel

class MovieDirectionService():

    def __init__(self,db) -> None:
        self.db = db

    def get_movie_direction(self):
        result = self.db.query(MovieDirectionModel).all()
        return result
    
    
    def get_movie_direction_by_dir_id(self,id_movie_direction:int):
        result = self.db.query(MovieDirectionModel).filter(MovieDirectionModel.dir_id == id_movie_direction).first()
        return result
    
    def get_movie_direction_by_mov_id(self,id_movie_direction:int):
        result = self.db.query(MovieDirectionModel).filter(MovieDirectionModel.mov_id == id_movie_direction).all()
        return result

    def create_movie_direction(self,movie_direction: MovieDirectionModel):
        new_movie_direction = MovieDirectionModel(
            dir_id = movie_direction.dir_id,
            mov_id = movie_direction.mov_id,
        )
        self.db.add(new_movie_direction)
        self.db.commit()
        return new_movie_direction
    
    def update_movie_direction(self,id:int, data:MovieDirectionModel):
        direction = self.db.query(MovieDirectionModel).get(id)
        if direction:
            direction.dir_id = data.dir_id
            direction.mov_id = data.mov_id
            self.db.commit()
            return True
        return False

    def delete_movie_direction(self,id:int):
        direction = self.db.query(MovieDirectionModel).get(id)
        if direction:
            self.db.delete(direction)
            self.db.commit()
            return True
        return False
    