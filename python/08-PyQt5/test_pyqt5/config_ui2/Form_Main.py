# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created: Tue May 07 16:37:40 2019
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

import os,sys
import copy
import codecs
import re
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtXml import *
from PyQt5 import QtCore,QtGui,QtXml
from Global import *
from xml.dom.minidom import Document
import configparser
from qtpy.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import configparser
from qtpy.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

import configparser
from qtpy.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import os


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtWidgets.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtWidgets.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(903, 620)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.casetree = QtWidgets.QTreeWidget(self.centralwidget)
        self.casetree.setGeometry(QtCore.QRect(0, 0, 411, 531))
        self.casetree.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.casetree.setColumnCount(1)
        self.casetree.setObjectName(_fromUtf8("casetree"))
        self.casetree.headerItem().setText(0, _fromUtf8("测试用例树"))
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(420, 0, 471, 251))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(170, 90, 81, 20))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.ip = QtWidgets.QLineEdit(self.groupBox)
        self.ip.setGeometry(QtCore.QRect(280, 90, 111, 20))
        self.ip.setObjectName(_fromUtf8("ip"))
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(10, 30, 81, 21))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_13 = QtWidgets.QLabel(self.groupBox)
        self.label_13.setGeometry(QtCore.QRect(10, 90, 61, 21))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.label_14 = QtWidgets.QLabel(self.groupBox)
        self.label_14.setGeometry(QtCore.QRect(10, 120, 71, 21))
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.product = QtWidgets.QComboBox(self.groupBox)
        self.product.setGeometry(QtCore.QRect(70, 30, 81, 22))
        self.product.setObjectName(_fromUtf8("product"))
        self.label_15 = QtWidgets.QLabel(self.groupBox)
        self.label_15.setGeometry(QtCore.QRect(10, 60, 41, 20))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.son_product = QtWidgets.QComboBox(self.groupBox)
        self.son_product.setGeometry(QtCore.QRect(70, 60, 81, 22))
        self.son_product.setObjectName(_fromUtf8("son_product"))
        self.username = QtWidgets.QLineEdit(self.groupBox)
        self.username.setGeometry(QtCore.QRect(280, 30, 111, 20))
        self.username.setObjectName(_fromUtf8("username"))
        self.label_17 = QtWidgets.QLabel(self.groupBox)
        self.label_17.setGeometry(QtCore.QRect(170, 30, 81, 20))
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_18 = QtWidgets.QLabel(self.groupBox)
        self.label_18.setGeometry(QtCore.QRect(170, 60, 81, 20))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.password = QtWidgets.QLineEdit(self.groupBox)
        self.password.setGeometry(QtCore.QRect(280, 60, 111, 20))
        self.password.setObjectName(_fromUtf8("password"))
        self.exceltoxml = QtWidgets.QPushButton(self.groupBox)
        self.exceltoxml.setGeometry(QtCore.QRect(170, 180, 61, 23))
        self.exceltoxml.setObjectName(_fromUtf8("exceltoxml"))
        self.py2xml = QtWidgets.QPushButton(self.groupBox)
        self.py2xml.setGeometry(QtCore.QRect(250, 180, 71, 23))
        self.py2xml.setObjectName(_fromUtf8("py2xml"))
        self.savecfg = QtWidgets.QPushButton(self.groupBox)
        self.savecfg.setGeometry(QtCore.QRect(330, 180, 71, 23))
        self.savecfg.setObjectName(_fromUtf8("savecfg"))
        self.sship = QtWidgets.QLineEdit(self.groupBox)
        self.sship.setGeometry(QtCore.QRect(70, 120, 81, 20))
        self.sship.setObjectName(_fromUtf8("sship"))
        self.com = QtWidgets.QLineEdit(self.groupBox)
        self.com.setGeometry(QtCore.QRect(70, 90, 81, 20))
        self.com.setObjectName(_fromUtf8("com"))
        self.testmode_checkBox = QtWidgets.QCheckBox(self.groupBox)
        self.testmode_checkBox.setGeometry(QtCore.QRect(10, 210, 71, 21))
        self.testmode_checkBox.setObjectName(_fromUtf8("testmode_checkBox"))
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(170, 150, 81, 20))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.error_num = QtWidgets.QLineEdit(self.groupBox)
        self.error_num.setGeometry(QtCore.QRect(280, 150, 111, 20))
        self.error_num.setObjectName(_fromUtf8("error_num"))
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(170, 120, 81, 20))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.client_sshIp = QtWidgets.QLineEdit(self.groupBox)
        self.client_sshIp.setGeometry(QtCore.QRect(280, 120, 111, 20))
        self.client_sshIp.setObjectName(_fromUtf8("client_sshIp"))
        self.label_11 = QtWidgets.QLabel(self.groupBox)
        self.label_11.setGeometry(QtCore.QRect(10, 150, 81, 20))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.loop_num = QtWidgets.QLineEdit(self.groupBox)
        self.loop_num.setGeometry(QtCore.QRect(90, 150, 61, 20))
        self.loop_num.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.loop_num.setObjectName(_fromUtf8("loop_num"))
        self.label_12 = QtWidgets.QLabel(self.groupBox)
        self.label_12.setGeometry(QtCore.QRect(10, 180, 41, 20))
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.BaudRate = QtWidgets.QComboBox(self.groupBox)
        self.BaudRate.setGeometry(QtCore.QRect(70, 180, 81, 22))
        self.BaudRate.setObjectName(_fromUtf8("BaudRate"))
        self.BaudRate.addItem(_fromUtf8(""))
        self.BaudRate.addItem(_fromUtf8(""))
        self.BaudRate.addItem(_fromUtf8(""))
        self.BaudRate.addItem(_fromUtf8(""))
        self.BaudRate.addItem(_fromUtf8(""))
        self.BaudRate.addItem(_fromUtf8(""))
        self.BaudRate.addItem(_fromUtf8(""))
        self.BaudRate.addItem(_fromUtf8(""))
        self.BaudRate.addItem(_fromUtf8(""))
        self.BaudRate.addItem(_fromUtf8(""))
        self.BaudRate.addItem(_fromUtf8(""))
        self.BaudRate.addItem(_fromUtf8(""))
        self.BaudRate.addItem(_fromUtf8(""))
        self.BaudRate.addItem(_fromUtf8(""))
        self.BaudRate.addItem(_fromUtf8(""))
        self.BaudRate.addItem(_fromUtf8(""))
        self.expand_button = QtWidgets.QPushButton(self.groupBox)
        self.expand_button.setGeometry(QtCore.QRect(170, 210, 61, 23))
        self.expand_button.setObjectName(_fromUtf8("expand_button"))
        self.testlog = QtWidgets.QTextEdit(self.centralwidget)
        self.testlog.setGeometry(QtCore.QRect(420, 270, 461, 261))
        self.testlog.setObjectName(_fromUtf8("testlog"))
        self.selectall = QtWidgets.QPushButton(self.centralwidget)
        self.selectall.setGeometry(QtCore.QRect(214, 550, 71, 23))
        self.selectall.setObjectName(_fromUtf8("selectall"))
        self.selectnone = QtWidgets.QPushButton(self.centralwidget)
        self.selectnone.setGeometry(QtCore.QRect(330, 550, 71, 23))
        self.selectnone.setObjectName(_fromUtf8("selectnone"))
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(10, 550, 81, 21))
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.sumtestcases = QtWidgets.QLabel(self.centralwidget)
        self.sumtestcases.setGeometry(QtCore.QRect(90, 550, 81, 21))
        self.sumtestcases.setText(_fromUtf8(""))
        self.sumtestcases.setObjectName(_fromUtf8("sumtestcases"))
        self.start_test = QtWidgets.QPushButton(self.centralwidget)
        self.start_test.setGeometry(QtCore.QRect(474, 550, 61, 23))
        self.start_test.setObjectName(_fromUtf8("start_test"))
        self.casetree.raise_()
        self.testlog.raise_()
        self.groupBox.raise_()
        self.selectall.raise_()
        self.selectnone.raise_()
        self.label_10.raise_()
        self.sumtestcases.raise_()
        self.start_test.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 903, 23))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_save = QtWidgets.QAction(MainWindow)
        self.action_save.setObjectName(_fromUtf8("action_save"))
        self.action_open = QtWidgets.QAction(MainWindow)
        self.action_open.setObjectName(_fromUtf8("action_open"))
        self.menu.addAction(self.action_save)
        self.menu.addAction(self.action_open)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.groupBox.setTitle(_translate("MainWindow", "基本配置", None))
        self.label_6.setText(_translate("MainWindow", "DUT 登陆地址", None))
        self.ip.setText(_translate("MainWindow", "192.168.0.1", None))
        self.label_9.setText(_translate("MainWindow", "产品类", None))
        self.label_13.setText(_translate("MainWindow", "产品COM", None))
        self.label_14.setText(_translate("MainWindow", "服务器IP", None))
        self.label_15.setText(_translate("MainWindow", "产品名", None))
        self.username.setText(_translate("MainWindow", "admin", None))
        self.label_17.setText(_translate("MainWindow", "DUT登陆用户名", None))
        self.label_18.setText(_translate("MainWindow", "DUT 登陆密码", None))
        self.password.setText(_translate("MainWindow", "admin", None))
        self.exceltoxml.setText(_translate("MainWindow", "用例转换", None))
        self.py2xml.setText(_translate("MainWindow", "创建配置", None))
        self.savecfg.setText(_translate("MainWindow", "保存配置", None))
        self.sship.setText(_translate("MainWindow", "192.168.20.2", None))
        self.com.setText(_translate("MainWindow", "COM1", None))
        self.testmode_checkBox.setText(_translate("MainWindow", "调试模式", None))
        self.label_8.setText(_translate("MainWindow", "允许异常次数", None))
        self.error_num.setText(_translate("MainWindow", "3", None))
        self.label_7.setText(_translate("MainWindow", "客户端IP地址", None))
        self.client_sshIp.setText(_translate("MainWindow", "192.168.0.1", None))
        self.label_11.setText(_translate("MainWindow", "模块循环次数", None))
        self.loop_num.setText(_translate("MainWindow", "1", None))
        self.label_12.setText(_translate("MainWindow", "波特率", None))
        self.BaudRate.setItemText(0, _translate("MainWindow", "115200", None))
        self.BaudRate.setItemText(1, _translate("MainWindow", "38400", None))
        self.BaudRate.setItemText(2, _translate("MainWindow", "110", None))
        self.BaudRate.setItemText(3, _translate("MainWindow", "300", None))
        self.BaudRate.setItemText(4, _translate("MainWindow", "600", None))
        self.BaudRate.setItemText(5, _translate("MainWindow", "1200", None))
        self.BaudRate.setItemText(6, _translate("MainWindow", "2400", None))
        self.BaudRate.setItemText(7, _translate("MainWindow", "4800", None))
        self.BaudRate.setItemText(8, _translate("MainWindow", "9600", None))
        self.BaudRate.setItemText(9, _translate("MainWindow", "14400", None))
        self.BaudRate.setItemText(10, _translate("MainWindow", "19200", None))
        self.BaudRate.setItemText(11, _translate("MainWindow", "57600", None))
        self.BaudRate.setItemText(12, _translate("MainWindow", "230400", None))
        self.BaudRate.setItemText(13, _translate("MainWindow", "380400", None))
        self.BaudRate.setItemText(14, _translate("MainWindow", "460800", None))
        self.BaudRate.setItemText(15, _translate("MainWindow", "921600", None))
        self.expand_button.setText(_translate("MainWindow", "扩展配置", None))
        self.selectall.setText(_translate("MainWindow", "全选", None))
        self.selectnone.setText(_translate("MainWindow", "全否", None))
        self.label_10.setText(_translate("MainWindow", "测试点总计:", None))
        self.start_test.setText(_translate("MainWindow", "开始测试", None))
        self.menu.setTitle(_translate("MainWindow", "文件", None))
        self.action_save.setText(_translate("MainWindow", "保存", None))
        self.action_open.setText(_translate("MainWindow", "打开", None))

