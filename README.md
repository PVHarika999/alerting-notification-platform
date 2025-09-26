# Alerting & Notification Platform

A comprehensive alerting and notification system built with Flask, SQLAlchemy, and APScheduler that allows administrators to create and manage alerts while providing end users with personalized notification experiences.

## Features

### Admin Features
- ✅ Create unlimited alerts with title, message, severity levels
- ✅ Configure visibility (Organization, Team, or User-specific)
- ✅ Set start & expiry times for alerts
- ✅ Enable/disable recurring reminders (every 2 hours)
- ✅ Update and archive existing alerts
- ✅ View analytics and engagement metrics

### End User Features
- ✅ Receive alerts based on visibility settings
- ✅ Mark alerts as read/unread
- ✅ Snooze alerts for the current day
- ✅ View alert history and snoozed items
- ✅ Automatic reminder system (every 2 hours until snoozed/expired)

### System Features
- ✅ Real-time analytics dashboard
- ✅ Extensible delivery channels (In-App, Email, SMS ready)
- ✅ Clean OOP design with Strategy, Observer, and State patterns
- ✅ Background scheduler for automated reminders
- ✅ RESTful API architecture

## Installation & Setup

### Prerequisites
- Python 3.8+
- pip

### Quick Start

1. **Clone and Setup**
   git clone https://github.com/PVHarika999/alerting-notification-platform.git
cd alerting-notification-platform
2. **Install dependencies**
pip install -r requirements.txt
3. **Run setup script**
python scripts/setup.py
4. **Start the application**
python app.py
5. **Verify installation**<br>
curl http://127.0.0.1:5000/health<br>
<img width="285" height="185" alt="Image" src="https://github.com/user-attachments/assets/5f944235-046b-472f-b8fc-ea2921e224f9" /><br>

curl http://127.0.0.1:5000/api/analytics/dashboard<br>
<img width="339" height="286" alt="Image" src="https://github.com/user-attachments/assets/aae4bc73-170a-446d-bae0-a330e80c9aeb" /><br>

curl http://127.0.0.1:5000/api/user/alerts?user_id=1<br>
<img width="468" height="491" alt="Image" src="https://github.com/user-attachments/assets/be8bdc4d-c9cf-44b8-9739-26ec421bcff9" /><br>

curl http://127.0.0.1:5000/api/admin/alerts <br>
