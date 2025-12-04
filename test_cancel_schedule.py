import requests

# First, get all schedules
response = requests.get('http://localhost:5000/api/schedules')
schedules = response.json()

if len(schedules) == 0:
    print("No schedules found!")
else:
    # Get the first pending schedule
    pending = [s for s in schedules if s['status'] == 'pending']
    
    if len(pending) == 0:
        print("No pending schedules to cancel!")
    else:
        schedule_id = pending[0]['_id']
        print(f"Cancelling schedule: {schedule_id}")
        print(f"Recipient: {pending[0]['recipient']}")
        
        # Cancel it
        cancel_response = requests.put(f'http://localhost:5000/api/schedules/{schedule_id}/cancel')
        
        if cancel_response.status_code == 200:
            print("✅ Schedule cancelled successfully!")
        else:
            print("❌ Error:", cancel_response.json())
