from models.director import Director as DirectorModel

class DirectorService():
    def __init__(self,db) -> None:
        self.db = db
    
        
    
    def get_director(self) -> DirectorModel:
        result = self.db.query(DirectorModel).all()
        return result
    
    def get_director_id(self,id:int) ->DirectorModel:
        result = self.db.query(DirectorModel).filter(DirectorModel.dir_id == id).first()
        return result
    
    def create_director(self, director:DirectorModel):
        new_director = DirectorModel(
            dir_id = director.dir_id,
            dir_fname = director.dir_fname,
            dir_lname = director.dir_lname,
        )
        self.db.add(new_director)
        self.db.commit()
        return
    
    def update_director(self,id:int, data:DirectorModel):
        director = self.db.query(DirectorModel).get(id)
        if director:
            director.dir_fname = data.dir_fname
            director.dir_lname = data.dir_fname
            self.db.commit()
            return True
        return False

    def delete_director(self,id:int):
        director = self.db.query(DirectorModel).get(id)
        if director:
            self.db.delete(director)
            self.db.commit()
            return True
        return False
    