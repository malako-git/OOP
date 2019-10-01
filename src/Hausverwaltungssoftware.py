from db_controller import *

if __name__ == "__main__":

    controller = DB_Controller()

    master = Tk()
    MainWindow(master, controller)
    master.mainloop()
