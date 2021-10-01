#coding=utf-8
import sys
from PyQt4 import QtCore, QtGui
# 子窗口
class W2(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle(u'子窗口')
        self.lineEdit = QtGui.QLineEdit()

        self.label1 = QtGui.QLabel(u"从父窗口接收")
        self.label2 = QtGui.QLabel(u"发送给父窗口")
        self.lineEdit1 = QtGui.QLineEdit()
        self.lineEdit2 = QtGui.QLineEdit()

        self.button2 = QtGui.QPushButton(u'发送', self)

        layout = QtGui.QGridLayout()
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)
        layout.addWidget(self.button2, 2, 1)

        self.setLayout(layout)
        self.button2.clicked.connect(self.transfer)

    def receive(self, s):
        print (u'接受到父窗口值')
        self.lineEdit1.setText(str(s))

    def transfer(self):
        str = self.lineEdit2.text()
        self.emit(QtCore.SIGNAL("transfer_father"), str)