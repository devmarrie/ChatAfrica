#!/usr/bin/python3
"""Use's questions about Africa"""
from base_model import BaseModel
from app import db


class Question(BaseModel):
    __tablename__ = "questions"
    data = db.Column(db.String((128)), nullable=False)

    chat_id = db.Column(db.Integer, db.ForeignKey('chats.id'))
    chat = db.relationship("Chat", back_populates="questions")

    asker_id = db.relationship("User", back_populates="users.id")
    asker = db.relationship("User", back_populates="questions")

    responses = db.relationship("Response", back_populates="question")

