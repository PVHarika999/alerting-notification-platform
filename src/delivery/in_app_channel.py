from .base_channel import BaseDeliveryChannel
from src.models import Alert, User

class InAppChannel(BaseDeliveryChannel):
    def send(self, alert: Alert, user: User) -> bool:
        """Send in-app notification (stored in database)"""
        try:
            # In-app notifications are handled via database records
            # The notification is already created in NotificationDelivery
            # This could be extended to push to websockets, etc.
            print(f"📱 In-App Alert for {user.name}: {alert.title}")
            return True
        except Exception as e:
            print(f"Failed to send in-app notification: {e}")
            return False
    
    def validate_config(self, config: dict) -> bool:
        """Validate in-app channel config"""
        return True  # No special config needed for in-app
