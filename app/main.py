#!/usr/bin/python3
# -*-coding:utf-8-*-

# **********************************************************
# * Author        : SnailCL
# * Create time   : 2020-05-21 13:13:47
# * Last modified : 2020-05-21 14:55:06
# * Filename      : main.py
# * Description   :
# **********************************************************

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QStackedWidget, QVBoxLayout
)

from app.stastics.stastics import Stastics
from app.task.task import Task


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.stack = QStackedWidget(self)

        self.frame_stastics = Stastics(self)
        self.stack.addWidget(self.frame_stastics)

        self.frame_task = Task(self)
        self.stack.addWidget(self.frame_task)

        main_lyt = QVBoxLayout(self)
        main_lyt.addWidget(self.stack)


def main():
    """界面启动"""
    app = QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
