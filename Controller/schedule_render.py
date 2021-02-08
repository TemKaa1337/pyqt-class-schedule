import json
from datetime import *


class SchedulerRender:
    def __init__(self, db):
        self.db = db

    def get_current_week_schedule(self):
        current_date = date.today()
        start_week = current_date - timedelta(current_date.weekday())
        end_week = current_date + timedelta(6 - current_date.weekday())
        
        self.db.cursor.execute('select * from current_schedule where date = ?', (start_week + '-' + end_week, ))
        data = self.db.cursor.fetchall()

        if not data:
            pass
        else:
            pass

        print(start_week, current_date, end_week)
