import sqlite3

# 1. CREATE OR CONNECT TO DATABASE
conn = sqlite3.connect("temperature_readings.db")
cursor = conn.cursor()

# 2. CREATE TABLE
cursor.execute("""
CREATE TABLE IF NOT EXISTS Temperature_Data (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    Day_Of_Week TEXT,
    Temperature_Value REAL
)
""")

# 3. READ FILE & INSERT DATA
input_file = "Assignment5input.txt"

with open(input_file, "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        day, temp = line.split()
        temp = float(temp)

        cursor.execute("""
            INSERT INTO Temperature_Data (Day_Of_Week, Temperature_Value)
            VALUES (?, ?)
        """, (day, temp))

conn.commit()

# 4. QUERY AVERAGE TEMPERATURES
cursor.execute("""
SELECT AVG(Temperature_Value)
FROM Temperature_Data
WHERE Day_Of_Week = 'Sunday'
""")
avg_sunday = cursor.fetchone()[0]

cursor.execute("""
SELECT AVG(Temperature_Value)
FROM Temperature_Data
WHERE Day_Of_Week = 'Thursday'
""")
avg_thursday = cursor.fetchone()[0]

print("Average Sunday Temperature: ", avg_sunday)
print("Average Thursday Temperature:", avg_thursday)

conn.close()
