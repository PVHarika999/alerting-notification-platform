from datetime import datetime, date, timedelta
from typing import List, Dict, Optional
from config.database import db
from src.models import User, Alert, UserAlertPreference, NotificationDelivery

class UserService:
    def snooze_alert(self, user_id: int, alert_id: int) -> bool:
        """Snooze an alert for the current day"""
        preference = UserAlertPreference.query.filter_by(
            user_id=user_id,
            alert_id=alert_id
        ).first()
        
        if not preference:
            preference = UserAlertPreference(
                user_id=user_id,
                alert_id=alert_id
            )
            db.session.add(preference)
        
        preference.is_snoozed = True
        preference.snoozed_until = date.today()
        db.session.commit()
        
        return True
    
    def mark_alert_read(self, user_id: int, alert_id: int) -> bool:
        """Mark an alert as read"""
        preference = UserAlertPreference.query.filter_by(
            user_id=user_id,
            alert_id=alert_id
        ).first()
        
        if not preference:
            preference = UserAlertPreference(
                user_id=user_id,
                alert_id=alert_id
            )
            db.session.add(preference)
        
        preference.is_read = True
        preference.read_at = datetime.utcnow()
        db.session.commit()
        
        return True
    
    def get_user_alerts(self, user_id: int) -> List[Dict]:
        """Get user's active alerts with their states"""
        user = User.query.get(user_id)
        if not user:
            return []
        
        # Get alerts based on user's visibility
        alerts_query = db.session.query(Alert).filter(
            Alert.is_active == True,
            db.or_(
                Alert.expiry_time.is_(None),
                Alert.expiry_time > datetime.utcnow()
            )
        )
        
        # Filter by visibility
        org_alerts = alerts_query.filter_by(visibility_type='organization')
        team_alerts = alerts_query.filter_by(visibility_type='team').filter(
            Alert.target_audience.contains(str(user.team_id)) if user.team_id else False
        )
        user_alerts = alerts_query.filter_by(visibility_type='user').filter(
            Alert.target_audience.contains(str(user_id))
        )
        
        all_alerts = org_alerts.union(team_alerts).union(user_alerts).all()
        
        result = []
        for alert in all_alerts:
            preference = UserAlertPreference.query.filter_by(
                user_id=user_id,
                alert_id=alert.id
            ).first()
            
            alert_dict = alert.to_dict()
            alert_dict['is_read'] = preference.is_read if preference else False
            alert_dict['is_snoozed'] = (preference.is_snoozed and 
                                      preference.snoozed_until >= date.today()) if preference else False
            
            result.append(alert_dict)
        
        return result
    
    def get_snoozed_alerts(self, user_id: int) -> List[Dict]:
        """Get user's snoozed alerts history"""
        preferences = UserAlertPreference.query.filter_by(
            user_id=user_id,
            is_snoozed=True
        ).all()
        
        result = []
        for pref in preferences:
            alert_dict = pref.alert.to_dict()
            alert_dict['snoozed_until'] = pref.snoozed_until.isoformat() if pref.snoozed_until else None
            result.append(alert_dict)
        
        return result
