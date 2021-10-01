#!/usr/bin/python3
#-*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QToolTip, QPushButton
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QDesktopWidget # 提供用户的桌面信息，包括屏幕的大小
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtCore import QCoreApplication

class Testpyqt(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.move(300, 300)  # move()是修改控件位置的的方法。它把控件放置到屏幕坐标的(300, 300)的位置
        self.resize(250, 150)  # 改变控件的大小，窗口宽250px，高150px
        self.setGeometry(300, 300, 250, 150)
        #################### 窗口图标 #########################
        self.setWindowTitle('搜狗') # 给窗口添加了一个标题
        self.setWindowIcon(QIcon('icon.png'))# 设置图标logo

        #################### 按钮与提示框 #########################
        QToolTip.setFont(QFont('SansSerif', 10)) # 设置提示框的字体，10px的SansSerif字体
        # self.setToolTip('This is a <b>QWidget</b> widget')# 调用setTooltip()创建提示框,可以使用富文本格式的内容
        btn = QPushButton('Button', self) #创建一个按钮
        btn.setToolTip('This is a <b>QPushButton</b> widget') #为按钮添加一个提示框
        btn.resize(btn.sizeHint())#调整按钮大小，sizeHint():默认按钮大小
        btn.move(50, 50)

        #################### 退出 #########################
        qbtn = QPushButton('Quit', self)# 创建一个继承自QPushButton的按钮
        qbtn.clicked.connect(QCoreApplication.instance().quit)# 事件传递系统在PyQt5内建的single和slot机制里面
                                                             # 点击事件和能终止进程并退出应用的quit函数绑定在了一起
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(150, 50)

        self.center()
        self.show()# show()能让控件在桌面上显示出来。控件在内存里创建，之后才能在显示器上显示出来。
        ################### 消息盒子 #########################
    def closeEvent(self,event):   # E大写
        # 如果关闭QWidget，就会产生一个QCloseEvent，并且把它传入到closeEvent函数的event参数中
        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.Yes |
                                     QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
    ################### 窗口居中 #########################
    def center(self):
        qr = self.frameGeometry() #获得主窗口所在的框架
        cp = QDesktopWidget().availableGeometry().center() # 获取显示器的分辨率，然后得到屏幕中间点的位置
        qr.moveCenter(cp) # 把主窗口框架的中心点放置到屏幕的中心位置
        self.move(qr.topLeft()) #通过move函数把主窗口的左上角移动到其框架的左上角

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = Testpyqt()
    sys.exit(app.exec_())  # 进入了应用的主循环中，事件处理器这个时候开始工作。主循环从窗口上接收事件，
    # 并把事件传入到派发到应用控件里。当调用exit()方法或直接销毁主控件时，主循环就会结束。














