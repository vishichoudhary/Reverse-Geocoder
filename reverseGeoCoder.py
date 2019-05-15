import hashlib
import sqlite3
conn = sqlite3.connect('cordinatedToAddress.db')
cursor = conn.cursor()

coordinatesTable = """ CREATE TABLE IF NOT EXISTS coordinates(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    lat VARCHAR(10),
                                    lng VARCHAR(10),
                                    address VARCHAR(50)
                                ); """
cursor.execute(coordinatesTable)


class ReverseGeoCoder:

    def __init__(self):
        self.coordinates = []

    def registerCoordintes(self):
        coordinates = input()
        if not coordinates[0] == "[":
            coordinates = input().split(",")
            self.coordinates.append([coordinates[0][1:], coordinates[1][:-1]])
        else:
            coordinates = coordinates[1:-1].split(',')
            for index, coordinate in enumerate(coordinates):
                if index % 2 == 1:
                    self.coordinates.append(
                        [coordinates[index-1][1:], coordinates[index][:-1]])

    def fetchAddress(self, lat, lng):
        # call maps api here, but we are faking api call for randrom address
        hash_object = hashlib.md5((lat + lng).encode())
        return hash_object.hexdigest()

    def run(self):
        mappedAddress = {}
        for coordinate in self.coordinates:
            cursor.execute(
                'SELECT * FROM coordinates WHERE lat=? and lng=?', (coordinate[0], coordinate[1]))
            result = cursor.fetchone()
            if result == None:
                # cache the result
                address = self.fetchAddress(coordinate[0], coordinate[1])
                cursor.execute('insert into coordinates(lat, lng, address) values(?, ?, ?);', (
                    coordinate[0], coordinate[1], address))
                mappedAddress[coordinate[0] + "," + coordinate[1]] = address
            else:
                mappedAddress[coordinate[0] + "," + coordinate[1]] = result[3]
        print(mappedAddress)


reverseGeoCoder = ReverseGeoCoder()
reverseGeoCoder.registerCoordintes()
reverseGeoCoder.run()