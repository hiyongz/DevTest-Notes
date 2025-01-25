# -*- coding: utf-8 -*-
# @Time    : 2024/8/18 18:11
# @Author  : hiyongz
# @File    : vokoscreenNG_demo.py
# @Project: windows


# -*-coding:utf-8-*-
# @Time:    2023/05/19 21:12
# @Author:  haiyongz
# @File:    calcDemo.py
# @description: 读取DUT CPU idle数据
# 执行方式：python calcDemo.py

import datetime
import logging
import os
import uiautomation as auto
import subprocess


class Loggers():
    """日志记录器

    记录日志，支持命令行窗口和保存到文件。
    Attributes:
        console_level: 输出到控制台最低的日志严重级别
        file_level: 保存到文件最低的日志严重级别
        fmt: 日志格式化输出样式
        datefmt: 时间格式化
    """

    def __init__(self, console_level=logging.INFO, file_level=logging.INFO,
                 fmt='%(asctime)s - %(levelname)s: %(message)s', datefmt='%Y%m%d-%H:%M:%S'):
        self.filename = 'wlan-log_' + datetime.datetime.now().strftime('%Y%m%d') + '.log'
        self.fmt = fmt
        self.datefmt = datefmt
        self.console_level = console_level
        self.file_level = file_level

    def myLogger(self):
        # 创建自定义 logger
        logging.root.setLevel(logging.NOTSET)
        self.logger = logging.getLogger(__name__)
        abspath = os.path.dirname(os.path.abspath(__file__))  # 脚本绝对路径
        logpath = os.path.join(abspath, 'log')  # 日志保存路径
        if not os.path.exists(logpath):
            os.mkdir(logpath)
        self.logname = os.path.join(logpath, self.filename)

        # 创建处理器 handlers
        # console_handler = logging.StreamHandler() # 输出到控制台
        file_handler = logging.FileHandler(self.logname, mode='a')  # 输出到文件
        # console_handler.setLevel(self.console_level)
        file_handler.setLevel(self.file_level)

        # 设置日志格式
        format_str = logging.Formatter(self.fmt, self.datefmt)  # 设置日志格式
        # 将格式器添加到处理器中
        # console_handler.setFormatter(format_str)
        file_handler.setFormatter(format_str)

        # 将处理器添加到logger
        # self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)
        return self.logger


class creenRecord(Loggers):
    """uiautomation控制计算器

    """

    def __init__(self):
        super().__init__()
        self.logger = Loggers().myLogger()
        auto.uiautomation.DEBUG_SEARCH_TIME = True
        auto.uiautomation.SetGlobalSearchTimeout(2)  # 设置全局搜索超时时间
        self.calcWindow = auto.WindowControl(searchDepth=1, Name='vokoscreenNG 4.2.0', desc='vokoscreenNG窗口')  # 计算器窗口
        if not self.calcWindow.Exists(0, 0):
            subprocess.Popen('D:/tools/vokoscreenNG/vokoscreenNG.exe')  # 设置窗口前置
            self.calcWindow = auto.WindowControl(
                searchDepth=1, Name='vokoscreenNG 4.2.0', desc='vokoscreenNG窗口')
        self.calcWindow.SetActive()  # 激活窗口
        self.calcWindow.SetTopmost(True)  # 设置为顶层

    def gotoVokoscreenNG(self):
        self.calcWindow.RadioButtonControl(Name='窗口', desc='打开导航').Click(waitTime=0.01)
        # self.calcWindow.ButtonControl(AutomationId='TogglePaneButton', desc='打开导航').Click(waitTime=0.01)
        # self.calcWindow.ListItemControl(AutomationId='Scientific', desc='选择科学计算器').Click(waitTime=0.01)
        # clearButton = self.calcWindow.ButtonControl(AutomationId='clearEntryButton', desc='点击CE清空输入')
        # if clearButton.Exists(0, 0):
        #     clearButton.Click(waitTime=0)
        # else:
        #     self.calcWindow.ButtonControl(AutomationId='clearButton', desc='点击C清空输入').Click(waitTime=0.01)

    def getKeyControl(self):
        automationId2key = {'num0Button': '0', 'num1Button': '1', 'num2Button': '2', 'num3Button': '3',
                            'num4Button': '4', 'num5Button': '5', 'num6Button': '6', 'num7Button': '7',
                            'num8Button': '8', 'num9Button': '9', 'decimalSeparatorButton': '.', 'plusButton': '+',
                            'minusButton': '-', 'multiplyButton': '*', 'divideButton': '/', 'equalButton': '=',
                            'openParenthesisButton': '(', 'closeParenthesisButton': ')'}

        calckeys = self.calcWindow.GroupControl(ClassName='LandmarkTarget')
        keyControl = {}
        for control, depth in auto.WalkControl(calckeys, maxDepth=3):
            if control.AutomationId in automationId2key:
                self.logger.info(control.AutomationId)
                keyControl[automationId2key[control.AutomationId]] = control
        return keyControl

    def calculate(self, expression, keyControl):
        expression = ''.join(expression.split())
        if not expression.endswith('='):
            expression += '='
            for char in expression:
                keyControl[char].Click(waitTime=0)
        self.calcWindow.SendKeys('{Ctrl}c', waitTime=0.1)
        return auto.GetClipboardText()

    def calc_demo1(self):
        """计算器示例1

        :return
        """
        self.gotoScientific()
        # calc = auto.WindowControl(Name="计算器")
        calc_list = ["二", "加", "八", "等于"]
        for i in range(0, len(calc_list)):
            self.calcWindow.ButtonControl(Name=calc_list[i]).Click(waitTime=0.2)
        # calc_result = self.calcWindow.TextControl(AutomationId='CalculatorResults').Name
        self.calcWindow.SendKeys('{Ctrl}c', waitTime=0.1)
        calc_result = auto.GetClipboardText()
        print(calc_result)

    def calc_demo2(self):
        """计算器示例2

        :return :
        """
        self.gotoVokoscreenNG()  # 选择科学计算器
        # keyControl = self.getKeyControl()  # 获取按键控件
        # result = self.calculate('(1 + 2 - 3) * 4 / 5.6 - 7', keyControl)
        # print('(1 + 2 - 3) * 4 / 5.6 - 7 =', result)
        # self.calcWindow.CaptureToImage('calc.png', x=7, y=0, width=-14, height=-7)  # 截图
        # self.calcWindow.GetWindowPattern().Close() # 关闭计算机


if __name__ == "__main__":
    ui = creenRecord()
    # ui.calc_demo1()
    ui.calc_demo2()




