import json
from datetime import datetime
from typing import List, Dict, Optional
from config.database import db
from src.models import Alert, User, Team

class AlertService:
    def __init__(self, notification_service=None):
        self.notification_service = notification_service
    
    def create_alert(self, alert_data: Dict, created_by: int) -> Alert:
        """Create a new alert and trigger notifications"""
        alert = Alert(
            title=alert_data['title'],
            message=alert_data['message'],
            severity=alert_data.get('severity', 'info'),
            delivery_type=alert_data.get('delivery_type', 'in_app'),
            visibility_type=alert_data['visibility_type'],
            target_audience=json.dumps(alert_data.get('target_audience', [])),
            start_time=datetime.fromisoformat(alert_data['start_time']) if alert_data.get('start_time') else datetime.utcnow(),
            expiry_time=datetime.fromisoformat(alert_data['expiry_time']) if alert_data.get('expiry_time') else None,
            reminder_enabled=alert_data.get('reminder_enabled', True),
            reminder_frequency_hours=alert_data.get('reminder_frequency_hours', 2),
            created_by=created_by
        )
        
        db.session.add(alert)
        db.session.commit()
        
        # Trigger immediate notification
        if self.notification_service:
            self.notification_service.send_notification(alert)
        
        return alert
    
    def update_alert(self, alert_id: int, updates: Dict) -> Optional[Alert]:
        """Update an existing alert"""
        alert = Alert.query.get(alert_id)
        if not alert:
            return None
        
        for key, value in updates.items():
            if hasattr(alert, key):
                if key in ['start_time', 'expiry_time'] and value:
                    value = datetime.fromisoformat(value)
                elif key == 'target_audience':
                    value = json.dumps(value)
                setattr(alert, key, value)
        
        alert.updated_at = datetime.utcnow()
        db.session.commit()
        
        return alert
    
    def get_alerts_by_admin(self, admin_id: int, filters: Dict = None) -> List[Alert]:
        """Get alerts created by admin with optional filters"""
        query = Alert.query.filter_by(created_by=admin_id)
        
        if filters:
            if filters.get('severity'):
                query = query.filter_by(severity=filters['severity'])
            if filters.get('is_active') is not None:
                query = query.filter_by(is_active=filters['is_active'])
            if filters.get('visibility_type'):
                query = query.filter_by(visibility_type=filters['visibility_type'])
        
        return query.order_by(Alert.created_at.desc()).all()
    
    def get_active_alerts(self) -> List[Alert]:
        """Get all active alerts that haven't expired"""
        now = datetime.utcnow()
        return Alert.query.filter(
            Alert.is_active == True,
            db.or_(Alert.expiry_time.is_(None), Alert.expiry_time > now)
        ).all()
    
    def archive_alert(self, alert_id: int) -> bool:
        """Archive (deactivate) an alert"""
        alert = Alert.query.get(alert_id)
        if alert:
            alert.is_active = False
            alert.updated_at = datetime.utcnow()
            db.session.commit()
            return True
        return False
