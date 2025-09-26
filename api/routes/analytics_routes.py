from flask import Blueprint
from src.controllers import AnalyticsController

analytics_bp = Blueprint('analytics', __name__, url_prefix='/api/analytics')
analytics_controller = AnalyticsController()

@analytics_bp.route('/dashboard', methods=['GET'])
def get_dashboard_metrics():
    return analytics_controller.get_dashboard_metrics()
