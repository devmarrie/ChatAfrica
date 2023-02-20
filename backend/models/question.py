#!/usr/bin/python3
"""Use's questions about Africa"""
from sqlalchemy import Column, String
from base_model import BaseModel
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Question(BaseModel):
    __tablename__ = "Questions"
    query = Column(String((128)), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    chat_id = Column(String(60), ForeignKey('chats.id'))
    response_id = Column(String(60), ForeignKey('responses.id'), nullable=False)
    
    response = relationship("Response", back_populates="questions")
    user = relationship("User", back_populates="questions")
    chat = relationship("Chat", back_populates="questions")

