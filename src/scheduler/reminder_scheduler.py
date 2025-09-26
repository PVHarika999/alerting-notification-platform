from apscheduler.schedulers.background import BackgroundScheduler
from src.services import NotificationService
import logging

class ReminderScheduler:
    def __init__(self, app=None):
        self.scheduler = BackgroundScheduler()
        self.notification_service = NotificationService()
        self.app = app
        
        if app:
            self.init_app(app)
    
    def init_app(self, app):
        """Initialize scheduler with Flask app"""
        self.app = app
        
        # Schedule reminder job every 2 hours
        self.scheduler.add_job(
            func=self.send_reminders,
            trigger="interval",
            hours=2,
            id='reminder_job'
        )
        
        # Start scheduler
        self.scheduler.start()
        
        # Ensure scheduler shuts down when app closes
        import atexit
        atexit.register(lambda: self.scheduler.shutdown())
    
    def send_reminders(self):
        """Send reminder notifications for active alerts"""
        try:
            with self.app.app_context():
                self.notification_service.send_reminders()
                print("✅ Reminder notifications sent successfully")
        except Exception as e:
            print(f"❌ Error sending reminders: {e}")
            logging.error(f"Reminder job failed: {e}")
    
    def trigger_reminders_manually(self):
        """Manually trigger reminders (for testing)"""
        self.send_reminders()
