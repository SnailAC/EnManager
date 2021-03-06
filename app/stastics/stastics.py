#!/usr/bin/python3
# -*-coding:utf-8-*-

# **********************************************************
# * Author        : SnailCL
# * Create time   : 2020-05-21 13:19:28
# * Last modified : 2020-05-21 13:23:30
# * Filename      : stastics.py
# * Description   :
# **********************************************************

from PyQt5.QtWidgets import (
    QFrame
)

from app.constant import CONFIG_DICT


class Stastics(QFrame):
    def __init__(self, parent=None):
        super(Stastics, self).__init__()
        self.parent = parent
        print('Stastics', CONFIG_DICT)

        self.initUI()

    def initUI(self):
        pass


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    win = Stastics()
    win.show()
    sys.exit(app.exec_())
