import sqlite3

from window.main_window import *


class DB_Controller:

    def __init__(self):
        self.conn = sqlite3.connect("haeuser.db", timeout=2)  # db erstellen und connecten
        self.cur = self.conn.cursor()  # cursor erstellen#

    def main(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS HaeuserOne (
            Farbe TEXT(20),
            Adresse TEXT,
            Baujahr INTEGER,
            Wohnflaeche REAL,
            Zimmer INTEGER,
            Preis REAL,
            Grundstueckgroesse REAL,
            Badezimmer INTEGER,
            Heizart TEXT,
            Besitzer TEXT
            )""")
        # erstellt einen table in der datenbank haeuser.db und definiert die entrys und deren type
        self.conn.commit()

    def new_haus_table_entry(self, haus):
        print("erstelle neuen eintrag in Datenbank")
        self.cur.execute("INSERT INTO HaeuserOne VALUES(?, ?, ?, ? ,?, ?, ?, ?, ?, ?)", (
            haus.farbe,
            haus.adresse,
            haus.baujahr,
            haus.wohnflaeche,
            haus.zimmer,
            haus.preis,
            haus.grundstueckgroesse,
            haus.badezimmer,
            haus.heizart,
            haus.besitzer))
        # cur.execute("INSERT INTO HaeuserOne (%s) VALUES(?)" %(attr),(data,))
        # cursor.execute("INSERT INTO PRESSURE (" + city + ") values (?)", (pressure,))
        self.conn.commit()
        # db.conn.close()

    def edit_haus_table_entry(self, haus, id):
        print("bearbeite eintrag @ oid" + id)

        self.cur.execute("""UPDATE HaeuserOne SET
            Farbe = :farbe,
            Adresse = :adresse,
            Baujahr = :baujahr,
            Wohnflaeche = :wohnflaeche,
            Zimmer = :zimmer,
            Preis = :preis,
            Grundstueckgroesse = :grundstueckgroesse,
            Badezimmer = :badezimmer,
            Heizart = :heizart,
            Besitzer = :besitzer

            WHERE oid = :oid""",
                         {
                             "farbe": haus.farbe,
                             "adresse": haus.adresse,
                             "baujahr": haus.baujahr,
                             "wohnflaeche": haus.wohnflaeche,
                             "zimmer": haus.zimmer,
                             "preis": haus.preis,
                             "grundstueckgroesse": haus.grundstueckgroesse,
                             "badezimmer": haus.badezimmer,
                             "heizart": haus.heizart,
                             "besitzer": haus.besitzer,

                             "oid": id

                         })

        self.conn.commit()

    def show_db(self):

        self.cur.execute("SELECT *, oid FROM HaeuserOne")
        haeuser_in_db = self.cur.fetchall()

        # print(haeuser_in_db)

        print_db = ""

        for haeuser in haeuser_in_db:
            print_db += str(haeuser[10]) + " " + "\t" + str(haeuser[1]) + " // " + str(haeuser[9]) + "\n"
        return (print_db)

    def delete(self, id):
        try:
            self.cur.execute("DELETE from HaeuserOne WHERE oid = " + id)
            self.conn.commit()
        except Error:
            print("User Error !!!")

    def getHaus(self, id):
        self.cur.execute("SELECT * FROM HaeuserOne WHERE oid = " + id)
        return self.cur.fetchone()
