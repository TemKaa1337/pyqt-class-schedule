from PyQt5.QtWidgets import QPushButton, QWidget, QMessageBox
import sys
import json
from View.compiled.homework import Ui_HomeWorkForm


class ClassHomework(QWidget):
    def __init__(self, day_number, class_number, text, class_name, main_window):
        super().__init__()
        self.ui = Ui_HomeWorkForm()
        self.ui.setupUi(self)
        self.class_number = class_number
        self.day_number = day_number
        self.main = main_window
        self.class_name = class_name
        self.ui.homeworkArea.insertPlainText(text)
        self.ui.saveHWButton.clicked.connect(self.save_homework)
        self.ui.clearHWButton.clicked.connect(self.clear_area)

    def save_homework(self):
        self.save_task(self.ui.homeworkArea.toPlainText())
        QMessageBox.about(self, "", "Домашка сохранена!!!")

    def clear_area(self):
        self.ui.homeworkArea.setPlainText('')
        self.save_task('')
        QMessageBox.about(self, "", "Домашка очищена и сохранена!!!")

    def save_task(self, text):
        class_info = json.loads(self.main.class_info[self.day_number])
        classes_in_day = [f for f in class_info['class'].keys()]

        if self.class_number < len(classes_in_day):
            class_info['class'][classes_in_day[self.class_number]]['task'] = text
            self.main.class_info = list(self.main.class_info)
            self.main.class_info[self.day_number] = json.dumps(class_info)
            self.main.class_info = tuple(self.main.class_info)
            self.main.update_schedule()
