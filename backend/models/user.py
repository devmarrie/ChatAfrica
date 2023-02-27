from app import db
from base_model import BaseModel


class User(BaseModel):
    __tablename__ = 'users'
    
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    chats = db.relationship('Chat', backpopulates='creator', lazy=True)
    questions = db.relationship('Question', back_populates='asker')
    responses = db.relationship('Response', back_populates='user')
    