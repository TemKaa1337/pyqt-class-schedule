import xlrd
import os
import sys


class ScheduleParser:
    days_translations = {
        'ПН': 'monday',
        'ВТ': 'tuesday',
        'СР': 'wednesday',
        'ЧТ': 'thursday',
        'ПТ': 'friday',
        'СБ': 'saturday',
        'ВС': 'sunday',
    }
    schedule = {
        'monday': {
            'time': [],
            'class': []
        },
        'tuesday': {
            'time': [],
            'class': []
        },
        'wednesday': {
            'time': [],
            'class': []
        },
        'thursday': {
            'time': [],
            'class': []
        },
        'friday': {
            'time': [],
            'class': []
        },
        'saturday': {
            'time': [],
            'class': []
        },
        'sunday': {
            'time': [],
            'class': []
        },
    }
    current_day = ''

    def __init__(self):
        self.schedule_path = os.path.join(os.path.dirname(__file__), '../files/scheduleGroup.xls')

    def parse_schedule(self):
        skip_row = True
        book = xlrd.open_workbook(self.schedule_path)
        sheet = book.sheet_by_index(0)

        for rx in range(sheet.nrows):
            if skip_row:
                if sheet.row(rx)[0].value == 'ПН':
                    skip_row = False
                    self.current_day = self.days_translations[sheet.row(rx)[0].value]
            else:
                if sheet.row(rx)[0].value != '':
                    self.current_day = self.days_translations[sheet.row(rx)[0].value]

            if not skip_row and sheet.row(rx)[1].value != '':
                self.add_classes_info(sheet.row(rx))

    def add_classes_info(self, row_info):
        self.schedule[self.current_day]['time'].append(row_info[1].value)
        self.schedule[self.current_day]['class'].append(row_info[2].value.split('\n')[0])

    def get_schedule(self):
        return self.schedule

