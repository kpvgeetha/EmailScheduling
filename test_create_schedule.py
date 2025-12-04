import requests
from datetime import datetime, timedelta

print("Creating a New Schedule")
print("=" * 60)

# Schedule email for 2 minutes from now
future_time = (datetime.now() + timedelta(minutes=2)).strftime("%Y-%m-%dT%H:%M:%S")
current_time = datetime.now().strftime("%Y-%m-%dT%H:%M:%S")

schedule_data = {
    "recipient": "sthitapragnya@thoughtnudge.com",  # ✅ UPDATED EMAIL
    "subject": "Weather Update - Test Email",
    "scheduled_time": future_time,
    "timezone": "Asia/Kolkata",
    "latitude": "12.9716",   # Bangalore coordinates
    "longitude": "77.5946"
}

print(f"Current time: {current_time}")
print(f"Scheduled for: {future_time}")
print(f"Recipient: {schedule_data['recipient']}")
print(f"Subject: {schedule_data['subject']}\n")

try:
    response = requests.post('http://localhost:5000/api/schedules', json=schedule_data)
    
    if response.status_code == 201:
        result = response.json()
        print("✅ Schedule created successfully!")
        print(f"Schedule ID: {result['schedule_id']}")
        print(f"\n⏰ This email will be sent in 2 minutes.")
        print("Watch your Flask app console for the email output!")
    else:
        print("❌ Error creating schedule:")
        print(response.json())
        
except Exception as e:
    print(f"❌ Request failed: {e}")
