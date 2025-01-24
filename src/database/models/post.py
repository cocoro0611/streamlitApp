# from .base import Base
# from sqlalchemy import Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship

# class Post(Base):
#     __tablename__ = 'posts'
#     id = Column(Integer, primary_key=True)
#     title = Column(String)
#     user_id = Column(Integer, ForeignKey('users.id'))
#     user = relationship("User", back_populates="posts")