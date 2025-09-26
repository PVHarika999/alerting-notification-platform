from config.database import db
from .base import BaseModel

class Team(BaseModel):
    __tablename__ = 'teams'
    
    name = db.Column(db.String(100), nullable=False, unique=True)
    description = db.Column(db.Text)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description
        }
