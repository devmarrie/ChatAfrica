#!/usr/bin/python3
"""Stores the response sent to users"""
from .. import db
from .base_model import BaseModel

class Response(BaseModel):
    __tablename__ = "responses"

    data = db.Column(db.String, nullable=False)
    chat_id = db.Column(db.Integer, db.ForeignKey("chats.id"))
    question_id = db.Column(db.Integer, db.ForeignKey("questions.id"))
    
