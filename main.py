import sys
from PyQt5 import QtWidgets
from View.compiled.schedule import Ui_Schedule
from Controller.schedule_render import SchedulerRender
from database.db import Database


class ApplicationWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_Schedule()
        self.ui.setupUi(self)


def main():
    db = Database()
    render = SchedulerRender(db)
    res = render.get_current_week_schedule()
    # app = QtWidgets.QApplication(sys.argv)
    # application = ApplicationWindow()
    # application.show()
    # sys.exit(app.exec_())


if __name__ == "__main__":
    main()
