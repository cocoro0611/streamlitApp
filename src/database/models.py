from .db import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

class User(Base):
    __tablename__ = "User"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=True)
    chest_press_weight = Column(Integer)
    lat_pulldown_weight = Column(Integer)
    leg_press_weight = Column(Integer)
    total_abdominal_weight = Column(Integer)
    rotary_torso_weight = Column(Integer)
    created_at = Column(DateTime, default=datetime.now)

    # Userと ExerciseResultの1対多のリレーションシップを定義
    exercise_results = relationship("ExerciseResult", back_populates="user")

class ExerciseResult(Base):
    __tablename__ = "ExerciseResult"

    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("User.id"), nullable=False)
    date = Column(DateTime, nullable=False)
    running_distance = Column(Integer)
    swimming_distance = Column(Integer)
    chest_press_count = Column(Integer)
    lat_pulldown_count = Column(Integer)
    leg_press_count = Column(Integer)
    total_abdominal_count = Column(Integer)
    rotary_torso_count = Column(Integer)

    # ExerciseResultとUserの多対1のリレーションシップを定義
    user = relationship("User", back_populates="exercise_results")