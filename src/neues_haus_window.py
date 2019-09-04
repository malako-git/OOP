from tkinter import *

from haus import *
import main


class NeuesHausWindow:

    def __init__(self, master):
        self.master = master

        self.master.geometry("500x350+300+350")
        self.master.title("Neues Haus hinzufügen")

        self.label1 = Label(self.master, text="Fügen sie ein neues Haus der Datenbank hinzu", fg="black").grid(row=0,
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

        Haus.farbe = Entry(self.master)
        Haus.farbe.grid(row=1, column=1)
        Haus.adresse = Entry(self.master)
        Haus.adresse.grid(row=2, column=1)
        Haus.baujahr = Entry(self.master)
        Haus.baujahr.grid(row=3, column=1)
        Haus.wohnflaeche = Entry(self.master)
        Haus.wohnflaeche.grid(row=4, column=1)
        Haus.zimmer = Entry(self.master)
        Haus.zimmer.grid(row=5, column=1)
        Haus.preis = Entry(self.master)
        Haus.preis.grid(row=6, column=1)
        Haus.grundstueckgroesse = Entry(self.master)
        Haus.grundstueckgroesse.grid(row=7, column=1)
        Haus.badezimmer = Entry(self.master)
        Haus.badezimmer.grid(row=8, column=1)
        Haus.heizart = Entry(self.master)
        Haus.heizart.grid(row=9, column=1)
        Haus.besitzer = Entry(self.master)
        Haus.besitzer.grid(row=10, column=1)

        self.button1 = Button(self.master, text="Haus hinzufügen", fg="green", command=self.add_new_haus).place(x=20,
                                                                                                                y=300,
                                                                                                                width=100,
                                                                                                                height=25)
        self.button1 = Button(self.master, text="Abbrechen", fg="red", command=self.quit).place(x=370, y=300, width=100,
                                                                                                height=25)

    def quit(self):
        self.master.destroy()

    def add_new_haus(self):
        main.Main.new_haus_table_entry(Haus.farbe.get(), Haus.adresse.get(), Haus.baujahr.get(), Haus.wohnflaeche.get(), Haus.zimmer.get(), Haus.preis.get(), Haus.grundstueckgroesse.get(), Haus.badezimmer.get(), Haus.heizart.get(), Haus.besitzer.get())
        Haus.farbe.delete(0, END)
        Haus.adresse.delete(0, END)
        Haus.baujahr.delete(0, END)
        Haus.wohnflaeche.delete(0, END)
        Haus.zimmer.delete(0, END)
        Haus.preis.delete(0, END)
        Haus.grundstueckgroesse.delete(0, END)
        Haus.badezimmer.delete(0, END)
        Haus.heizart.delete(0, END)
        Haus.besitzer.delete(0, END)