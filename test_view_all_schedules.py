import requests
from datetime import datetime

response = requests.get('http://localhost:5000/api/schedules')

if response.status_code == 200:
    schedules = response.json()
    print(f"Total Schedules: {len(schedules)}\n")
    print("=" * 80)
    
    for i, schedule in enumerate(schedules, 1):
        print(f"Schedule #{i}")
        print(f"  ID: {schedule['_id']}")
        print(f"  Recipient: {schedule['recipient']}")
        print(f"  Subject: {schedule['subject']}")
        print(f"  Scheduled Time: {schedule['scheduled_time']}")
        print(f"  Status: {schedule['status']}")
        print(f"  Created At: {schedule['created_at']}")
        print("-" * 80)
else:
    print("❌ Error:", response.json())
