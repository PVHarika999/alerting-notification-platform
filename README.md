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
## 🧪 Complete API Testing Guide

### Prerequisites for Testing
- Application running on `http://127.0.0.1:5000`
- Use curl, Postman, or any REST client
- Default users and alerts are seeded automatically

---

## **Testing All 11 Endpoints**
I have used Postman
### **1. System Health Check**
GET http://127.0.0.1:5000/health<br>
<img width="649" height="312" alt="Image" src="https://github.com/user-attachments/assets/43991c9e-0e10-447d-a70f-35b452738bf5" />

---

### **Admin Endpoints (5 Tests)**

#### **2. Create Alert**

POST http://127.0.0.1:5000/api/admin/alerts <br>
{
"title": "System Maintenance Tonight",
"message": "Scheduled maintenance from 11 PM to 1 AM. Please save your work.",
"severity": "warning",
"visibility_type": "organization",
"target_audience": [],
"expiry_time": "2025-09-28T01:00:00"
}

<img width="672" height="494" alt="Image" src="https://github.com/user-attachments/assets/f1bde086-b670-4637-a0ac-1a489386cdd1" /><br>

GET http://127.0.0.1:5000/api/admin/alerts?admin_id=1
"alerts": [
        {
            "created_at": "2025-09-26T08:50:10.498560",
            "created_by": 1,
            "delivery_type": "in_app",
            "expiry_time": "2025-09-28T01:00:00",
            "id": 6,
            "is_active": true,
            "message": "Scheduled maintenance from 11 PM to 1 AM. Please save your work.",
            "reminder_enabled": true,
            "reminder_frequency_hours": 2,
            "severity": "warning",
            "start_time": "2025-09-26T08:50:10.497324",
            "target_audience": "[]",
            "title": "System Maintenance Tonight",
            "visibility_type": "organization"
        },
        {
            "created_at": "2025-09-26T08:44:17.133594",
            "created_by": 1,
            "delivery_type": "in_app",
            "expiry_time": "2025-09-28T01:00:00",
            "id": 5,
            "is_active": true,
            "message": "Scheduled maintenance from 11 PM to 1 AM. Please save your work.",
            "reminder_enabled": true,
            "reminder_frequency_hours": 2,
            "severity": "warning",
            "start_time": "2025-09-26T08:44:17.092902",
            "target_audience": "[]",
            "title": "System Maintenance Tonight",
            "visibility_type": "organization"
        },
        {
            "created_at": "2025-09-26T07:54:01.257614",
            "created_by": 1,
            "delivery_type": "in_app",
            "expiry_time": "2025-09-26T13:54:01.256805",
            "id": 4,
            "is_active": true,
            "message": "Production server is experiencing issues. All hands on deck!",
            "reminder_enabled": true,
            "reminder_frequency_hours": 2,
            "severity": "critical",
            "start_time": "2025-09-26T07:54:01.257614",
            "target_audience": "[1]",
            "title": "Critical: Server Down",
            "visibility_type": "team"
        },
        {
            "created_at": "2025-09-26T07:54:01.257612",
            "created_by": 1,
            "delivery_type": "in_app",
            "expiry_time": "2025-09-27T07:54:01.256779",
            "id": 3,
            "is_active": true,
            "message": "Weekly engineering standup at 10 AM tomorrow.",
            "reminder_enabled": true,
            "reminder_frequency_hours": 2,
            "severity": "info",
            "start_time": "2025-09-26T07:54:01.257611",
            "target_audience": "[1]",
            "title": "Engineering Team Meeting",
            "visibility_type": "team"
        },
        {
            "created_at": "2025-09-26T07:54:01.257610",
            "created_by": 1,
            "delivery_type": "in_app",
            "expiry_time": "2025-10-03T07:54:01.256357",
            "id": 2,
            "is_active": true,
            "message": "Please review the updated security policy in the company handbook.",
            "reminder_enabled": true,
            "reminder_frequency_hours": 2,
            "severity": "info",
            "start_time": "2025-09-26T07:54:01.257609",
            "target_audience": "[]",
            "title": "New Security Policy",
            "visibility_type": "organization"
        },
        {
            "created_at": "2025-09-26T07:54:01.257607",
            "created_by": 1,
            "delivery_type": "in_app",
            "expiry_time": "2025-09-27T07:54:01.256311",
            "id": 1,
            "is_active": true,
            "message": "The system will be down for maintenance from 11 PM to 1 AM.",
            "reminder_enabled": true,
            "reminder_frequency_hours": 2,
            "severity": "warning",
            "start_time": "2025-09-26T07:54:01.257605",
            "target_audience": "[]",
            "title": "System Maintenance Tonight",
            "visibility_type": "organization"
        }
    ]
}

