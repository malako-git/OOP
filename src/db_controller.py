from window.main_window import *
from db import *


class DB_Controller():

    def __init__(self, master, id):
        self.id = id
        self.master = master

    def main():
        db.cur.execute("""CREATE TABLE IF NOT EXISTS HaeuserOne (
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
        db.conn.commit()

        master = Tk()
        MainWindow(master)
        master.mainloop()

    def new_haus_table_entry(farbe, adresse, baujahr, wohnflaeche, zimmer, preis, grundstueckgroesse, badezimmer, heizart, besitzer):
        print("erstelle neuen eintrag in Datenbank")
        db.cur.execute("INSERT INTO HaeuserOne VALUES(?, ?, ?, ? ,?, ?, ?, ?, ?, ?)", (
        farbe, adresse, baujahr, wohnflaeche, zimmer, preis, grundstueckgroesse, badezimmer, heizart, besitzer))
        # cur.execute("INSERT INTO HaeuserOne (%s) VALUES(?)" %(attr),(data,))
        # cursor.execute("INSERT INTO PRESSURE (" + city + ") values (?)", (pressure,))
        db.conn.commit()
        # db.conn.close()

    def edit_haus_table_entry(id):
        print("bearbeite eintrag @ oid" + id)

        db.cur.execute("""UPDATE HaeuserOne SET
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
                           "farbe": farbe_global.get(),
                           "adresse": adresse_global.get(),
                           "baujahr": baujahr_global.get(),
                           "wohnflaeche": wohnflaeche_global.get(),
                           "zimmer": zimmer_global.get(),
                           "preis": preis_global.get(),
                           "grundstueckgroesse": grundstueckgroesse_global.get(),
                           "badezimmer": badezimmer_global.get(),
                           "heizart": heizart_global.get(),
                           "besitzer": besitzer_global.get(),

                           "oid": id

                       })

        db.conn.commit()
