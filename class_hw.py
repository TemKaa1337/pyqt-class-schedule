from PyQt5.QtWidgets import QPushButton, QWidget, QVBoxLayout, QLabel
import sys
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

        pass

    def clear_area(self):
        pass
