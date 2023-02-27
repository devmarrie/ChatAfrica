from app import db
from base_model import BaseModel


class Chat(BaseModel):
    __tablename__ = 'chats'
    data = db.Column(db.String(255), nullable=False)
    
    creator_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    creator = db.relationship("User", back_populates="chat")

    questions = db.relationship("Question", back_populates="chat")


