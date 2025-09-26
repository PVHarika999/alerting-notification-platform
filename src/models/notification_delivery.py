from datetime import datetime
from config.database import db
from .base import BaseModel

class NotificationDelivery(BaseModel):
    __tablename__ = 'notification_deliveries'
    
    alert_id = db.Column(db.Integer, db.ForeignKey('alerts.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    delivery_channel = db.Column(db.String(50), nullable=False)
    delivery_status = db.Column(db.Enum('sent', 'failed', 'pending', name='delivery_status_enum'), default='pending')
    delivered_at = db.Column(db.DateTime)
    error_message = db.Column(db.Text)
    
    alert = db.relationship('Alert', backref='deliveries')
    user = db.relationship('User', backref='received_notifications')
    
    def to_dict(self):
        return {
            'id': self.id,
            'alert_id': self.alert_id,
            'user_id': self.user_id,
            'delivery_channel': self.delivery_channel,
            'delivery_status': self.delivery_status,
            'delivered_at': self.delivered_at.isoformat() if self.delivered_at else None,
            'error_message': self.error_message
        }
