import json
from .db import Database


class DatabaseSeeder:
    def __init__(self, schedule):
        self.schedule = schedule
        self.db = Database()

    def seed(self):
        query = tuple()

        for day in self.schedule:
            query += (json.dumps({'time': self.schedule[day]['time'], 'class': self.schedule[day]['class']}), )

        self.db.cursor.execute("insert into default_schedule (monday, tuesday, wednesday, thursday, friday, saturday, sunday) values (?, ?, ?, ?, ?, ?, ?);", query)
        self.db.connection.commit()
