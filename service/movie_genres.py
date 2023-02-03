from models.movie_genre import MovieGenres as MovieGenresModel


class MovieGenresService():

    def __init__(self,db) -> None:
        self.db = db

    def get_movie_genres(self,id_movie_genres:int):
        result = self.db.query(MovieGenresModel).filter(MovieGenresModel.movie_id == id_movie_genres).all()
        return result

    def create_movie_genres(self,movie_genres: MovieGenresModel):
        new_movie_genres = MovieGenresModel(
            gen_id = movie_genres.gen_id,
            mov_id = movie_genres.movie_id,
        )
        self.db.add(new_movie_genres)
        self.db.commit()
        return
    
    def update_movie_genres(self,id:int, data:MovieGenresModel):
        movie_genres = self.db.query(MovieGenresModel).get(id)
        if movie_genres:
            movie_genres.gen_id = data.gen_id
            movie_genres.mov_id = data.mov_id
            self.db.commit()
            return True
        return False

    def delete_movie_genres(self,id:int):
        movie_genres = self.db.query(MovieGenresModel).get(id)
        if movie_genres:
            self.db.delete(movie_genres)
            self.db.commit()
            return True
        return False
    