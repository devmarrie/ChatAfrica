import uuid
from database import db
from datetime import datetime

class BaseModel(db.Model):
    __abstract__ = True
    id = db.Column(db.String(60), primary_key=True, default=str(uuid.uuid4()))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

