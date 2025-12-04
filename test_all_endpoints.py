import requests
from datetime import datetime, timedelta
import time

print("=" * 80)
print("COMPREHENSIVE API TEST SUITE")
print("=" * 80)

base_url = "http://localhost:5000/api"

# Test 1: Health Check
print("\n1️⃣ Testing Health Endpoint...")
response = requests.get(f"{base_url}/health")
assert response.status_code == 200, "Health check failed"
print("✅ Health check passed")

# Test 2: Create Schedule
print("\n2️⃣ Testing Create Schedule...")
future_time = (datetime.now() + timedelta(minutes=1)).strftime("%Y-%m-%dT%H:%M:%S")
schedule_data = {
    "recipient": "sthitapragnya@thoughtnudge.com",  # ✅ UPDATED EMAIL
    "subject": "Automated Test Email",
    "scheduled_time": future_time,
    "timezone": "Asia/Kolkata",
    "latitude": "12.9716",
    "longitude": "77.5946"
}
response = requests.post(f"{base_url}/schedules", json=schedule_data)
assert response.status_code == 201, "Create schedule failed"
schedule_id = response.json()['schedule_id']
print(f"✅ Schedule created: {schedule_id}")

# Test 3: Get All Schedules
print("\n3️⃣ Testing Get All Schedules...")
response = requests.get(f"{base_url}/schedules")
assert response.status_code == 200, "Get all schedules failed"
schedules = response.json()
print(f"✅ Retrieved {len(schedules)} schedules")

# Test 4: Get Single Schedule
print("\n4️⃣ Testing Get Single Schedule...")
response = requests.get(f"{base_url}/schedules/{schedule_id}")
assert response.status_code == 200, "Get single schedule failed"
schedule = response.json()
assert schedule['_id'] == schedule_id, "Schedule ID mismatch"
print(f"✅ Retrieved schedule: {schedule['subject']}")

# Test 5: Cancel Schedule
print("\n5️⃣ Testing Cancel Schedule...")
response = requests.put(f"{base_url}/schedules/{schedule_id}/cancel")
assert response.status_code == 200, "Cancel schedule failed"
print("✅ Schedule cancelled")

# Verify cancellation
response = requests.get(f"{base_url}/schedules/{schedule_id}")
assert response.json()['status'] == 'cancelled', "Status not updated"
print("✅ Status verified as 'cancelled'")

# Test 6: Create another schedule for deletion test
print("\n6️⃣ Testing Delete Schedule...")
future_time = (datetime.now() + timedelta(minutes=5)).strftime("%Y-%m-%dT%H:%M:%S")
schedule_data['scheduled_time'] = future_time
response = requests.post(f"{base_url}/schedules", json=schedule_data)
delete_id = response.json()['schedule_id']

response = requests.delete(f"{base_url}/schedules/{delete_id}")
assert response.status_code == 200, "Delete schedule failed"
print(f"✅ Schedule deleted: {delete_id}")

# Verify deletion
response = requests.get(f"{base_url}/schedules/{delete_id}")
assert response.status_code == 404, "Schedule still exists"
print("✅ Deletion verified")

# Test 7: Get Logs
print("\n7️⃣ Testing Get Logs...")
response = requests.get(f"{base_url}/logs")
assert response.status_code == 200, "Get logs failed"
logs = response.json()
print(f"✅ Retrieved {len(logs)} email logs")

print("\n" + "=" * 80)
print("🎉 ALL TESTS PASSED!")
print("=" * 80)
