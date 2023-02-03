from models.actor import Actor as ActorMoldel

class ActorService():
    def __init__(self,db) -> None:
        self.db = db

    def get_actors(self) -> ActorMoldel:
        result = self.db.query(ActorMoldel).all()
        return result
    
    def get_actor_id(self,id:int) ->ActorMoldel:
        result = self.db.query(ActorMoldel).filter(ActorMoldel.act_id == id).first()
        return result

    def create_actor(self,actor:ActorMoldel):
        new_actor = ActorMoldel(
        actor_first_name = actor.actor_first_name ,
        actor_last_name = actor.actor_last_name,
        actor_gender = actor.actor_gender,    
        )
        self.db.add(new_actor)
        self.db.commit()
        return
    
    def update_actor(self,id:int, data:ActorMoldel):
        actor = self.db.query(ActorMoldel).get(id)
        if actor:
            actor.act_fname = data.act_fname
            actor.act_lname = data.act_lname
            actor.act_gender = data.act_gender

            self.db.commit()
            return True
        return False

    def delete_actor(self,id:int):
        actor = self.db.query(ActorMoldel).get(id)
        if actor:
            self.db.delete(actor)
            self.db.commit()
            return True
        return False
    