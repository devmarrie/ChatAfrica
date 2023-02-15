#!/usr/bin/python3
"""Stores the response sent to users"""
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import Base, BaseModel

class Response(Base, BaseModel):
    __tablename__ = "responses"
    answer = Column(String(800), nullable=False)
    chats = relationship("Chat", cascade='all, delete, delete-orphan',
                         backref="user")
    questions = relationship("Question", cascade='all, delete,delete-orphan',
                             backref="user")


