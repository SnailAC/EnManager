#!/usr/bin/python3
# -*-coding:utf-8-*-

# **********************************************************
# * Author        : SnailAC
# * Create time   : 2020-05-21 13:13:47
# * Last modified : 2020-05-21 13:13:47
# * Filename      : main.py
# * Description   :
# **********************************************************

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget
)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()


def main():
    """界面启动"""
    app = QApplication(sys.argv)
    myapp = MainWindow()
    myapp.show()
    sys.exit(app.exec_())
