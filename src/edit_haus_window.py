import sqlite3
from tkinter import *

from main import *


class EditHausWindow():

    def __init__(self, master, id):
        conn = sqlite3.connect("haeuser.db", timeout=2)  # db erstellen und connecten
        cur = conn.cursor()  # cursor erstellen

        self.master = master
        self.id = id
        self.master.geometry("500x350+300+350")
        self.master.title("Haus bearbeiten")

        self.label1 = Label(self.master, text="Bearbeiten sie ein Haus aus der Datenbank", fg="black").grid(row=0,
                                                                                                            column=1)
        self.label1 = Label(self.master, text="Farbe :", fg="black").grid(row=1, column=0)
        self.label1 = Label(self.master, text="Adresse :", fg="black").grid(row=2, column=0)
        self.label1 = Label(self.master, text="Baujahr :", fg="black").grid(row=3, column=0)
        self.label1 = Label(self.master, text="Wohnfläche :", fg="black").grid(row=4, column=0)
        self.label1 = Label(self.master, text="Zimmer :", fg="black").grid(row=5, column=0)
        self.label1 = Label(self.master, text="Preis :", fg="black").grid(row=6, column=0)
        self.label1 = Label(self.master, text="Grundstückgröeße :", fg="black").grid(row=7, column=0)
        self.label1 = Label(self.master, text="Badezimmer :", fg="black").grid(row=8, column=0)
        self.label1 = Label(self.master, text="Heizart :", fg="black").grid(row=9, column=0)
        self.label1 = Label(self.master, text="Besitzer :", fg="black").grid(row=10, column=0)

        # self.label2=Label(self.master, text="",fg="black").grid(row=1,column=0)
        # self.label2=Label(self.master, text="",fg="black").grid(row=2,column=2)
        # self.label2=Label(self.master, text="",fg="black").grid(row=3,column=2)
        self.label2 = Label(self.master, text="in m²", fg="black").grid(row=4, column=2)
        # self.label2=Label(self.master, text="",fg="black").grid(row=5,column=2)
        self.label2 = Label(self.master, text="in €", fg="black").grid(row=6, column=2)
        self.label2 = Label(self.master, text="in m²", fg="black").grid(row=7, column=2)
        # self.label2=Label(self.master, text="",fg="black").grid(row=8,column=2)
        # self.label2=Label(self.master, text="",fg="black").grid(row=9,column=2)
        self.label2 = Label(self.master, text="Vorname / Nachname", fg="black").grid(row=10, column=2)

        global farbe_global
        global adresse_global
        global baujahr_global
        global wohnflaeche_global
        global zimmer_global
        global preis_global
        global grundstueckgroesse_global
        global badezimmer_global
        global heizart_global
        global besitzer_global

        farbe_global = Entry(self.master)
        farbe_global.grid(row=1, column=1)
        adresse_global = Entry(self.master)
        adresse_global.grid(row=2, column=1)
        baujahr_global = Entry(self.master)
        baujahr_global.grid(row=3, column=1)
        wohnflaeche_global = Entry(self.master)
        wohnflaeche_global.grid(row=4, column=1)
        zimmer_global = Entry(self.master)
        zimmer_global.grid(row=5, column=1)
        preis_global = Entry(self.master)
        preis_global.grid(row=6, column=1)
        grundstueckgroesse_global = Entry(self.master)
        grundstueckgroesse_global.grid(row=7, column=1)
        badezimmer_global = Entry(self.master)
        badezimmer_global.grid(row=8, column=1)
        heizart_global = Entry(self.master)
        heizart_global.grid(row=9, column=1)
        besitzer_global = Entry(self.master)
        besitzer_global.grid(row=10, column=1)

        cur.execute("SELECT * FROM HaeuserOne WHERE oid = " + self.id)
        haeuser = cur.fetchall()

        for haus in haeuser:
            farbe_global.insert(0, haus[0])
            adresse_global.insert(0, haus[1])
            baujahr_global.insert(0, haus[2])
            wohnflaeche_global.insert(0, haus[3])
            zimmer_global.insert(0, haus[4])
            preis_global.insert(0, haus[5])
            grundstueckgroesse_global.insert(0, haus[6])
            badezimmer_global.insert(0, haus[7])
            heizart_global.insert(0, haus[8])
            besitzer_global.insert(0, haus[9])

        self.button1 = Button(self.master, text="Haus speichern", fg="green", command=self.edit_haus).place(x=20, y=300,
                                                                                                            width=100,
                                                                                                            height=25)
        self.button1 = Button(self.master, text="Abbrechen", fg="red", command=self.quit).place(x=370, y=300, width=100,
                                                                                                height=25)

    def quit(self):
        self.master.destroy()

    def edit_haus(self):
        Main.edit_haus_table_entry(self.id)
