#!/usr/bin/python3
"""Stores the response sent to users"""
from app import db
from base_model import BaseModel

class Response(BaseModel):
    __tablename__ = "responses"
    data = db.Column(db.String, nullable=False)

    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    question = db.relationship("Question", back_populates="responses")

    chat = db.relationship("Chat", back_populates="responses")
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    user = db.relationship('User', back_populates='responses')

