import datetime
import sqlite3
import pandas as pd


class Database:
    def __init__(self, db_file):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def get_text(self):
        with self.connection:
            result = self.cursor.execute(f"SELECT text FROM music ORDER BY id DESC ").fetchall()
        return result


# db = Database('database.db')
# print(db.get_text()[0][0])