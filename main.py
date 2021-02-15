import json
import sys
from datetime import *
from PyQt5 import QtWidgets
from View.compiled.schedule import Ui_Schedule
from Controller.schedule_render import SchedulerRender
from database.db import Database
from class_hw import ClassHomework
from initialize import InitializeProject


class ApplicationWindow(QtWidgets.QMainWindow):
    day_translation = [
        'monday',
        'tuesday',
        'wednesday',
        'thursday',
        'friday',
        'saturday',
        'sunday'
    ]

    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.db = Database()
        self.ui = Ui_Schedule()
        self.ui.setupUi(self)
        self.check_for_first_exec()
        self.ui.prevWeekButton.clicked.connect(self.render_prev_week)
        self.ui.nextWeekButton.clicked.connect(self.render_next_week)
        self.render_controller = SchedulerRender(self.db)
        self.class_info = self.render_controller.get_week_schedule()[0]

        for i in range(28):
            day_number = i // 4
            class_number = i % 4 + 1

            property = getattr(self.ui, self.day_translation[day_number] + 'CheckBox_' + str(class_number))
            property.stateChanged.connect(self.check_state_changed)

            property = getattr(self.ui, self.day_translation[day_number] + 'ClassButton_' + str(class_number))
            property.clicked.connect(self.class_clicked)

    def check_for_first_exec(self):
        try:
            self.db.cursor.execute('select * from default_schedule;');
        except:
            init = InitializeProject()
            init.initialize()


    def render_prev_week(self):
        new_date = datetime.strptime(self.render_controller.current_week.split('-')[0], '%d.%m.%Y') - timedelta(7)
        self.class_info = self.render_controller.get_week_schedule(new_date)[0]
        self.render()
        pass

    def render_next_week(self):
        new_date = datetime.strptime(self.render_controller.current_week.split('-')[0], '%d.%m.%Y') + timedelta(7)
        self.class_info = self.render_controller.get_week_schedule(new_date)[0]
        self.render()
        pass

    def check_state_changed(self, widget):
        check_box = self.sender()
        day_number = check_box.property('day_number')
        class_number = check_box.property('class_number')

        class_info = json.loads(self.class_info[day_number])
        classes_in_day = [f for f in class_info['class'].keys()]

        if class_number < len(classes_in_day):
            class_info['class'][classes_in_day[class_number]]['checked'] = check_box.isChecked()
            self.class_info = list(self.class_info)
            self.class_info[day_number] = json.dumps(class_info)
            self.class_info = tuple(self.class_info)
            self.update_schedule()

    def class_clicked(self):
        button = self.sender()
        day_number = button.property('day_number')
        class_number = button.property('class_number')

        class_info = json.loads(self.class_info[day_number])
        classes_in_day = [f for f in class_info['class'].keys()]

        if classes_in_day and class_number < len(classes_in_day):
            self.class_hw = ClassHomework(day_number, class_number, class_info['class'][classes_in_day[class_number]]['task'], classes_in_day[class_number], self)
            self.class_hw.show()

    def update_schedule(self):
        self.db.cursor.execute("""
        INSERT INTO current_schedule (
            date, 
            monday, 
            tuesday, 
            wednesday, 
            thursday, 
            friday, 
            saturday, 
            sunday
        ) VALUES(?, ?, ?, ?, ?, ?, ?, ?) ON CONFLICT(date) DO UPDATE SET
            monday=excluded.monday,
            tuesday=excluded.tuesday,
            wednesday=excluded.wednesday,
            thursday=excluded.thursday,
            friday=excluded.friday,
            saturday=excluded.saturday, 
            sunday=excluded.sunday
        ;""", (self.render_controller.current_week,) + self.class_info)
        self.db.connection.commit()
        pass

    def render(self):
        class_length = len(self.class_info)

        for day_number in range(class_length):
            info = json.loads(self.class_info[day_number])
            label = getattr(self.ui, self.day_translation[day_number] + 'DateLabel')
            label.setText(self.render_controller.week_days[day_number])
            classes = [key for key in info['class'].keys()]

            for i in range(4):
                class_button = getattr(self.ui, self.day_translation[day_number] + 'ClassButton_' + str(i + 1))
                check_box = getattr(self.ui, self.day_translation[day_number] + 'CheckBox_' + str(i + 1))
                time_label = getattr(self.ui, self.day_translation[day_number] + 'TimeLabel_' + str(i + 1))

                if i < len(classes):
                    text = classes[i]
                    time = info['time'][i]
                    check = info['class'][classes[i]]['checked']
                else:
                    text = ''
                    time = ''
                    check = False

                class_button.setText(text)
                time_label.setText(time)
                check_box.setChecked(check)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.render()
    application.show()
    sys.exit(app.exec_())
