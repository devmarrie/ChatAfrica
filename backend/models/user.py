#!/usr/bin/python3
"""User Class"""
from sqlalchemy import Column, String
from base_model import BaseModel
from sqlalchemy.orm import relationship

class User(BaseModel):
    __tablename__ = 'users'
    name = Column(String(60), nullable=False)
    email = Column(String(128), nullable=False)

    chats = relationship("Chat", back_populates="user")
    questions = relationship("Question", back_populates="user")
    
    
