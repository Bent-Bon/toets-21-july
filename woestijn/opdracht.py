import sqlite3
import random
def all_destinations(type):
    connection = sqlite3.connect('travel.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {type}")
    data_list = cursor.fetchall()
    connection.close()
    return data_list

plekken_checker = all_destinations("destinations")
plekken = all_destinations("destinations")
plekken.append((6, 'Nightcity', 750.0))
plekken.append((7, 'Paris', 900.0))
plekken.append((8, 'Berkel', 100.0))
print(plekken)

autos = all_destinations("cars")
print(autos)

print("")

while True:
    destinatie = random.choice(plekken)
    if destinatie in plekken_checker:
        break
print(destinatie)

print("")

beschrikbaar = []

for auto in autos:
    afstand = auto[3] * auto[4]
    if afstand >= destinatie[2]:
        beschrikbaar.append(f"ID: {auto[0]}, Brand: {auto[1]}, Model: {auto[2]}, Usage: {auto[3]} km/l, Tank Volume: {auto[4]} liters, max afstand: {afstand}")
print(beschrikbaar)