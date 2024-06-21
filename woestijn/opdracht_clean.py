import sqlite3
import random
def all_destinations(type):
    connection = sqlite3.connect('travel.db')
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {type}")
    data_list = cursor.fetchall()
    connection.close()
    return data_list

plekken = all_destinations("destinations")
print(plekken)

autos = all_destinations("cars")
print(autos)

print("")

destinatie = random.choice(plekken)

print(f"plek: {destinatie}")

print("")

beschrikbaar = []

for auto in autos:
    afstand = auto[3] * auto[4]
    if afstand >= destinatie[2]:
        beschrikbaar.append(f"ID: {auto[0]}, Brand: {auto[1]}, Model: {auto[2]}, Usage: {auto[3]} km/l, Tank Volume: {auto[4]} liters, max afstand: {afstand}")
print(f"alle beschrikbare auto's:")
for car in beschrikbaar:
    print(car)