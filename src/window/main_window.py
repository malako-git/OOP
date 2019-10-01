from sqlite3 import OperationalError
from window.edit_haus_window import EditHausWindow
from window.neues_haus_window import *


class MainWindow:

    def __init__(self, master, db):
        self.db = db
        self.master = master
        self.master.geometry("1000x700+200+200")
        self.master.title("Hausverwaltungs Software")

        self.button1 = Button(self.master, text="Neues Haus", fg="black", command=self.new_haus_window).place(x=10, y=20, width=120, height=30)
        self.button2 = Button(self.master, text="Bearbeiten", fg="orange", command=self.edit_haus_window).place(x=270, y=20, width=120, height=30)
        self.button3 = Button(self.master, text="Quit", bg="#38778f", fg="red", command=self.quit).place(x=870, y=20, width=120, height=30)
        self.button4 = Button(self.master, text="Datenbank", fg="blue", command=self.refresh_db).place(x=140, y=20, width=120, height=30)
        self.button5 = Button(self.master, text="Löschen", fg="red", command=self.delete).place(x=400, y=20, width=120, height=30)
        self.id = Entry(master)
        self.id.place(x=610, y=25, width=40, height=20)
        self.label_id = Label(master, text="Haus ID:", fg="black").place(x=530, y=25, width=70, height=20)
        self.refresh_db()

    def new_haus_window(self):
        haus = Haus()
        master2 = Toplevel(self.master)
        NeuesHausWindow(master2, self.db, haus)

    def edit_haus_window(self):
        haus = Haus()
        try:
            haus.fillEntitiy(self.db.getHaus(self.id.get()))
            master3 = Toplevel(self.master)
            EditHausWindow(master3, self.db, haus, self.id.get())
        except OperationalError as e:
            print("Sqlite operational error: {}!".format(e))

    def refresh_db(self):
        print_db = self.db.show_db()
        show_db_label_category = Label(self.master, text="Besitzer"+ " " + "\t" + "Farbe" + " // " + "Heizart")
        show_db_label = Label(self.master, text=print_db)
        show_db_label_category.place(x=400, y=300)
        show_db_label.place(x=400, y=350)

    def delete(self):
        self.db.delete(self.id.get())

    def quit(self):
        self.master.destroy()
