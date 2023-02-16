#!/usr/bin/python3
"""User Class"""
from sqlalchemy import Column, String
from base_model import BaseModel,session
from sqlalchemy.orm import relationship

class User(BaseModel):
    __tablename__ = 'users'
    name = Column(String(60), nullable=False)
    email = Column(String(128), nullable=False)

    chats = relationship('Chat', back_populates='user')
    questions = relationship("Question", back_populates='user')
    
    def get_user_by_id(user_id):
        return session.query(User).filter_by(id=user_id).first()

