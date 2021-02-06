import sqlite3


class Database:
    def __init__(self):
        self.connection = sqlite3.connect('C:\\Users\\Admin\\Desktop\\MYPROJECTS\\pyqt-class-schedule\\database\\db.db')
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()
