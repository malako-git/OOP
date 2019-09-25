from tkinter import *
from model.haus import *
import db_controller


class NeuesHausWindow:

    def __init__(self, master, db):
        self.db = db
        self.master = master

        self.master.geometry("600x350+300+350")
        self.master.title("Neues Haus hinzufügen")

        self.label1 = self.create_input_labels()
        self.label2 = self.create_info_labels()

        attributes = Haus.__dict__.keys()
        self.newatrib = list(filter(lambda a: not a.startswith('__'), attributes))

        print(self.newatrib)

        self.new_haus_dict={}
        count = 1
        for atrib in self.newatrib:
            self.new_haus_dict[atrib] = Entry(self.master)
            self.new_haus_dict[atrib].grid(row=count, column=1)
            count += 1

        self.button1 = Button(self.master, text="Haus hinzufügen", fg="green", command=self.add_new_haus).place(x=20,
                                                                                                                y=300,
                                                                                                                width=100,
                                                                                                                height=25)
        self.button1 = Button(self.master, text="Abbrechen", fg="red", command=self.quit).place(x=370, y=300, width=100,
                                                                                                height=25)

    def quit(self):
        self.master.destroy()

    def add_new_haus(self):
        # Get Values and add to DB
        count = 0
        new_haus = []
        for atrib in self.newatrib:
            new_haus.append(self.new_haus_dict[self.newatrib[count]].get())
            count += 1
        self.db.new_haus_table_entry(new_haus)

        # Clear Entry
        for atrib in self.new_haus_dict:
            self.new_haus_dict[atrib].delete(0, END)


    def create_input_labels(self):
        label1 = Label(self.master, text="Erstellen Sie ein neues Haus in der Datenbank", fg="black").grid(row=0, column=1)
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

    def filter_methods(self, value):
        if value.startswith('__'):
            return False
        else:
            return True
