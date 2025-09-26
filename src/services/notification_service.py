import json
from datetime import datetime
from typing import List
from config.database import db
from src.models import Alert, User, Team, NotificationDelivery, UserAlertPreference
from src.delivery.in_app_channel import InAppChannel

class NotificationService:
    def __init__(self):
        self.channels = {
            'in_app': InAppChannel()
        }
    
    def send_notification(self, alert: Alert) -> None:
        """Send notification to all relevant users"""
        target_users = self._get_target_users(alert)
        
        for user in target_users:
            # Create or update user alert preference
            preference = UserAlertPreference.query.filter_by(
                user_id=user.id,
                alert_id=alert.id
            ).first()
            
            if not preference:
                preference = UserAlertPreference(
                    user_id=user.id,
                    alert_id=alert.id
                )
                db.session.add(preference)
            
            # Send via appropriate channel
            channel = self.channels.get(alert.delivery_type)
            if channel:
                success = channel.send(alert, user)
                
                # Log delivery
                delivery = NotificationDelivery(
                    alert_id=alert.id,
                    user_id=user.id,
                    delivery_channel=alert.delivery_type,
                    delivery_status='sent' if success else 'failed',
                    delivered_at=datetime.utcnow() if success else None,
                    error_message=None if success else 'Delivery failed'
                )
                db.session.add(delivery)
        
        db.session.commit()
    
    def _get_target_users(self, alert: Alert) -> List[User]:
        """Determine target users based on visibility settings"""
        target_audience = json.loads(alert.target_audience) if alert.target_audience else []
        
        if alert.visibility_type == 'organization':
            return User.query.all()
        elif alert.visibility_type == 'team':
            if target_audience:
                return User.query.filter(User.team_id.in_(target_audience)).all()
            return []
        elif alert.visibility_type == 'user':
            if target_audience:
                return User.query.filter(User.id.in_(target_audience)).all()
            return []
        
        return []
    
    def send_reminders(self) -> None:
        """Send reminders for active alerts"""
        from datetime import date
        from src.services.alert_service import AlertService
        
        alert_service = AlertService()
        active_alerts = alert_service.get_active_alerts()
        
        for alert in active_alerts:
            if not alert.reminder_enabled:
                continue
            
            # Get users who haven't snoozed this alert today
            today = date.today()
            target_users = self._get_target_users(alert)
            
            for user in target_users:
                preference = UserAlertPreference.query.filter_by(
                    user_id=user.id,
                    alert_id=alert.id
                ).first()
                
                # Skip if snoozed for today
                if preference and preference.is_snoozed and preference.snoozed_until >= today:
                    continue
                
                # Send reminder
                channel = self.channels.get(alert.delivery_type)
                if channel:
                    success = channel.send(alert, user)
                    
                    # Log delivery
                    delivery = NotificationDelivery(
                        alert_id=alert.id,
                        user_id=user.id,
                        delivery_channel=alert.delivery_type,
                        delivery_status='sent' if success else 'failed',
                        delivered_at=datetime.utcnow() if success else None,
                        error_message=None if success else 'Reminder delivery failed'
                    )
                    db.session.add(delivery)
        
        db.session.commit()
