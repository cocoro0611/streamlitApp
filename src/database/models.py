from .db import Base
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

# なぜか分割できないのでここに全てのmodelを書く必要がある
class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String, unique=True)
    name = Column(String, nullable=True)
    createdAt = Column(DateTime, default=datetime.now)

class Test(Base):
    __tablename__ = "Test"

    id2 = Column(Integer, primary_key=True, autoincrement=True)
    email2 = Column(String, unique=True)
    name2 = Column(String, nullable=True)
    createdAt2 = Column(DateTime, default=datetime.now)