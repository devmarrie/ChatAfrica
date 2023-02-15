#!/usr/bin/python3
"""User Class"""
from sqlalchemy import Column, String
from models.base_model import Base, BaseModel
from sqlalchemy.orm import relationship

class User(Base,BaseModel):
    __tablename__ = 'users'
    name = Column(String(60), nullable=False)
    email = Column(String(128), nullable=False)
    chats = relationship("Chat", cascade='all, delete, delete-orphan',
                         backref="user")
    questions = relationship("Question", cascade='all, delete,delete-orphan',
                             backref="user")


