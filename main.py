import json
import sys
from PyQt5 import QtWidgets
from View.compiled.schedule import Ui_Schedule
from Controller.schedule_render import SchedulerRender
from database.db import Database


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
        self.render_controller = SchedulerRender(self.db)
        self.class_info = self.render_controller.get_week_schedule()[0]

        for i in range(28):
            property = getattr(self.ui, self.day_translation[i // 4] + 'CheckBox_' + str(i % 4 + 1))
            property.stateChanged.connect(self.check_state_changed)

    def check_state_changed(self, widget):
        print(widget.property('day_number'))
        # print(self.sender().dynamicPropertyNames()[0].ToString())
        # print(self.sender().dynamicPropertyNames().day_number, self.sender().dynamicPropertyNames().class_number)

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

                if i >= len(classes):
                    text = ''
                    time = ''
                    check = False
                else:
                    text = classes[i]
                    time = info['time'][i]
                    check = info['class'][classes[i]]['checked']

                class_button.setText(text)
                time_label.setText(time)
                check_box.setChecked(check)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    application = ApplicationWindow()
    application.render()
    application.show()
    sys.exit(app.exec_())
