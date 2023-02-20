from app import db
from base_model import BaseModel


class Chat(BaseModel):
    __tablename__ = 'chats'
    
    maessage = db.Column(db.String(255), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    

