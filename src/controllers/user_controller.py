from flask import request, jsonify
from src.services import UserService

class UserController:
    def __init__(self):
        self.user_service = UserService()
    
    def get_user_alerts(self):
        """Get alerts for a specific user"""
        try:
            user_id = request.args.get('user_id', 1, type=int)  # Default to user 1 for demo
            
            alerts = self.user_service.get_user_alerts(user_id)
            
            return jsonify({
                'user_id': user_id,
                'alerts': alerts
            }), 200
            
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def mark_alert_read(self, alert_id):
        """Mark an alert as read"""
        try:
            user_id = request.json.get('user_id', 1)  # Default to user 1 for demo
            
            success = self.user_service.mark_alert_read(user_id, alert_id)
            if not success:
                return jsonify({'error': 'Failed to mark alert as read'}), 400
            
            return jsonify({'message': 'Alert marked as read'}), 200
            
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def snooze_alert(self, alert_id):
        """Snooze an alert for the day"""
        try:
            user_id = request.json.get('user_id', 1)  # Default to user 1 for demo
            
            success = self.user_service.snooze_alert(user_id, alert_id)
            if not success:
                return jsonify({'error': 'Failed to snooze alert'}), 400
            
            return jsonify({'message': 'Alert snoozed for today'}), 200
            
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    
    def get_snoozed_alerts(self):
        """Get user's snoozed alerts history"""
        try:
            user_id = request.args.get('user_id', 1, type=int)
            
            snoozed_alerts = self.user_service.get_snoozed_alerts(user_id)
            
            return jsonify({
                'user_id': user_id,
                'snoozed_alerts': snoozed_alerts
            }), 200
            
        except Exception as e:
            return jsonify({'error': str(e)}), 500
