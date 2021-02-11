import json
from datetime import *


class SchedulerRender:
    week_days = []

    def __init__(self, db):
        self.db = db

    def get_week_schedule(self, render_date=date.today()):
        def set_week_days(date):
            for i in range(7):
                self.week_days.append(str((date - timedelta(date.weekday() - i)).strftime('%d.%m')))

        set_week_days(render_date)

        # date format Y-m-d-Y-m-d
        self.db.cursor.execute('select monday, tuesday, wednesday, thursday, friday, saturday, sunday from current_schedule where date = ?', (self.week_days[0] + '-' + self.week_days[len(self.week_days) - 1],))
        data = self.db.cursor.fetchall()

        if not data:
            self.db.cursor.execute('select monday, tuesday, wednesday, thursday, friday, saturday, sunday from default_schedule')
            data = self.db.cursor.fetchall()

        return data
