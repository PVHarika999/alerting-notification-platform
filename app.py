import os
from flask import Flask, jsonify
from config.settings import config
from config.database import init_db
from api import create_api
from src.scheduler import ReminderScheduler
from data.seed_data import seed_database

def create_app(config_name=None):
    """Application factory pattern"""
    if config_name is None:
        config_name = os.environ.get('FLASK_CONFIG', 'default')
    
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    
    # Initialize database
    init_db(app)
    
    # Register API routes
    create_api(app)
    
    # Initialize scheduler
    scheduler = ReminderScheduler(app)
    
    # Health check endpoint
    @app.route('/health')
    def health_check():
        return jsonify({
            'status': 'healthy',
            'service': 'Alerting & Notification Platform',
            'version': '1.0.0'
        })
    
    # Manual trigger for reminders (for testing)
    @app.route('/api/trigger-reminders', methods=['POST'])
    def trigger_reminders():
        scheduler.trigger_reminders_manually()
        return jsonify({'message': 'Reminders triggered successfully'})
    
    return app, scheduler

if __name__ == '__main__':
    app, scheduler = create_app()
    
    # Seed database on first run
    with app.app_context():
        try:
            seed_database()
        except Exception as e:
            print(f"Database already seeded or error: {e}")
    
    print("🚀 Starting Alerting & Notification Platform...")
    print("📊 Dashboard: http://127.0.0.1:5000/health")
    print("📱 API Documentation: Check the README.md")
    
    app.run(debug=True, host='0.0.0.0', port=5000)
