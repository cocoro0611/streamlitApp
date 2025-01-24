from sqlalchemy.orm import Session
from src.database.models import User

class UserCRUD:
    # データベースセッションを保持
    def __init__(self, db: Session):
        self.db = db # インスタンスにdbを保存

    def create(self, email: str, name: str):
        user = User(email=email, name=name)
        self.db.add(user)
        self.db.commit()
        return user

    def get_all(self):
        return self.db.query(User).all()

    def update(self, user_id: int, name: str):
        user = self.db.query(User).filter(User.id == user_id).first()  # ユーザー検索
        if user:
            user.name = name
            self.db.commit()
        return user

    def delete(self, user_id: int):
        user = self.db.query(User).filter(User.id == user_id).first()  # ユーザー検索
        if user:
            self.db.delete(user)
            self.db.commit()
            return True
        return False