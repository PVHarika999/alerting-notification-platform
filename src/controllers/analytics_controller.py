from flask import jsonify
from src.services import AnalyticsService

class AnalyticsController:
    def __init__(self):
        self.analytics_service = AnalyticsService()
    
    def get_dashboard_metrics(self):
        """Get system-wide dashboard metrics"""
        try:
            metrics = self.analytics_service.get_dashboard_metrics()
            
            return jsonify({
                'dashboard_metrics': metrics
            }), 200
            
        except Exception as e:
            return jsonify({'error': str(e)}), 500
