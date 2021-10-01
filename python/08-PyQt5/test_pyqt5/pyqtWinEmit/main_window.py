# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(341, 179)
        Form.setMaximumSize(QtCore.QSize(341, 179))
        self.widget = QtGui.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(9, 20, 325, 131))
        self.widget.setObjectName(_fromUtf8("widget"))
        self.gridLayout = QtGui.QGridLayout(self.widget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.widget)
        self.label.setMinimumSize(QtCore.QSize(30, 20))
        self.label.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtGui.QLineEdit(self.widget)
        self.lineEdit.setMinimumSize(QtCore.QSize(122, 20))
        self.lineEdit.setMaximumSize(QtCore.QSize(122, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.widget)
        self.label_3.setMinimumSize(QtCore.QSize(30, 20))
        self.label_3.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.lineEdit_3 = QtGui.QLineEdit(self.widget)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(122, 20))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(122, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.gridLayout.addWidget(self.lineEdit_3, 0, 3, 1, 2)
        self.label_2 = QtGui.QLabel(self.widget)
        self.label_2.setMinimumSize(QtCore.QSize(30, 20))
        self.label_2.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lineEdit_2 = QtGui.QLineEdit(self.widget)
        self.lineEdit_2.setMinimumSize(QtCore.QSize(122, 20))
        self.lineEdit_2.setMaximumSize(QtCore.QSize(122, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.gridLayout.addWidget(self.lineEdit_2, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.widget)
        self.label_4.setMinimumSize(QtCore.QSize(30, 20))
        self.label_4.setMaximumSize(QtCore.QSize(30, 16777215))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 2, 1, 1)
        self.lineEdit_4 = QtGui.QLineEdit(self.widget)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(122, 20))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(122, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.gridLayout.addWidget(self.lineEdit_4, 1, 3, 1, 2)
        self.savecfg = QtGui.QPushButton(self.widget)
        self.savecfg.setMinimumSize(QtCore.QSize(78, 23))
        self.savecfg.setMaximumSize(QtCore.QSize(78, 16777215))
        self.savecfg.setObjectName(_fromUtf8("savecfg"))
        self.gridLayout.addWidget(self.savecfg, 2, 2, 1, 2)
        self.showcfg = QtGui.QPushButton(self.widget)
        self.showcfg.setMinimumSize(QtCore.QSize(75, 23))
        self.showcfg.setMaximumSize(QtCore.QSize(75, 16777215))
        self.showcfg.setObjectName(_fromUtf8("showcfg"))
        self.gridLayout.addWidget(self.showcfg, 2, 4, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.label.setText(_translate("Form", "para1", None))
        self.label_3.setText(_translate("Form", "para3", None))
        self.label_2.setText(_translate("Form", "para2", None))
        self.label_4.setText(_translate("Form", "para4", None))
        self.savecfg.setText(_translate("Form", "保存", None))
        self.showcfg.setText(_translate("Form", "参数", None))

