#!/usr/bin/python3
#-*- coding:utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

if __name__ == "__main__":    
    app = QApplication(sys.argv)
    w = QWidget() #QWidge控件是一个用户界面的基本控件，它提供了基本的应用构造器
    w.move(300, 300)  # move()是修改控件位置的的方法。它把控件放置到屏幕坐标的(300, 300)的位置
    w.resize(250,150)# 改变控件的大小，窗口宽250px，高150px。
    w.setGeometry(300, 300, 250, 150)

    w.setWindowTitle('搜狗')# 给窗口添加了一个标题
    w.setWindowIcon(QIcon('icon.png')) # 设置图标logo
    w.show() #show()能让控件在桌面上显示出来。控件在内存里创建，之后才能在显示器上显示出来。
    sys.exit(app.exec_())# 进入了应用的主循环中，事件处理器这个时候开始工作。主循环从窗口上接收事件，
                         # 并把事件传入到派发到应用控件里。当调用exit()方法或直接销毁主控件时，主循环就会结束。














