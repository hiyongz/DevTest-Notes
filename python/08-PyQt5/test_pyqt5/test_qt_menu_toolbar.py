#!/usr/bin/python3
#-*- coding:utf-8 -*-
'''
ZetCode PyQt5 tutorial
菜单栏和工具栏
'''
import sys
from PyQt5.QtWidgets import QMainWindow, QTextEdit, QAction, QApplication
from PyQt5.QtWidgets import qApp,QMenu
from PyQt5.QtGui import QIcon

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        textEdit = QTextEdit()
        self.setCentralWidget(textEdit) # 创建了一个文本编辑区域

        ################ 状态栏 ################
        self.statusBar().showMessage('Ready')# 创建状态栏,在状态栏上显示一条信息
        ################ 菜单栏 ################
        exitAct = QAction(QIcon('exit.png'), '&Exit', self)# QAction是菜单栏、工具栏或者快捷键的动作的组合
        exitAct.setShortcut('Ctrl+Q')
        exitAct.setStatusTip('Exit application')# 创建一个状态栏，当鼠标悬停在菜单栏时显示当前状态
        exitAct.triggered.connect(qApp.quit)

        # self.statusBar()
        menubar = self.menuBar() # 创建菜单栏
        fileMenu = menubar.addMenu('&File')# 添加了一个file菜单
        fileMenu.addAction(exitAct)# 关联点击退出应用的事件
        ################ 子菜单 ################
        impMenu = QMenu('Import', self) # QMenu创建一个新菜单
        impAct = QAction('Import mail', self)
        impMenu.addAction(impAct) # 使用addAction添加一个动作
        fileMenu.addMenu(impMenu)

        newAct = QAction('New', self)
        fileMenu.addAction(newAct)

        ################ 勾选菜单 ################
        self.statusbar = self.statusBar()
        self.statusbar.showMessage('Ready')
        viewMenu = menubar.addMenu('View')

        viewStatAct = QAction('View statusbar', self, checkable=True)# 创建一个能选中的菜单
        viewStatAct.setStatusTip('View statusbar')
        viewStatAct.setChecked(True) # 默认设置为选中状态
        viewStatAct.triggered.connect(self.toggleMenu)

        viewMenu.addAction(viewStatAct)
        ################ 工具栏 ################
        exitAct = QAction(QIcon('exit.jpg'), 'Exit', self)
        exitAct.setShortcut('Ctrl+Q')
        exitAct.triggered.connect(qApp.quit)

        self.toolbar = self.addToolBar('Exit') # addToolBar 添加工具栏
        self.toolbar.addAction(exitAct)



        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle('Main window')
        self.show()
    def toggleMenu(self, state):
        if state:
            self.statusbar.show()
        else:
            self.statusbar.hide()

    def contextMenuEvent(self, event):
        ################ 右键菜单 ################
        cmenu = QMenu(self)

        newAct = cmenu.addAction("New")
        opnAct = cmenu.addAction("Open")
        quitAct = cmenu.addAction("Quit")
        # 从鼠标右键事件对象中获得当前坐标。mapToGlobal()方法把当前组件的相对坐标转换为窗口（window）的绝对坐标。
        action = cmenu.exec_(self.mapToGlobal(event.pos()))# 使用exec_()方法显示菜单

        if action == quitAct:
            qApp.quit()
        # textEdit = QTextEdit()
        # self.setCentralWidget(textEdit)
        #
        # exitAct = QAction(QIcon('exit24.png'), 'Exit', self)
        # exitAct.setShortcut('Ctrl+Q')
        # exitAct.setStatusTip('Exit application')
        # exitAct.triggered.connect(self.close)
        #
        # self.statusBar()
        #
        # menubar = self.menuBar()
        # fileMenu = menubar.addMenu('&File')
        # fileMenu.addAction(exitAct)
        #
        # toolbar = self.addToolBar('Exit')
        # toolbar.addAction(exitAct)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


















