import sqlite3


class db():
    print("conn to db open")
    conn = sqlite3.connect("haeuser.db", timeout=2)  # db erstellen und connecten
    cur = conn.cursor()  # cursor erstellen
