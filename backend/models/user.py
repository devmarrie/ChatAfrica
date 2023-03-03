from .. import db
from .base_model import BaseModel
from .question import Question
from flask_login import UserMixin


class User(BaseModel, UserMixin):
    __tablename__ = 'users'
    
    # id = db.Column(db.Integer, primary_key=True)
    google_id = db.Column(db.Integer, unique=True, nullable=False)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    avatar_url = db.Column(db.String(250), nullable=False)


    chats = db.relationship('Chat', backref='users', lazy=True)
