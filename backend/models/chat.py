from .. import db
from .base_model import BaseModel
from .response import Response


<<<<<<< HEAD
class Chat(BaseModel):
    __tablename__ = 'chats'

    data = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    questions = db.relationship('Question', back_populates='chats')
    responses = db.relationship('Response', back_populates='chats')
=======
class Chat(BaseModel):    
    user_id = db.Column(db.String(60), db.ForeignKey('user.id'), nullable=False)
    questions = db.relationship('Question', backref='chat')
    responses = db.relationship('Response', backref='chat')
>>>>>>> marrie
