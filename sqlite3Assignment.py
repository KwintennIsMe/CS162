import sqlite3

connection = sqlite3.connect("artists.db")
cursor = connection.cursor()
cursor.execute("create table music_artists (artist text, genre text, number_recordings integer)")
musicArtists = [
    ("Miley", "Rock", 14),
    ("Dolly", "Country", 123),
    ("Eminem", "HipHop", 98),
    ("Brittany", "Rock", 37)
]
cursor.executemany("insert into music_artists values (?,?,?)", musicArtists)
connection.commit()

#Print music_artists
for row in cursor.execute("select * from music_artists"):
    print(row)

#Print music_artists entries containing "Rock" as genre
cursor.execute("select * from music_artists where genre=:g", {"g": "Rock"})
rockSearch = cursor.fetchall()
print(rockSearch)

connection.close()