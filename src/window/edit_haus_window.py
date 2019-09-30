import sqlite3
from tkinter import *
from model.haus import *
from db_controller import *


class EditHausWindow:

    def __init__(self, master, db, haus, id):
        self.master = master
        self.db = db
        self.haus = haus
        self.id = id

        self.master.geometry("500x350+300+350")
        self.master.title("Haus bearbeiten")
        self.label1 = self.create_input_labels()
        self.label2 = self.create_info_labels()

        attributes = Haus.__dict__.keys()
        self.filtered_atrib = list(filter(lambda a: not (a.startswith('__') or a.startswith('fill')), attributes))

        self.list_elements = {}
        count = 1
        for atrib in self.filtered_atrib:
            self.list_elements[atrib] = Entry(self.master)
            self.list_elements[atrib].grid(row=count, column=1)
            self.list_elements[atrib].insert(0, self.haus.__dict__[atrib])
            count += 1

        self.button1 = Button(self.master, text="Haus speichern", fg="green", command=self.edit_haus).place(x=20, y=300, width=100, height=25)
        self.button1 = Button(self.master, text="Abbrechen", fg="red", command=self.quit).place(x=370, y=300, width=100, height=25)

    def quit(self):
        self.master.destroy()

    def edit_haus(self):
        for atrib in self.filtered_atrib:
            self.haus.__dict__[atrib] = self.list_elements[atrib].get()

        self.db.edit_haus_table_entry(self.haus, self.id)

    def create_input_labels(self):
        label1 = Label(self.master, text="Bearbeiten sie ein Haus aus der Datenbank", fg="black").grid(row=0, column=1)
        label1 = Label(self.master, text="Farbe :", fg="black").grid(row=1, column=0)
        label1 = Label(self.master, text="Adresse :", fg="black").grid(row=2, column=0)
        label1 = Label(self.master, text="Baujahr :", fg="black").grid(row=3, column=0)
        label1 = Label(self.master, text="Wohnfläche :", fg="black").grid(row=4, column=0)
        label1 = Label(self.master, text="Zimmer :", fg="black").grid(row=5, column=0)
        label1 = Label(self.master, text="Preis :", fg="black").grid(row=6, column=0)
        label1 = Label(self.master, text="Grundstückgröeße :", fg="black").grid(row=7, column=0)
        label1 = Label(self.master, text="Badezimmer :", fg="black").grid(row=8, column=0)
        label1 = Label(self.master, text="Heizart :", fg="black").grid(row=9, column=0)
        label1 = Label(self.master, text="Besitzer :", fg="black").grid(row=10, column=0)

        return label1

    def create_info_labels(self):
        # label2=Label(self.master, text="",fg="black").grid(row=1,column=0)
        # label2=Label(self.master, text="",fg="black").grid(row=2,column=2)
        # label2=Label(self.master, text="",fg="black").grid(row=3,column=2)
        label2 = Label(self.master, text="in m²", fg="black").grid(row=4, column=2)
        # label2=Label(self.master, text="",fg="black").grid(row=5,column=2)
        label2 = Label(self.master, text="in €", fg="black").grid(row=6, column=2)
        label2 = Label(self.master, text="in m²", fg="black").grid(row=7, column=2)
        # label2=Label(self.master, text="",fg="black").grid(row=8,column=2)
        # label2=Label(self.master, text="",fg="black").grid(row=9,column=2)
        label2 = Label(self.master, text="Vorname / Nachname", fg="black").grid(row=10, column=2)

        return label2
