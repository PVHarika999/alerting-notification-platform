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

#### **3. List Admin Alerts**

GET http://127.0.0.1:5000//api/admin/alerts/1 <br>
<img width="438" height="482" alt="Image" src="https://github.com/user-attachments/assets/dbd191b8-9d27-48b6-8d6f-930528a8962f" />

#### **4. Update Alert**

#### **5. Get Alert Analytics**

#### **6. Archive Alert**

---

### **User Endpoints (4 Tests)**

#### **7. Get User Alerts**

#### **8. Mark Alert as Read**

#### **9. Snooze Alert**

#### **10. Get Snoozed Alerts History**

---

### **Analytics Endpoints (1 Test)**

#### **11. System Dashboard Analytics**

---

### **Bonus: Manual Reminder Trigger**

#### **12. Trigger Reminders (Testing)**
