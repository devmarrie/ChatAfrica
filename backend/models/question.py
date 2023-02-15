#!/usr/bin/python3
"""Use's questions about Africa"""
from sqlalchemy import Column,String
from models.base_model import Base,BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Question(Base, BaseModel):
    __tablename__ = "Questions"
    query = Column(String((128)), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    response_id = Column(String(60), ForeignKey('resposes.id'), nullable=False)
    chats = relationship("Chat", cascade='all, delete, delete-orphan',
                          backref="user")

