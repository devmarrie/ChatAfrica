from database import db
from base_model import BaseModel


class Chat(BaseModel):    
    user_id = db.Column(db.String(60), db.ForeignKey('user.id'), nullable=False)
    responses = db.relationship('Response', backref='chat')

   