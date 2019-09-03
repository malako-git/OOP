from tkinter import *
import sqlite3
from sqlite3 import Error
import time
# pass


class MainWindow():

    def __init__(self, master):
        self.master = master
        self.master.geometry("1000x700+200+200")
        self.master.title("Hausverwaltungs Software")

        self.button1 = Button(self.master, text="Neues Haus", fg="black",command=self.new_haus_window).place(x =10, y=20, width=120,height=30)
        self.button2 = Button(self.master, text="Bearbeiten", fg="orange",command=self.edit_haus_window).place(x =270, y=20, width=120,height=30)
        self.button3 = Button(self.master, text="Quit", bg="#38778f" ,fg="red",command=self.quit).place(x =870, y=20, width=120,height=30)
        self.button4 = Button(self.master, text="Datenbank", fg="blue",command=self.show_db).place(x =140, y=20, width=120,height=30)
        self.button5 = Button(self.master, text="Löschen", fg="red",command=self.delete).place(x =400, y=20, width=120,height=30)
        self.id = Entry(master)
        self.id.place(x=610,y=25,width=40,height=20)
        self.label_id = Label(master, text="Haus ID:",fg="black").place(x=530,y=25,width=70,height=20)



    def new_haus_window(self):
        master2=Toplevel(self.master)
        nhwGUI=NeuesHausWindow(master2)

    def edit_haus_window(self):
        new_id = self.id.get()
        master3=Toplevel(self.master)
        ehwGUI=EditHausWindow(master3, new_id)


    def show_db(self):
        conn = sqlite3.connect("haeuser.db", timeout=2)  # db erstellen und connecten
        cur = conn.cursor() # cursor erstellen

        cur.execute("SELECT *, oid FROM HaeuserOne")
        haeuser_in_db = cur.fetchall()

        # print(haeuser_in_db)

        print_db = ""
        for haeuser in haeuser_in_db:
            print_db += str(haeuser[10])+ " "+"\t"+ str(haeuser[1])+ " // "+ str(haeuser[9])+"\n"

        show_db_label = Label(self.master, text=print_db)
        show_db_label.place(x=400,y=350)

        db.conn.commit()


    def delete(self):
        conn = sqlite3.connect("haeuser.db", timeout=2)  # db erstellen und connecten
        cur = conn.cursor() # cursor erstellen
        print("lösche eintrag @ oid " + self.id.get())
        try:
            cur.execute("DELETE from HaeuserOne WHERE oid = " + self.id.get())
            conn.commit()
        except Error:
            print("User Error !!!")

    def quit(self):
        self.master.destroy()


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

        #self.label2=Label(self.master, text="",fg="black").grid(row=1,column=0)
        #self.label2=Label(self.master, text="",fg="black").grid(row=2,column=2)
        #self.label2=Label(self.master, text="",fg="black").grid(row=3,column=2)
        self.label2=Label(self.master, text="in m²",fg="black").grid(row=4,column=2)
        #self.label2=Label(self.master, text="",fg="black").grid(row=5,column=2)
        self.label2=Label(self.master, text="in €",fg="black").grid(row=6,column=2)
        self.label2=Label(self.master, text="in m²",fg="black").grid(row=7,column=2)
        #self.label2=Label(self.master, text="",fg="black").grid(row=8,column=2)
        #self.label2=Label(self.master, text="",fg="black").grid(row=9,column=2)
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

class EditHausWindow():

    def __init__(self, master, id):

        conn = sqlite3.connect("haeuser.db", timeout=2)  # db erstellen und connecten
        cur = conn.cursor() # cursor erstellen

        self.master=master
        self.id = id
        self.master.geometry("500x350+300+350")
        self.master.title("Haus bearbeiten")

        self.label1=Label(self.master, text="Bearbeiten sie ein Haus aus der Datenbank",fg="black").grid(row=0,column=1)
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

        #self.label2=Label(self.master, text="",fg="black").grid(row=1,column=0)
        #self.label2=Label(self.master, text="",fg="black").grid(row=2,column=2)
        #self.label2=Label(self.master, text="",fg="black").grid(row=3,column=2)
        self.label2=Label(self.master, text="in m²",fg="black").grid(row=4,column=2)
        #self.label2=Label(self.master, text="",fg="black").grid(row=5,column=2)
        self.label2=Label(self.master, text="in €",fg="black").grid(row=6,column=2)
        self.label2=Label(self.master, text="in m²",fg="black").grid(row=7,column=2)
        #self.label2=Label(self.master, text="",fg="black").grid(row=8,column=2)
        #self.label2=Label(self.master, text="",fg="black").grid(row=9,column=2)
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


        cur.execute("SELECT * FROM HaeuserOne WHERE oid = " + self.id)
        haeuser = cur.fetchall()

        for haus in haeuser:
            Haus.farbe.insert(0, haus[0])
            Haus.adresse.insert(0, haus[1])
            Haus.baujahr.insert(0, haus[2])
            Haus.wohnflaeche.insert(0, haus[3])
            Haus.zimmer.insert(0, haus[4])
            Haus.preis.insert(0, haus[5])
            Haus.grundstueckgroesse.insert(0, haus[6])
            Haus.badezimmer.insert(0, haus[7])
            Haus.heizart.insert(0, haus[8])
            Haus.besitzer.insert(0, haus[9])

        self.button1=Button(self.master, text="Haus speichern",fg="green",command=self.edit_haus).place(x = 20, y= 300, width=100, height=25)
        self.button1=Button(self.master, text="Abbrechen",fg="red",command=self.quit).place(x = 370, y= 300, width=100, height=25)

    def quit(self):
        self.master.destroy()

    def edit_haus(self):
        Main.edit_haus_table_entry(Haus.farbe.get(), Haus.adresse.get(), Haus.baujahr.get(), Haus.wohnflaeche.get(), Haus.zimmer.get(), Haus.preis.get(), Haus.grundstueckgroesse.get(), Haus.badezimmer.get(), Haus.heizart.get(), Haus.besitzer.get(), self.id.get())
        time.sleep(.2)
        quit()



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

class db():
    print("conn to db open")
    conn = sqlite3.connect("haeuser.db", timeout=2)  # db erstellen und connecten
    cur = conn.cursor() # cursor erstellen

class Main():

    def __init__(self, id):

        self.id = id

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



        mw = MainWindow(master)
        master.mainloop()




    def new_haus_table_entry(farbe, adresse, baujahr, wohnflaeche, zimmer, preis, grundstueckgroesse, badezimmer, heizart, besitzer):

        db.cur.execute("INSERT INTO HaeuserOne VALUES(?, ?, ?, ? ,?, ?, ?, ?, ?, ?)", (farbe, adresse, baujahr, wohnflaeche, zimmer, preis, grundstueckgroesse, badezimmer, heizart, besitzer))
        # cur.execute("INSERT INTO HaeuserOne (%s) VALUES(?)" %(attr),(data,))
        # cursor.execute("INSERT INTO PRESSURE (" + city + ") values (?)", (pressure,))
        db.conn.commit()
        # db.conn.close()

    def edit_haus_table_entry(farbe, adresse, baujahr, wohnflaeche, zimmer, preis, grundstueckgroesse, badezimmer, heizart, besitzer, id):

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

            WHERE oid = :oid"""
            {"farbe": farbe,
            "Adresse": adresse,



            }




            )



        db.conn.commit()


if __name__ == "__main__":

    Main.main()
