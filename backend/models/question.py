#!/usr/bin/python3
"""Use's questions about Africa"""
from .base_model import BaseModel
from .response import Response
from .. import db


class Question(BaseModel):
    __tablename__ = "questions"

    data = db.Column(db.String((128)), nullable=False)
    chat_id = db.Column(db.Integer, db.ForeignKey('chats.id'))
    
    response = db.relationship("Response", backref="questions")
