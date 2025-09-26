from flask import request, jsonify
from src.services import AlertService, NotificationService, AnalyticsService

class AdminController:
    def __init__(self):
        self.notification_service = NotificationService()
        self.alert_service = AlertService(self.notification_service)
        self.analytics_service = AnalyticsService()
    
    def create_alert(self):
        """Create a new alert"""
        try:
            data = request.get_json()
            
            # Validate required fields
            required_fields = ['title', 'message', 'visibility_type']
            for field in required_fields:
                if field not in data:
                    return jsonify({'error': f'Missing required field: {field}'}), 400
            
            # For demo, assume admin_id is 1 (in real app, get from JWT token)
            admin_id = data.get('created_by', 1)
            
            alert = self.alert_service.create_alert(data, admin_id)
            
            return jsonify({
                'message': 'Alert created successfully',
                'alert': alert.to_dict()
            }), 201
            
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def list_alerts(self):
        """List alerts created by admin"""
        try:
            # For demo, assume admin_id is 1
            admin_id = request.args.get('admin_id', 1, type=int)
            
            filters = {}
            if request.args.get('severity'):
                filters['severity'] = request.args.get('severity')
            if request.args.get('is_active'):
                filters['is_active'] = request.args.get('is_active').lower() == 'true'
            if request.args.get('visibility_type'):
                filters['visibility_type'] = request.args.get('visibility_type')
            
            alerts = self.alert_service.get_alerts_by_admin(admin_id, filters)
            
            return jsonify({
                'alerts': [alert.to_dict() for alert in alerts]
            }), 200
            
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def update_alert(self, alert_id):
        """Update an existing alert"""
        try:
            data = request.get_json()
            
            alert = self.alert_service.update_alert(alert_id, data)
            if not alert:
                return jsonify({'error': 'Alert not found'}), 404
            
            return jsonify({
                'message': 'Alert updated successfully',
                'alert': alert.to_dict()
            }), 200
            
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def archive_alert(self, alert_id):
        """Archive an alert"""
        try:
            success = self.alert_service.archive_alert(alert_id)
            if not success:
                return jsonify({'error': 'Alert not found'}), 404
            
            return jsonify({'message': 'Alert archived successfully'}), 200
            
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def get_alert_analytics(self, alert_id):
        """Get analytics for specific alert"""
        try:
            analytics = self.analytics_service.get_alert_analytics(alert_id)
            if not analytics:
                return jsonify({'error': 'Alert not found'}), 404
            
            return jsonify(analytics), 200
            
        except Exception as e:
            return jsonify({'error': str(e)}), 500
