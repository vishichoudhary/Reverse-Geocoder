import sqlite3
conn = sqlite3.connect('cordinatedToAddress.db')
cursor = conn.cursor()

coordinatesTable = """ CREATE TABLE IF NOT EXISTS coordinates(
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    lat VARCHAR(10),
                                    long VARCHAR(10),
                                    address VARCHAR(50)
                                ); """
cursor.execute(coordinatesTable)

class ReverseGeoCoder:

    def __init__(self):
        self.coordinates = []

    def registerCoordintes(self):
        self.coordinates.append(['28.657776','77.289506'])
        self.coordinates.append(['28.657776','77.289506'])

    def run(self):
        for coordinate in self.coordinates:
            cursor.execute('SELECT * FROM coordinates WHERE lat=? and long=?' % (coordinate[0], coordinate[1]))
            result = cursor.fetchone()
            if result == None:
                # cache the result
                cursor.execute('insert into coordinates(lat, long, address) values(?, ?, ?);' , (coordinate[0], coordinate[1], "random hu maai"))
            else:
                print(result)

reverseGeoCoder = ReverseGeoCoder()
reverseGeoCoder.registerCoordintes()
reverseGeoCoder.run()

