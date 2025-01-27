from sqlalchemy.orm import Session
from src.database.models import User

class UserCRAD:
    def __init__(self, db: Session):
        self.db = db

    def create(
            self, 
            name: str, 
            chest_press_weight: int, 
            lat_pulldown_weight: int, 
            leg_press_weight: int, 
            total_abdominal_weight: int, 
            rotary_torso_weight: int
            ):

        user = User(
            name=name,
            chest_press_weight=chest_press_weight,
            lat_pulldown_weight=lat_pulldown_weight,
            leg_press_weight=leg_press_weight,
            total_abdominal_weight=total_abdominal_weight,
            rotary_torso_weight=rotary_torso_weight,
        )
        self.db.add(user)
        self.db.commit()
        return user

    def get_all(self):
        return self.db.query(User).all()

    def update(
            self,
            user_id: int,
            name: str,
            chest_press_weight: int,
            lat_pulldown_weight: int,
            leg_press_weight: int,
            total_abdominal_weight: int,
            rotary_torso_weight: int
        ):
        user = self.db.query(User).filter(User.id == user_id).first() 
        if user:
            user.name = name
            user.chest_press_weight = chest_press_weight
            user.lat_pulldown_weight = lat_pulldown_weight
            user.leg_press_weight = leg_press_weight
            user.total_abdominal_weight = total_abdominal_weight
            user.rotary_torso_weight = rotary_torso_weight
            self.db.commit()
        return user

    def delete(self, user_id: int):
        user = self.db.query(User).filter(User.id == user_id).first()
        if user:
            self.db.delete(user)
            self.db.commit()
            return True
        return False