from flask import Blueprint
from src.controllers import UserController

user_bp = Blueprint('user', __name__, url_prefix='/api/user')
user_controller = UserController()

@user_bp.route('/alerts', methods=['GET'])
def get_user_alerts():
    return user_controller.get_user_alerts()

@user_bp.route('/alerts/<int:alert_id>/read', methods=['POST'])
def mark_alert_read(alert_id):
    return user_controller.mark_alert_read(alert_id)

@user_bp.route('/alerts/<int:alert_id>/snooze', methods=['POST'])
def snooze_alert(alert_id):
    return user_controller.snooze_alert(alert_id)

@user_bp.route('/alerts/snoozed', methods=['GET'])
def get_snoozed_alerts():
    return user_controller.get_snoozed_alerts()
