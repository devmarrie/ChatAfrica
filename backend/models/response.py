#!/usr/bin/python3
"""Stores the response sent to users"""
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from base_model import BaseModel

class Response(BaseModel):
    __tablename__ = "responses"
    answer = Column(String(800), nullable=False)
    chat_id = Column(String(60), ForeignKey('chats.id'))

    chat = relationship("Chat", back_populates="responses")
    questions = relationship("Question", back_populates="response")
    

