from abc import ABC, abstractmethod
from src.models import Alert, User

class BaseDeliveryChannel(ABC):
    @abstractmethod
    def send(self, alert: Alert, user: User) -> bool:
        """Send notification to user via this channel"""
        pass
    
    @abstractmethod
    def validate_config(self, config: dict) -> bool:
        """Validate channel-specific configuration"""
        pass
