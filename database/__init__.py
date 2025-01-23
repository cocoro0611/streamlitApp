# database/__init__.py
from .database import SessionLocal, engine, Base
from .models import User

# テーブル作成
Base.metadata.create_all(bind=engine)