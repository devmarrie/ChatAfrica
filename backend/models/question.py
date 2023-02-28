#!/usr/bin/python3
"""Use's questions about Africa"""
from .base_model import BaseModel
from .response import Response
from .. import db


class Question(BaseModel):
    __tablename__ = "Questions"
    query = db.Column(db.String((128)), nullable=False)
    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    chat_id = db.Column(db.String(60), db.ForeignKey('chats.id'))
    response_id = db.Column(db.String(60), db.ForeignKey('responses.id'), nullable=False)
    
    response = db.relationship("Response", back_populates="questions")
    user = db.relationship("User", back_populates="questions")
    chats = db.relationship("Chat", back_populates="questions")
