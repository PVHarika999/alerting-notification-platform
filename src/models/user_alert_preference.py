from datetime import datetime, date
from config.database import db
from .base import BaseModel

class UserAlertPreference(BaseModel):
    __tablename__ = 'user_alert_preferences'
    
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    alert_id = db.Column(db.Integer, db.ForeignKey('alerts.id'), nullable=False)
    is_read = db.Column(db.Boolean, default=False)
    is_snoozed = db.Column(db.Boolean, default=False)
    snoozed_until = db.Column(db.Date)
    read_at = db.Column(db.DateTime)
    
    user = db.relationship('User', backref='alert_preferences')
    alert = db.relationship('Alert', backref='user_preferences')
    
    __table_args__ = (db.UniqueConstraint('user_id', 'alert_id'),)
    
    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'alert_id': self.alert_id,
            'is_read': self.is_read,
            'is_snoozed': self.is_snoozed,
            'snoozed_until': self.snoozed_until.isoformat() if self.snoozed_until else None,
            'read_at': self.read_at.isoformat() if self.read_at else None
        }
