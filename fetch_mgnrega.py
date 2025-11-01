import requests
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Viper$1813",
    database="mgnrega_new_db"
)
cursor = conn.cursor()

API_URL = "https://api.data.gov.in/resource/ee03643a-ee4c-48c2-ac30-9f2ff26ab722"
API_KEY = "579b464db66ec23bdd000001518eba7faac74fc279f0825e1d2cb316"

params = {
    "api-key": API_KEY,
    "format": "json",
    "limit": 2000,
    "filters[state_name]": "TAMIL NADU"
}

response = requests.get(API_URL, params=params)
data = response.json()

if "records" not in data:
    print("❌ ERROR: 'records' not found")
    print(data)
    exit()

insert_query = """
INSERT INTO mgnrega_district_performance 
(district, report_year, report_month, person_days, expenditure)
VALUES (%s, %s, %s, %s, %s)
"""

count = 0
for r in data["records"]:
    district = r.get("district_name")
    year = r.get("finyear")
    month = r.get("month")
    person_days = r.get("persondays")
    expenditure = r.get("total_expenditure")

    if not district:
        continue

    cursor.execute(insert_query, (district, year, month, person_days, expenditure))
    count += 1

conn.commit()
cursor.close()
conn.close()

print(f"✅ Tamil Nadu district Data Inserted: {count} records")

