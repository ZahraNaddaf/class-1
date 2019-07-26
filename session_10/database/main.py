import sqlite3

path = "C:/Users/Student/Downloads/chinook.db"

conn = sqlite3.connect(path)

rows = conn.execute("""
SELECT t.name آهنگ , t.milliseconds/60 دقیقه, a.title عنوان FROM tracks as t
join albums as a on  t.albumid= a.albumid
join artists as ar on a.artistid = ar.artistid
""")


for row in rows:
    print(row)