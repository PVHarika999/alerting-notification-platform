from config.database import db
from .base import BaseModel

class User(BaseModel):
    __tablename__ = 'users'
    
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=True)
    is_admin = db.Column(db.Boolean, default=False)
    
    team = db.relationship('Team', backref='members')
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'team_id': self.team_id,
            'is_admin': self.is_admin
        }
