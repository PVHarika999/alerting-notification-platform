from typing import Dict, List
from sqlalchemy import func
from config.database import db
from src.models import Alert, NotificationDelivery, UserAlertPreference

class AnalyticsService:
    def get_dashboard_metrics(self) -> Dict:
        """Get system-wide analytics metrics"""
        # Total alerts created
        total_alerts = Alert.query.count()
        
        # Active alerts
        active_alerts = Alert.query.filter_by(is_active=True).count()
        
        # Total deliveries
        total_deliveries = NotificationDelivery.query.count()
        
        # Successful deliveries
        successful_deliveries = NotificationDelivery.query.filter_by(delivery_status='sent').count()
        
        # Total reads
        total_reads = UserAlertPreference.query.filter_by(is_read=True).count()
        
        # Total snoozes
        total_snoozes = UserAlertPreference.query.filter_by(is_snoozed=True).count()
        
        # Alerts by severity
        severity_breakdown = db.session.query(
            Alert.severity,
            func.count(Alert.id)
        ).group_by(Alert.severity).all()
        
        # Delivery success rate
        delivery_rate = (successful_deliveries / total_deliveries * 100) if total_deliveries > 0 else 0
        
        # Read rate
        read_rate = (total_reads / total_deliveries * 100) if total_deliveries > 0 else 0
        
        return {
            'total_alerts': total_alerts,
            'active_alerts': active_alerts,
            'total_deliveries': total_deliveries,
            'successful_deliveries': successful_deliveries,
            'total_reads': total_reads,
            'total_snoozes': total_snoozes,
            'delivery_success_rate': round(delivery_rate, 2),
            'read_rate': round(read_rate, 2),
            'severity_breakdown': {severity: count for severity, count in severity_breakdown}
        }
    
    def get_alert_analytics(self, alert_id: int) -> Dict:
        """Get analytics for a specific alert"""
        alert = Alert.query.get(alert_id)
        if not alert:
            return {}
        
        # Delivery stats
        deliveries = NotificationDelivery.query.filter_by(alert_id=alert_id)
        total_sent = deliveries.count()
        successful_sent = deliveries.filter_by(delivery_status='sent').count()
        
        # User engagement stats
        preferences = UserAlertPreference.query.filter_by(alert_id=alert_id)
        total_reads = preferences.filter_by(is_read=True).count()
        total_snoozes = preferences.filter_by(is_snoozed=True).count()
        
        return {
            'alert_id': alert_id,
            'title': alert.title,
            'severity': alert.severity,
            'total_sent': total_sent,
            'successful_deliveries': successful_sent,
            'total_reads': total_reads,
            'total_snoozes': total_snoozes,
            'read_rate': (total_reads / total_sent * 100) if total_sent > 0 else 0,
            'snooze_rate': (total_snoozes / total_sent * 100) if total_sent > 0 else 0
        }
