#!/usr/bin/python3
"""The chat class """
from sqlalchemy import Column,String
from sqlalchemy import ForeignKey
from models.base_model import Base,BaseModel


class Chat(Base, BaseModel):
    __tablename__ = "chats"
    text = Column(String(500), nullable=False)
    chat_id =Column(String(60), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    response_id = Column(String(60), ForeignKey('resposes.id'), nullable=False)
    question_id = Column(String(60), ForeignKey('questions.id'), nullable=False)