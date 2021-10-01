# -*- coding: utf-8 -*-
"""
说明
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from main_window import Ui_MainWindow
from table_window import *
import ConfigParser
from funcs import ParserCfg
import os,sys
global ConfigFile
ConfigFile = 'D:/pythonproj/pyqtWinEmit/config.ini'
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        global ConfigFile
        # self.setWindowTitle("Main")
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.read_config(ConfigFile)

        # 添加测试用例的响应事件
        self.connect(self.ui.savecfg, QtCore.SIGNAL("clicked()"), self.savecfg)
        self.connect(self.ui.showcfg, QtCore.SIGNAL("clicked()"), self.showcfg)
        self.start_flag = 0

    def read_config(self,ConfigFile):
        init_dict = ParserCfg(ConfigFile)
        self.guidict=init_dict
        # print "self.config_dict",self.config_dict
        self.ui.lineEdit.setText(self.guidict['A']['para1'])
        self.ui.lineEdit_2.setText(self.guidict['B']['para2'])
        self.ui.lineEdit_3.setText(self.guidict["C"]["para3"])
        self.ui.lineEdit_4.setText(self.guidict["D"]["para4"])
    def savecfg(self,flag=True):
        global G_MainDict
        global ConfigFile
        #先把以前的信息读取出来,然后保存成字典,然后把GUI上有的参数替换掉,没有的参数不操作
        init_dict = ParserCfg(ConfigFile)
        guidict = {}
        cf = ConfigParser.ConfigParser()

        self.guidict['A']['para1']=unicode(self.ui.lineEdit.text())
        self.guidict['B']['para2']=unicode(self.ui.lineEdit_2.text())
        self.guidict['C']['para3'] = unicode(self.ui.lineEdit_3.text())
        self.guidict['D']['para4'] = unicode(self.ui.lineEdit_4.text())
        for key,value in init_dict.iteritems():
            cf.add_section(key)
            for k,v in value.iteritems():
                if guidict.has_key(key):
                    if guidict[key].has_key(k):
                        cf.set(key, k, guidict[key][k])
                        continue
                cf.set(key, k, v)
        with open(ConfigFile.replace("\\","/"),"w+") as f:
            cf.write(f)

        if flag:
            QMessageBox.information(self,"savecfg",u"保存配置成功",QMessageBox.Yes)
        G_MainDict = ParserCfg(ConfigFile)

    def showcfg(self):
        ## 扩展配置窗口

        self.confui = Ui_Config()
        self.connect(self.confui, QtCore.SIGNAL("transfer_father"), self.receive)
        self.confui.show()

    @QtCore.pyqtSlot(str)
    def receive(self, para):
        global G_MainDict
        global ConfigFile
        G_MainDict = para
        self.ui.lineEdit.setText(para['A']['para1'])
        self.ui.lineEdit_2.setText(para['B']['para2'])
        self.ui.lineEdit_3.setText(para["C"]["para3"])
        self.ui.lineEdit_4.setText(para["D"]["para4"])
        # self.lineEdit1.setText(str(s))
        ############ 保存更新后的配置参数 ###############
        init_dict = ParserCfg(ConfigFile)
        cf = ConfigParser.ConfigParser()
        for key,value in init_dict.iteritems():
            cf.add_section(key)
            for k,v in value.iteritems():
                if para.has_key(key):
                    if para[key].has_key(k):
                        cf.set(key, k, para[key][k])
                        continue
                cf.set(key, k, v)
        with open(ConfigFile.replace("\\","/"),"w+") as f:
            cf.write(f)
        self.config = ParserCfg(ConfigFile)
        self.confui.close()
        QMessageBox.information(self,"savecfg",u"保存配置成功",QMessageBox.Yes)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    # app.setWindowIcon(QIcon("./images/icon.png"))
    form = MainWindow()
    form.show()
    app.exec_()