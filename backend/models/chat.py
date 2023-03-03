from .. import db
from .base_model import BaseModel
from .response import Response


class Chat(BaseModel):
    __tablename__ = 'chats'

    data = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.String(60), db.ForeignKey('users.id'), nullable=False)
    
    questions = db.relationship('Question', backref='chats')
    responses = db.relationship('Response', backref='chats')
