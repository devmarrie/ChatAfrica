from database import db
from base_model import BaseModel


class Question(BaseModel):
    que = db.Column(db.Text, nullable=False)
    res_id = db.Column(db.String(60), db.ForeignKey('response.id'))
   
    
    
