from config.database import db
from src.models import User, Team, Alert
import json
from datetime import datetime, timedelta

def seed_database():
    """Seed the database with sample data"""
    
    # Create teams
    engineering = Team(name="Engineering", description="Software development team")
    marketing = Team(name="Marketing", description="Marketing and growth team")
    hr = Team(name="HR", description="Human resources team")
    
    db.session.add_all([engineering, marketing, hr])
    db.session.commit()
    
    # Create users
    users = [
        User(name="Admin User", email="admin@company.com", is_admin=True, team_id=engineering.id),
        User(name="John Developer", email="john@company.com", team_id=engineering.id),
        User(name="Jane Marketing", email="jane@company.com", team_id=marketing.id),
        User(name="Bob HR", email="bob@company.com", team_id=hr.id),
        User(name="Alice Engineer", email="alice@company.com", team_id=engineering.id),
    ]
    
    db.session.add_all(users)
    db.session.commit()
    
    # Create sample alerts
    alerts = [
        Alert(
            title="System Maintenance Tonight",
            message="The system will be down for maintenance from 11 PM to 1 AM.",
            severity="warning",
            visibility_type="organization",
            target_audience=json.dumps([]),
            created_by=1,
            expiry_time=datetime.utcnow() + timedelta(days=1)
        ),
        Alert(
            title="New Security Policy",
            message="Please review the updated security policy in the company handbook.",
            severity="info",
            visibility_type="organization", 
            target_audience=json.dumps([]),
            created_by=1,
            expiry_time=datetime.utcnow() + timedelta(days=7)
        ),
        Alert(
            title="Engineering Team Meeting",
            message="Weekly engineering standup at 10 AM tomorrow.",
            severity="info",
            visibility_type="team",
            target_audience=json.dumps([engineering.id]),
            created_by=1,
            expiry_time=datetime.utcnow() + timedelta(days=1)
        ),
        Alert(
            title="Critical: Server Down",
            message="Production server is experiencing issues. All hands on deck!",
            severity="critical",
            visibility_type="team",
            target_audience=json.dumps([engineering.id]),
            created_by=1,
            expiry_time=datetime.utcnow() + timedelta(hours=6)
        )
    ]
    
    db.session.add_all(alerts)
    db.session.commit()
    
    print("✅ Database seeded successfully!")
    print(f"Created {len(users)} users, {len(alerts)} alerts, and 3 teams")
