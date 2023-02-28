<<<<<<< HEAD
#!/usr/bin/python3
"""Stores the response sent to users"""
from .. import db
from .base_model import BaseModel

class Response(BaseModel):
    __tablename__ = "responses"

    data = db.Column(db.String, nullable=False)
    chat_id = db.Column(db.Integer, db.ForeignKey("chats.id"))
=======
from app import db
from base_model import BaseModel

class Response(BaseModel):
    content = db.Column(db.Text, nullable=False)
    chat_id = db.Column(db.String(60), db.ForeignKey('chat.id'), nullable=False)

    
>>>>>>> marrie
    
    chats = db.relationship("Chat", back_populates="responses")
    questions = db.relationship("Question", back_populates="response")
