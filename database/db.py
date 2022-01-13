import sqlite3
import os
import sys


class Database:
    def __init__(self):
        self.connection = sqlite3.connect(os.path.join(os.path.dirname(__file__), 'db.db'))
        self.cursor = self.connection.cursor()
