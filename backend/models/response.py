from app import db
from base_model import BaseModel

class Response(BaseModel):
    content = db.Column(db.Text, nullable=False)
    chat_id = db.Column(db.String(60), db.ForeignKey('chat.id'), nullable=False)

    
    

