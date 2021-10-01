#coding=utf-8
import sys
from PyQt4 import QtCore, QtGui
from test_w2 import W2
style = """
        .QPushButton{
        border-style:none;
        border:1px solid #C2CCD8; 
        color:#F0F0F0;  
        padding:5px;
        min-height:20px;
        border-radius:5px;
        background:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:1,stop:0 #4D4D4D,stop:1 #292929);
        }
    """
# 父窗口
class MyForm(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.setWindowTitle(u'父窗口')

        self.label1 = QtGui.QLabel(u"从子窗口接收")
        self.label2 = QtGui.QLabel(u"发送给子窗口")
        self.lineEdit1 = QtGui.QLineEdit()
        self.lineEdit2 = QtGui.QLineEdit()

        self.button1 = QtGui.QPushButton(u'子窗口', self)
        self.button2 = QtGui.QPushButton(u'发送', self)

        layout = QtGui.QGridLayout()
        layout.addWidget(self.label1, 0, 0)
        layout.addWidget(self.lineEdit1, 0, 1)
        layout.addWidget(self.label2, 1, 0)
        layout.addWidget(self.lineEdit2, 1, 1)
        layout.addWidget(self.button1, 2, 0)
        layout.addWidget(self.button2, 2, 1)
        self.setLayout(layout)

        self.button1.clicked.connect(self.child)
        self.button2.clicked.connect(self.transfer)
        self.setStyleSheet(style)

    def child(self):
        print (u'弹出子窗口')
        self.w2 = W2()
        self.connect(self.w2, QtCore.SIGNAL("transfer_father"), self.receive)
        self.w2.show()
        self.w2.connect(self, QtCore.SIGNAL("transfer_child"), self.w2.receive)

    @QtCore.pyqtSlot(str)
    def receive(self, s):
        print (u'接受到子窗口值')
        self.lineEdit1.setText(str(s))

    def transfer(self):
        str = self.lineEdit2.text()
        self.emit(QtCore.SIGNAL("transfer_child"), str)


if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = MyForm()
    myapp.show()
    sys.exit(app.exec_())