#!/usr/bin/python3
"""The chat class """
from sqlalchemy import Column,String
from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from base_model import BaseModel, session


class Chat(BaseModel):
    __tablename__ = "chats"
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    user= relationship("User", back_populates='chats') 
    responses = relationship("Response", back_populates='chat')  
    questions = relationship("Question", back_populates='chat') 

    def get_chat_by_id(chat_id):
        return session.query(Chat).filter_by(id=chat_id).first()