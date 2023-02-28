from app import db
from base_model import BaseModel


class User(BaseModel):
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    chats = db.relationship('Chat', backref='user')

    
    
