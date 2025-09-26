from flask import Blueprint
from src.controllers import AdminController

admin_bp = Blueprint('admin', __name__, url_prefix='/api/admin')
admin_controller = AdminController()

@admin_bp.route('/alerts', methods=['POST'])
def create_alert():
    return admin_controller.create_alert()

@admin_bp.route('/alerts', methods=['GET'])
def list_alerts():
    return admin_controller.list_alerts()

@admin_bp.route('/alerts/<int:alert_id>', methods=['PUT'])
def update_alert(alert_id):
    return admin_controller.update_alert(alert_id)

@admin_bp.route('/alerts/<int:alert_id>/archive', methods=['POST'])
def archive_alert(alert_id):
    return admin_controller.archive_alert(alert_id)

@admin_bp.route('/alerts/<int:alert_id>/analytics', methods=['GET'])
def get_alert_analytics(alert_id):
    return admin_controller.get_alert_analytics(alert_id)
