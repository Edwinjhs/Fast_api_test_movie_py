from models.rating import RatingReviewers as RatingReviewersModel

class RatingService():

    def __init__(self,db) -> None:
        self.db = db

    def get_rating(self,id_rating:int):
        result = self.db.query(RatingReviewersModel).filter(RatingReviewersModel.rating_id == id_rating).all()
        return result

    def create_rating(self,rating: RatingReviewersModel):
        new_rating = RatingReviewersModel(
            rev_id = rating.rev_id,
            mov_id = rating.mov_id,
            rev_stars = rating.rev_stars,
            num_o_ratings = rating.num_o_ratings,
        )
        self.db.add(new_rating)
        self.db.commit()
        return
    
    def update_rating(self,id:int, data:RatingReviewersModel):
        rating = self.db.query(RatingReviewersModel).get(id)
        if rating:
            rating.gen_id = data.rev_id
            rating.mov_id = data.mov_id
            rating.rev_stars= data.rev_stars
            rating.num_o_ratings = data.num_o_ratings
            
            self.db.commit()
            return True
        return False

    def delete_rating(self,id:int):
        rating = self.db.query(RatingReviewersModel).get(id)
        if rating:
            self.db.delete(rating)
            self.db.commit()
            return True
        return False
    