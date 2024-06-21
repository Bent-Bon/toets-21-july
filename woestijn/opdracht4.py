import sqlite3
def car_picker(location):
    connection = sqlite3.connect('travel.db')
    cursor = connection.cursor()

    cursor.execute("SELECT distance FROM destinations WHERE name = ?", (location,))
    eind_data = cursor.fetchone()

    if eind_data is None:
        print(f"locatie '{location}' not in the database.")
        return []

    cursor.execute("SELECT * FROM cars WHERE (usage * tankvolume) >= ?", (eind_data[0],))
    autos = cursor.fetchall()

    connection.close()
    return autos

#test
locatie_lijst = ["Cairo", "Tunis", "Khartoum", "Tripoli", "Bamako"]
for plek in locatie_lijst:
    beschrikbare_autos = car_picker(plek)
    if beschrikbare_autos == []:
        print(f"geen auto's mogelijk voor {plek}")
    else:
        print(f"voor {plek} heeft u keuze uit:")
        for auto in beschrikbare_autos:
            print(auto)
    print("")