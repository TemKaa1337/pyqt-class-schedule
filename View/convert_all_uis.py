import os
from os.path import isfile, join

project_path = 'C:\\Users\\Admin\\Desktop\\MYPROJECTS\\pyqt-schedule'
ui_path = project_path + '\\View\\ui\\'
compiled = project_path + '\\View\\compiled\\'


def main():
    uis = [f for f in os.listdir(os.path.abspath('ui'))]

    for file in uis:
        os.system('python -m PyQt5.uic.pyuic -x ' + os.path.abspath('ui') + '/' + file + ' -o ' + os.path.abspath('compiled') + '/' + file.split('.')[0] + '.py')


if __name__ == '__main__':
    main()
