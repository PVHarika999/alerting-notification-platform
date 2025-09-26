
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
GET http://127.0.0.1:5000//api/admin/alerts?admin_id=1<br>
<img width="666" height="532" alt="Image" src="https://github.com/user-attachments/assets/32cedb5f-fc40-40ee-81f7-a21e6397af01" /><br>

#### **4. Update Alert**
GET http://127.0.0.1:5000/api/admin/alerts/1<br>
<img width="438" height="482" alt="Image" src="https://github.com/user-attachments/assets/dbd191b8-9d27-48b6-8d6f-930528a8962f" />

#### **5. Get Alert Analytics**
GET http://127.0.0.1:5000//api/admin/alerts/1/analytics <br>
<img width="367" height="312" alt="Image" src="https://github.com/user-attachments/assets/3158529b-9c9b-44b4-8f40-3d0f1f062a75" />
/><br>
<img width="436" height="283" alt="Image" src="https://github.com/user-attachments/assets/d1e3f924-ce52-4ced-94f5-7fff50a8f68a" />
#### **6. Archive Alert**<br>

POST http://127.0.0.1:5000//api/admin/alerts/1/archive<br>
<img width="436" height="283" alt="Image" src="https://github.com/user-attachments/assets/d1e3f924-ce52-4ced-94f5-7fff50a8f68a" /><br>

---

### **User Endpoints (4 Tests)**

#### **7. Get User Alerts**
GET http://127.0.0.1:5000/api/user/alerts?user_id=2 <br>
<img width="417" height="480" alt="Image" src="https://github.com/user-attachments/assets/92f46d27-a58c-4b3f-8bb8-b17058e0aab9" /><br>

#### **8. Mark Alert as Read**
POST http://127.0.0.1:5000//api/user/alerts/1/read
<img width="413" height="286" alt="Image" src="https://github.com/user-attachments/assets/baf5290f-2e50-40d6-b68a-bafb4ca138df" /><br>

#### **9. Snooze Alert**
POST http://127.0.0.1:5000/api/user/alerts/1/snooze <br>
<img width="388" height="340" alt="Image" src="https://github.com/user-attachments/assets/98e7ba11-d72b-405d-99af-258d83a270bd" /> <br>

#### **10. Get Snoozed Alerts History**
GET http://127.0.0.1:5000//api/user/alerts/snoozed?user_id=2
<img width="519" height="315" alt="Image" src="https://github.com/user-attachments/assets/2cd8a30b-1919-4569-a673-45beb4134ad8" />


---

### **Analytics Endpoints (1 Test)**

#### **11. System Dashboard Analytics**

GET http://127.0.0.1:5000/api/analytics/dashboard
<img width="522" height="372" alt="Image" src="https://github.com/user-attachments/assets/70955c6d-a6c8-4f6b-97d3-99d35cf366aa" />

---

### **Bonus: Manual Reminder Trigger**

#### **12. Trigger Reminders (Testing)**
POST http://127.0.0.1:5000/api/trigger-reminders
<img width="516" height="283" alt="Image" src="https://github.com/user-attachments/assets/f919e015-ed7e-4478-8779-78212019d369" />
