#!/usr/bin/python3
# -*-coding:utf-8-*-

# **********************************************************
# * Author        : SnailCL
# * Create time   : 2020-05-21 13:43:58
# * Last modified : 2020-05-21 13:43:58
# * Filename      : task.py
# * Description   :
# **********************************************************

from PyQt5.QtWidgets import (
    QFrame
)

from app.constant import CONFIG_DICT


class Task(QFrame):
    def __init__(self, parent=None):
        super(Task, self).__init__()
        self.parent = parent

        print('Task', CONFIG_DICT)

        self.initUI()

    def initUI(self):
        pass


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    win = Task()
    win.show()
    sys.exit(app.exec_())
