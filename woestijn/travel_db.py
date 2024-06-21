import sqlite3

conn = sqlite3.connect('travel.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS cars (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        brand TEXT NOT NULL,
        model TEXT NOT NULL,
        usage REAL NOT NULL,  -- Changed to REAL to reflect kilometers per liter
        tankvolume REAL NOT NULL
    )
''')

cars = [
    ('Toyota', 'Corolla', 15.0, 61.0),
    ('Honda', 'Civic', 34.5, 61.2),
    ('Ford', 'Mustang', 11.3, 60.0),
    ('Chevrolet', 'Impala', 10.0, 65.0),
    ('BMW', 'X5', 9.4, 85.0),
    ('Audi', 'A4', 14.0, 60.0),
    ('Mercedes-Benz', 'C-Class', 20.5, 71.0),
    ('Volkswagen', 'Golf', 17.0, 64.0),
    ('Hyundai', 'Elantra', 15.5, 53.0),
    ('Nissan', 'Altima', 16.5, 69.0)
]

cursor.executemany('''
    INSERT INTO cars (brand, model, usage, tankvolume)
    VALUES (?, ?, ?, ?)
''', cars)

cursor.execute('''
    CREATE TABLE IF NOT EXISTS destinations (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        distance REAL NOT NULL  -- Distance in kilometers
    )
''')

destinations = [
    ('Tunis', 300.0),
    ('Tripoli', 600.0),
    ('Cairo', 900.0),
    ('Bamako', 1300.0),
    ('Khartoum', 1700.0)
]

cursor.executemany('''
    INSERT INTO destinations (name, distance)
    VALUES (?, ?)
''', destinations)

conn.commit()
conn.close()

print("Database created and 10 cars plus 5 destinations inserted successfully.")
