from tkinter import *
import sqlite3
import time
from tkinter import scrolledtext
# pass

class ScrolledText(Text):
    def __init__(self, master=None, **kw):
        self.frame = Frame(master)
        self.vbar = Scrollbar(self.frame)
        self.vbar.pack(side=RIGHT, fill=Y)

        kw.update({'yscrollcommand': self.vbar.set})
        Text.__init__(self, self.frame, **kw)
        self.pack(side=LEFT, fill=BOTH, expand=True)
        self.vbar['command'] = self.yview

        # Copy geometry methods of self.frame without overriding Text
        # methods -- hack!
        text_meths = vars(Text).keys()
        methods = vars(Pack).keys() | vars(Grid).keys() | vars(Place).keys()
        methods = methods.difference(text_meths)

        for m in methods:
            if m[0] != '_' and m != 'config' and m != 'configure':
                setattr(self, m, getattr(self.frame, m))

    def __str__(self):
        return str(self.frame)

class MainWindow():

    def __init__(self, master):
        self.master = master
        self.master.geometry("1000x700+200+200")
        self.master.title("Hausverwaltungs Software")

        self.button1 = Button(self.master, text="Neues Haus", fg="black",command=self.new_haus_window).place(x =10, y=20, width=120,height=30)
        self.button2 = Button(self.master, text="Bearbeiten", fg="black",command=self.edit_haus_window).place(x =140, y=20, width=120,height=30)
        self.button3 = Button(self.master, text="Quit", fg="red",command=self.quit).place(x =870, y=20, width=120,height=30)

    def new_haus_window(self):
        root2=Toplevel(self.master)
        myGUI=NeuesHausWindow(root2)

    def edit_haus_window(self):
        pass

    def quit(self):
        self.master.destroy()

    def view_db():
        stext = ScrolledText(bg="white", height=10)
        stext.place(x=10, y=60)
        stext.focus_set()
        stext.mainloop()



class NeuesHausWindow():

    def __init__(self, master):
        self.master=master

        self.master.geometry("500x350+300+350")
        self.master.title("Neues Haus hinzufügen")

        self.label1=Label(self.master, text="Fügen sie ein neues Haus der Datenbank hinzu",fg="black").grid(row=0,column=1)
        self.label1=Label(self.master, text="Farbe :",fg="black").grid(row=1,column=0)
        self.label1=Label(self.master, text="Adresse :",fg="black").grid(row=2,column=0)
        self.label1=Label(self.master, text="Baujahr :",fg="black").grid(row=3,column=0)
        self.label1=Label(self.master, text="Wohnfläche :",fg="black").grid(row=4,column=0)
        self.label1=Label(self.master, text="Zimmer :",fg="black").grid(row=5,column=0)
        self.label1=Label(self.master, text="Preis :",fg="black").grid(row=6,column=0)
        self.label1=Label(self.master, text="Grundstückgröeße :",fg="black").grid(row=7,column=0)
        self.label1=Label(self.master, text="Badezimmer :",fg="black").grid(row=8,column=0)
        self.label1=Label(self.master, text="Heizart :",fg="black").grid(row=9,column=0)
        self.label1=Label(self.master, text="Besitzer :",fg="black").grid(row=10,column=0)

        self.label2=Label(self.master, text="",fg="black").grid(row=1,column=0)
        self.label2=Label(self.master, text="",fg="black").grid(row=2,column=2)
        self.label2=Label(self.master, text="",fg="black").grid(row=3,column=2)
        self.label2=Label(self.master, text="in m²",fg="black").grid(row=4,column=2)
        self.label2=Label(self.master, text="",fg="black").grid(row=5,column=2)
        self.label2=Label(self.master, text="in €",fg="black").grid(row=6,column=2)
        self.label2=Label(self.master, text="in m²",fg="black").grid(row=7,column=2)
        self.label2=Label(self.master, text="",fg="black").grid(row=8,column=2)
        self.label2=Label(self.master, text="",fg="black").grid(row=9,column=2)
        self.label2=Label(self.master, text="Vorname / Nachname",fg="black").grid(row=10,column=2)

        Haus.farbe=Entry(self.master)
        Haus.farbe.grid(row=1,column=1)
        Haus.adresse=Entry(self.master)
        Haus.adresse.grid(row=2,column=1)
        Haus.baujahr=Entry(self.master)
        Haus.baujahr.grid(row=3,column=1)
        Haus.wohnflaeche=Entry(self.master)
        Haus.wohnflaeche.grid(row=4,column=1)
        Haus.zimmer=Entry(self.master)
        Haus.zimmer.grid(row=5,column=1)
        Haus.preis=Entry(self.master)
        Haus.preis.grid(row=6,column=1)
        Haus.grundstueckgroesse=Entry(self.master)
        Haus.grundstueckgroesse.grid(row=7,column=1)
        Haus.badezimmer=Entry(self.master)
        Haus.badezimmer.grid(row=8,column=1)
        Haus.heizart=Entry(self.master)
        Haus.heizart.grid(row=9,column=1)
        Haus.besitzer=Entry(self.master)
        Haus.besitzer.grid(row=10,column=1)

        self.button1=Button(self.master, text="Haus hinzufügen",fg="green",command=self.add_new_haus).place(x = 20, y= 300, width=100, height=25)
        self.button1=Button(self.master, text="Abbrechen",fg="red",command=self.quit).place(x = 370, y= 300, width=100, height=25)

    def quit(self):
        self.master.destroy()

    def add_new_haus(self):
        Main.new_haus_table_entry(Haus.farbe.get(), Haus.adresse.get(), Haus.baujahr.get(), Haus.wohnflaeche.get(), Haus.zimmer.get(), Haus.preis.get(), Haus.grundstueckgroesse.get(), Haus.badezimmer.get(), Haus.heizart.get(), Haus.besitzer.get())
        time.sleep(.1)

        NeuesHausWindow.quit(self)


class Haus():

    def __init__(self):
        self.farbe = farbe
        self.adresse = adresse
        self.baujahr = baujahr
        self.wohnflaeche = wohnflaeche
        self.zimmer = zimmer
        self.preis = preis
        self.grundstueckgroesse = grundstueckgroesse
        self.badezimmer = badezimmer
        self.heizart = heizart
        self.besitzer = besitzer

class Main():

    def connect():

        conn = sqlite3.connect("haeuser.db")  # db erstellen
        cur = conn.cursor()  # cursor = cur

        return conn, cur

    def main():
        conn, cur = Main.connect()
        cur.execute("CREATE TABLE IF NOT EXISTS HaeuserOne (Farbe text(20), Adresse BLOB, Baujahr INTEGER, Wohnflaeche REAL, Zimmer INTEGER, Preis REAL, Grundstueckgroesse REAL, Badezimmer INTEGER, Heizart TEXT, Besitzer TEXT)")
        # erstellt einen table in der datenbank haeuser.db und definiert die entrys und deren type

        master = Tk()
        mw = MainWindow(master)
        MainWindow.view_db()
        master.mainloop()

    def new_haus_table_entry(farbe, adresse, baujahr, wohnflaeche, zimmer, preis, grundstueckgroesse, badezimmer, heizart, besitzer): # jener funktions name :D
        conn, cur = Main.connect()
        cur.execute("INSERT INTO HaeuserOne VALUES(?, ?, ?, ? ,?, ?, ?, ?, ?, ?)", (farbe, adresse, baujahr, wohnflaeche, zimmer, preis, grundstueckgroesse, badezimmer, heizart, besitzer))

        # cur.execute("INSERT INTO HaeuserOne (%s) VALUES(?)" %(attr),
                                                     # (data,))
        # cursor.execute("INSERT INTO PRESSURE (" + city + ") values (?)", (pressure,))
        conn.commit()

if __name__ == "__main__":

    Main.main()
