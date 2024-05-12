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

#Print music_artists table
for row in cursor.execute("select * from music_artists"):
    print(row)

#Print music_artists entries containing "Rock" as genre
cursor.execute("select * from music_artists where genre=:g", {"g": "Rock"})
rockSearch = cursor.fetchall()
print(rockSearch)

genre_data = [
    ("Rock", "Los Angeles"),
    ("Hippie", "Eugene"),
    ("Opera", "Florence")
]
cursor.execute("create table genres (genre text, city text)")
cursor.executemany("insert into genres values (?,?)", genre_data)
connection.commit()

#Print genre table
for row in cursor.execute("select * from genres"):
    print(row)

#Inner join both tables
cursor.execute("select music_artists.artist from music_artists inner join genres on music_artists.genre = genres.genre")
genreSearch = cursor.fetchall()
for row in genreSearch:
    print(row)
connection.close()