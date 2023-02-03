from models.reviewer import Reviewers as ReviewersModel 


class ReviewerService():
    def __init__(self,db) -> None:
        self.db = db
        
    def get_reviewers(self) -> ReviewersModel:
        result = self.db.query(ReviewersModel).all()
        return result
    
    def get_reviewers_id(self,id:int) ->ReviewersModel:
        result = self.db.query(ReviewersModel).filter(ReviewersModel.rev_id == id).first()
        return result
    
    def create_reviewer(self, reviewer:ReviewersModel):
        new_reviewer = ReviewersModel(
            rev_id = reviewer.rev_id,
            rev_name = reviewer.rev_name,
        )
        self.db.add(new_reviewer)
        self.db.commit()
        return
    
    def update_reviewers(self,id:int, data:ReviewersModel):
        reviewers = self.db.query(ReviewersModel).get(id)
        if reviewers:
            reviewers.rev_name = data.rev_name
            self.db.commit()
            return True
        return False

    def delete_reviewers(self,id:int):
        reviewers = self.db.query(ReviewersModel).get(id)
        if reviewers:
            self.db.delete(reviewers)
            self.db.commit()
            return True
        return False
    