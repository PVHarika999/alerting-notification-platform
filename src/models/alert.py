from datetime import datetime
from config.database import db
from .base import BaseModel

class Alert(BaseModel):
    __tablename__ = 'alerts'
    
    title = db.Column(db.String(200), nullable=False)
    message = db.Column(db.Text, nullable=False)
    severity = db.Column(db.Enum('info', 'warning', 'critical', name='severity_enum'), default='info')
    delivery_type = db.Column(db.Enum('in_app', 'email', 'sms', name='delivery_enum'), default='in_app')
    visibility_type = db.Column(db.Enum('organization', 'team', 'user', name='visibility_enum'), default='organization')
    target_audience = db.Column(db.Text)  # JSON string of IDs
    start_time = db.Column(db.DateTime, default=datetime.utcnow)
    expiry_time = db.Column(db.DateTime)
    reminder_enabled = db.Column(db.Boolean, default=True)
    reminder_frequency_hours = db.Column(db.Integer, default=2)
    is_active = db.Column(db.Boolean, default=True)
    created_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    creator = db.relationship('User', backref='created_alerts')
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'message': self.message,
            'severity': self.severity,
            'delivery_type': self.delivery_type,
            'visibility_type': self.visibility_type,
            'target_audience': self.target_audience,
            'start_time': self.start_time.isoformat() if self.start_time else None,
            'expiry_time': self.expiry_time.isoformat() if self.expiry_time else None,
            'reminder_enabled': self.reminder_enabled,
            'reminder_frequency_hours': self.reminder_frequency_hours,
            'is_active': self.is_active,
            'created_by': self.created_by,
            'created_at': self.created_at.isoformat()
        }
