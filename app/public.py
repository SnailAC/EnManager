#!/usr/bin/python3
# -*-coding:utf-8-*-

# **********************************************************
# * Author        : SnailAC
# * Create time   : 2020-05-21 13:49:21
# * Last modified : 2020-05-21 15:02:03
# * Filename      : public.py
# * Description   :
# **********************************************************


from PyQt5.QtWidgets import (
    QFrame, QDialog, QLabel, QPushButton, QVBoxLayout, QHBoxLayout
)
from PyQt5.QtGui import QKeyEvent, QCursor, QPixmap
from PyQt5.QtCore import Qt


class MyFrame(QFrame):
    def __init__(self, parent=None):
        super(MyFrame, self).__init__()
        self.parent = parent
        self.enterFunc = None
        self.m_flag = False
        self.isMove = False

    def setEnterFunc(self, func):
        self._enterFunc = func

    def keyPressEvent(self, event):
        keyEvent = QKeyEvent(event)
        key = keyEvent.key()
        if key in (Qt.Key_Enter, Qt.Key_Return):
            if self.enterFunc:
                self.enterFunc()

    def mousePressEvent(self, event):
        """重写鼠标事件，实现窗口拖动。"""
        if not self.isMove:  # 实例可设置是否移动
            return

        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标

    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))


class WarningBox(QDialog, MyFrame):
    def __init__(self, parent=None, message=""):
        super(WarningBox, self).__init__()
        self.setObjectName("WarningBox")
        self.parent = parent
        self.message = message
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setModal(True)
        self.setFixedSize(526, 250)
        self.initUI()
        with open('resource/qss/public.qss', 'r', encoding='utf-8') as f:
            self.setStyleSheet(f.read())

        self.btn_ok.clicked.connect(self.accept)
        self.btn_no.clicked.connect(self.reject)

    def initUI(self):
        self.label_img = QLabel()
        self.label_img.setPixmap(QPixmap("resource/image/warning.png"))
        self.label_msg = QLabel(self.message)
        self.label_msg.setMinimumWidth(268)
        self.label_msg.setMaximumWidth(428)
        self.label_msg.adjustSize()
        self.label_msg.setWordWrap(True)
        self.label_msg.setScaledContents(True)
        self.label_msg.setAlignment(Qt.AlignTop)
        self.label_msg.setObjectName("label_msg")
        self.btn_ok = QPushButton("确定")
        self.btn_ok.setObjectName("btn_ok")
        self.btn_no = QPushButton("取消")
        self.btn_no.setObjectName("btn_no")
        # layout
        layout = QVBoxLayout(self)
        layout.setSpacing(30)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addStretch(1)

        info_lyt = QHBoxLayout()
        info_lyt.setSpacing(10)
        info_lyt.setContentsMargins(0, 0, 0, 0)
        info_lyt.addStretch(1)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.label_img)
        vbox.addStretch(1)
        info_lyt.addLayout(vbox)
        info_lyt.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.label_msg)
        vbox.addStretch(1)
        info_lyt.addLayout(vbox)
        info_lyt.addStretch(1)
        layout.addLayout(info_lyt)

        hbox = QHBoxLayout()
        hbox.setSpacing(20)
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.addStretch(1)
        hbox.addWidget(self.btn_ok)
        hbox.addWidget(self.btn_no)
        hbox.addStretch(1)
        layout.addLayout(hbox)
        layout.addStretch(1)


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    win = WarningBox(message='hello world')
    win.show()
    sys.exit(app.exec_())
