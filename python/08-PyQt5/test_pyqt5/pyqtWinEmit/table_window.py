# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table_window.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui  import QTableWidget
from PyQt4.QtGui  import QTableWidgetItem,QHeaderView
from funcs import ParserCfg
import ConfigParser
global ConfigFile
ConfigFile = 'D:/pythonproj/pyqtWinEmit/config.ini'

class TableWidget(QTableWidget):
    def __init__(self, para,parent=None):
        QTableWidget.__init__(self, parent)
        global ConfigFile
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
            # self.setItem(i, 0, QTableWidgetItem(k))
            item = QTableWidgetItem(k)
            # execute the line below to every item you need locked
            item.setFlags(QtCore.Qt.ItemIsEnabled)
            self.setItem(i, 0, item)
            for k1, v1 in v.items():
                self.para_name[i][0] = k
                self.para_name[i][1] = k1
                # self.setItem(i, 1, QTableWidgetItem(k1))
                item1 = QTableWidgetItem(k1)
                item1.setFlags(QtCore.Qt.ItemIsEnabled)
                self.setItem(i, 1, item1)
                # print "type v1",type(v1)
                # print "v1",v1
                self.setItem(i, 2, QTableWidgetItem(v1))
                i += 1
        self.cellChanged.connect(self.onCellChanged)
        # item = QTableWidgetItem(str(i*j))
        #         # item.setFlags( Qt.ItemIsSelectable |  Qt.ItemIsEnabled )
        #         # table.setItem(i, j, item)

    def onCellChanged(self, row, column):
        text = self.item(row, column).text()
        self.para[self.para_name[row][0]][self.para_name[row][1]] = str(text)

class Ui_Config(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        global ConfigFile
        self.resize(306, 385)
        self.gridLayout = QtGui.QGridLayout(self)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtGui.QPushButton(self)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 3, 1, 1)
        # self.tableView = QtGui.QTableView(self)
        # self.tableView.setObjectName("tableView")
        self.tableWidget = QtGui.QTableWidget(self)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)

        # MainDir = 'D:/SP_APP/'
        # 定义当前的日志目录
        # ConfigFile = os.path.join(MainDir, "config.ini")
        self.para = ParserCfg(ConfigFile)
        self.tableWidget = TableWidget(self.para)

        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) #pyqt5
        self.tableWidget.horizontalHeader().setResizeMode(QHeaderView.Stretch)  # pyqt4
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.setHorizontalHeaderLabels(['', u'名称', u'值'])
        # self.tableWidget.setHorizontalHeaderLabels(['', '名称', '值'])
        self.tableWidget.setAutoFillBackground(True)
        # self.setShowGrid(False)  # 设置显示格子线
        # self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers) # 设置禁止编辑

        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 4)
        self.pushButton = QtGui.QPushButton(self)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 2, 1, 1)
        self.pushButton_2.setText(u"取消")
        self.pushButton.setText(u"保存")
        self.connect(self.pushButton, QtCore.SIGNAL("clicked()"), self.transfer)
        self.connect(self.pushButton_2, QtCore.SIGNAL('clicked()'), self.close)
    def transfer(self):
        # 将参数更新到主窗口
        self.emit(QtCore.SIGNAL("transfer_father"), self.para)

