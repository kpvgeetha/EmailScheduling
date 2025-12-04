import requests
import os

print("Bulk Upload Schedules from CSV")
print("=" * 60)

csv_file = 'sample_schedules.csv'

# Check if file exists
if not os.path.exists(csv_file):
    print(f"❌ File not found: {csv_file}")
    print("\nCreate a CSV file named 'sample_schedules.csv' with this content:")
    print("-" * 60)
    print("recipient,subject,scheduled_time,timezone,latitude,longitude")
    print("sthitapragnya@thoughtnudge.com,Morning Weather,2025-12-05T08:00:00,Asia/Kolkata,12.9716,77.5946")
    print("sthitapragnya@thoughtnudge.com,Afternoon Update,2025-12-05T14:00:00,Asia/Kolkata,19.0760,72.8777")
    print("sthitapragnya@thoughtnudge.com,Evening Brief,2025-12-05T18:00:00,Asia/Kolkata,28.7041,77.1025")
    print("-" * 60)
else:
    print(f"Uploading: {csv_file}\n")
    
    with open(csv_file, 'rb') as f:
        files = {'file': (csv_file, f, 'text/csv')}
        response = requests.post('http://localhost:5000/api/schedules/upload', files=files)
    
    if response.status_code == 201:
        result = response.json()
        print("✅ Bulk upload successful!")
        print(f"Schedules created: {result['count']}")
        print(f"Message: {result['message']}")
        
        # Show all schedules
        print("\nFetching all schedules...")
        all_schedules = requests.get('http://localhost:5000/api/schedules')
        if all_schedules.status_code == 200:
            print(f"Total schedules now: {len(all_schedules.json())}")
    else:
        print("❌ Error uploading file:")
        print(response.json())
