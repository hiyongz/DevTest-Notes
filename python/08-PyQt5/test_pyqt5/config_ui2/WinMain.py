#coding=utf-8
import os,sys
import copy
import codecs
import re
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtXml import *
from PyQt5 import QtCore,QtGui,QtXml
from Global import *
from Form_Main import Ui_MainWindow
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


#定义运行脚本的线程
class MainWindow(QMainWindow):
    def __init__(self,parent=None):
       # os.chdir(mainpath);
        # global kt,ks
        super(MainWindow,self).__init__(parent)
        # self.setWindowTitle("Main.exe")
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.open_config()
        # self.ui.connect(self.ui.savecfg, QtCore.SIGNAL("clicked()"), self.savecfg)
        # self.ui.savecfg.clicked.connect(self.savecfg(self))
        self.ui.savecfg.clicked.connect(self.savecfg)
    def open_config(self):
        global ConfigFile
        MainDir = 'E:/工作相关/pythonproj/Mesh_APP/'
        # 定义当前的日志目录
        ConfigFile = os.path.join(MainDir, "config.ini")
        init_dict = ParserCfg(ConfigFile)
        self.guidict=init_dict
        # print "self.config_dict",self.config_dict
        self.ui.loop_num.setText(self.guidict['num']['loopnum'])
        self.ui.error_num.setText(self.guidict['num']['error_num'])
        self.ui.ip.setText(self.guidict["dut"]["dip"])
        # self.ui.product.setText(self.guidict["dut"]["product"])
        # self.ui.son_product.setText(self.guidict['dut']['subprod'])
        self.ui.username.setText(self.guidict["dut"]["username"])
        self.ui.password.setText(self.guidict["dut"]["pwd"])
        self.ui.sship.setText(self.guidict["server"]["host"])
        self.ui.client_sshIp.setText(self.guidict["client"]["host"])
        self.ui.com.setText(self.guidict["km"]["com"])
        # self.ui.BaudRate.setText(self.guidict["km"]["baudrate"])
        self.mBWidget = ConfigMain()
    def savecfg(self,flag=True):
        self.c = ConfigMain()
        self.mBWidget.show()
        #先把以前的信息读取出来,然后保存成字典,然后把GUI上有的参数替换掉,没有的参数不操作
        global ConfigFile
        init_dict = ParserCfg(ConfigFile)
        guidict = {}
        guidict['num']={}
        guidict['kt']={}
        guidict['km']={}
        guidict['dut']={}
        guidict['server']={}
        guidict['client']={}
        cf = configparser.ConfigParser()
        guidict['num']['loopnum']=self.ui.loop_num.text()
        guidict['num']['error_num']=self.ui.error_num.text()
        guidict['dut']['dip'] = self.ui.ip.text()
        guidict['dut']['product'] = self.ui.product.currentText()
        guidict['dut']['subprod'] = self.ui.son_product.currentText()
        guidict['dut']['username']=self.ui.username.text()
        guidict['dut']['pwd'] = self.ui.password.text()
        guidict['server']['host'] = self.ui.sship.text()
        guidict['client']['host'] = self.ui.client_sshIp.text()
        guidict['km']['com'] = self.ui.com.text()
        guidict['km']['baudrate'] = self.ui.BaudRate.currentText()
        # for key,value in init_dict.iteritems():
        #     cf.add_section(key)
        #     for k,v in value.iteritems():
        #         if guidict.has_key(key):
        #             if guidict[key].has_key(k):
        #                 cf.set(key, k, guidict[key][k])
        #                 continue
        #         cf.set(key, k, v)
        # with open(ConfigFile.replace("\\","/"),"w+") as f:
        #     cf.write(f)
        self.config=ParserCfg(ConfigFile)
        print(self.config)
        # if flag:
        #     QMessageBox.information(self,"savecfg",u"保存配置成功",QMessageBox.Yes)
        #
        #
        #     self.workbook.Save()

class TableWidget(QTableWidget):
    def __init__(self, para,parent=None):
        QTableWidget.__init__(self, parent)
        self.para = para
        nRows = 0
        for k, v in self.para.items():
            nRows = len(v) + nRows
        nColumns = 3
        self.setRowCount(nRows)
        self.setColumnCount(nColumns)
        self.para_name = [[[],[]] for _ in range(nRows)]
        i = 0

        for k, v in self.para.items():
            self.setItem(i, 0, QTableWidgetItem(k))
            for k1, v1 in v.items():
                self.para_name[i][0] = k
                self.para_name[i][1] = k1
                self.setItem(i, 1, QTableWidgetItem(k1))
                self.setItem(i, 2, QTableWidgetItem(v1))
                i += 1
        self.cellChanged.connect(self.onCellChanged)
    @pyqtSlot(int, int)
    def onCellChanged(self, row, column):
        text = self.item(row, column).text()
        # number = str(text)
        self.para[self.para_name[row][0]][self.para_name[row][1]] = text

        # number = text
        # self.para.set_value(row, column, number)


class ConfigMain(QTableWidget):
    def __init__(self):
        super().__init__()
        self.initUI(self)
        # self.ui = self.MainWindow()
        # self.setupUi()
        # self.Ui_Form.setupUi(self)
    def initUI(self,Form):
        Form.setObjectName("Form")
        Form.resize(400, 800)
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.tableWidget.setObjectName("tableWidget")
        # self.tableWidget.setColumnCount(0)
        # self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        MainDir = 'E:/工作相关/pythonproj/Mesh_APP/'
        # 定义当前的日志目录
        ConfigFile = os.path.join(MainDir, "config.ini")
        self.para = ParserCfg(ConfigFile)
        self.tableWidget = TableWidget(self.para)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setHorizontalHeaderLabels(['','名称','值'])

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 6)
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 5, 1, 1)
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 4, 1, 1)
        self.pushButton_2.clicked.connect(self.print_my_df)
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)
        # self.initConfigUI(self)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_2.setText(_translate("Form", "确认"))
        self.pushButton.setText(_translate("Form", "取消"))

    @pyqtSlot()
    def print_my_df(self):
        headers = []
        for column in range(self.tableWidget.columnCount()):
            header = self.tableWidget.horizontalHeaderItem(column)
            if header is not None:
                headers.append(header.text())
            else:
                headers.append("Column " + str(column))

        for row in range(self.tableWidget.rowCount()):
            rowdata = []
            for column in range(self.tableWidget.columnCount()):
                item = self.tableWidget.item(row, column)
                if item is not None:
                    rowdata.append(item.text())
                else:
                    rowdata.append('')
            print(rowdata)
        aa = self.para["dut"]["dip"]
        # self.ui.mIP.setText(self.para["dut"]["dip"])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("./images/icon.png"))
    form = MainWindow()
    form.show()
    app.exec_()