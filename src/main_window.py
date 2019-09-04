import sqlite3
from tkinter import *

from edit_haus_window import *
from neues_haus_window import *
from db import *


class MainWindow():

    def __init__(self, master):
        self.master = master
        self.master.geometry("1000x700+200+200")
        self.master.title("Hausverwaltungs Software")

        self.button1 = Button(self.master, text="Neues Haus", fg="black", command=self.new_haus_window).place(x=10,
                                                                                                              y=20,
                                                                                                              width=120,
                                                                                                              height=30)
        self.button2 = Button(self.master, text="Bearbeiten", fg="orange", command=self.edit_haus_window).place(x=270,
                                                                                                                y=20,
                                                                                                                width=120,
                                                                                                                height=30)
        self.button3 = Button(self.master, text="Quit", bg="#38778f", fg="red", command=self.quit).place(x=870, y=20,
                                                                                                         width=120,
                                                                                                         height=30)
        self.button4 = Button(self.master, text="Datenbank", fg="blue", command=self.show_db).place(x=140, y=20,
                                                                                                    width=120,
                                                                                                    height=30)
        self.button5 = Button(self.master, text="Löschen", fg="red", command=self.delete).place(x=400, y=20, width=120,
                                                                                                height=30)
        self.id = Entry(master)
        self.id.place(x=610, y=25, width=40, height=20)
        self.label_id = Label(master, text="Haus ID:", fg="black").place(x=530, y=25, width=70, height=20)

    def new_haus_window(self):
        master2 = Toplevel(self.master)
        nhwGUI = NeuesHausWindow(master2)

    def edit_haus_window(self):
        from edit_haus_window import EditHausWindow
        new_id = self.id.get()
        master3 = Toplevel(self.master)
        ehwGUI = EditHausWindow(master3, new_id)

    def show_db(self):
        conn = sqlite3.connect("haeuser.db", timeout=2)  # db erstellen und connecten
        cur = conn.cursor()  # cursor erstellen

        cur.execute("SELECT *, oid FROM HaeuserOne")
        haeuser_in_db = cur.fetchall()

        # print(haeuser_in_db)

        print_db = ""

        for haeuser in haeuser_in_db:
            print_db += str(haeuser[10]) + " " + "\t" + str(haeuser[1]) + " // " + str(haeuser[9]) + "\n"

        show_db_label = Label(self.master, text=print_db)
        show_db_label.place(x=400, y=350)

        db.conn.commit()

    def delete(self):
        conn = sqlite3.connect("haeuser.db", timeout=2)  # db erstellen und connecten
        cur = conn.cursor()  # cursor erstellen
        print("lösche eintrag @ oid " + self.id.get())
        try:
            cur.execute("DELETE from HaeuserOne WHERE oid = " + self.id.get())
            conn.commit()
        except Error:
            print("User Error !!!")

    def quit(self):
        self.master.destroy()
