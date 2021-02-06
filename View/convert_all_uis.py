import os
from os.path import isfile, join

project_path = 'C:\\Users\\Admin\\Desktop\\MYPROJECTS\\pyqt-schedule'
ui_path = project_path + '\\View\\ui\\'
compiled = project_path + '\\View\\compiled\\'


def main():
    uis = [f for f in os.listdir(ui_path)]

    for file in uis:
        os.system('python -m PyQt5.uic.pyuic -x ' + ui_path + file + ' -o ' + compiled + file.split('.')[0] + '.py')


if __name__ == '__main__':
    main()