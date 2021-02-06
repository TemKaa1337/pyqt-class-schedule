import xlrd


class ScheduleParser:
    schedule_path = 'C:\\Users\\Admin\\Desktop\\MYPROJECTS\\pyqt-class-schedule\\files\\scheduleGroup.xls'
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

    def __init__(self, schedule_path):
        if schedule_path is not None:
            self.schedule_path = schedule_path

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
        self.schedule[self.current_day] = {'time': [], 'class': []}
        self.schedule[self.current_day]['time'] = [row_info[1].value]
        self.schedule[self.current_day]['class'] = [row_info[2].value.split('\n')[0]]

    def get_schedule(self):
        return self.schedule


if __name__ == '__main__':
    parser = ScheduleParser()
    parser.parse_schedule()
    print(parser.get_schedule())
