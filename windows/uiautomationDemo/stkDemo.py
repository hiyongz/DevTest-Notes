# -*- coding: utf-8 -*-
# @Time    : 2025/1/25 9:42
# @Author  : hiyongz
# @File    : stkDemo.py
# @Project: DevTest-Notes

import datetime
import logging
import os
from time import sleep

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


class uiautoSTK(Loggers):
    """uiautomation控制计算器

    """

    def __init__(self):
        super().__init__()
        self.logger = Loggers().myLogger()
        auto.uiautomation.DEBUG_SEARCH_TIME = True
        auto.uiautomation.SetGlobalSearchTimeout(10)  # 设置全局搜索超时时间
        # subprocess.Popen('calc')  # 设置窗口前置
        os.startfile("C:/Users/Public/Desktop/STK 11 x64.lnk")
        sleep(1)

    # def stop_stk(self):
        "AgUiApplication.exe"

    def continue_startup(self):

        self.startupWindow = auto.WindowControl(searchDepth=1, Name='Warning: ITAR Restricted Software',
                                             desc='Warning: ITAR Restricted Software')
        if not self.startupWindow.Exists(0, 0):
            os.startfile("C:/Users/Public/Desktop/STK 11 x64.lnk")
            self.startupWindow = auto.WindowControl(searchDepth=1, Name='Warning: ITAR Restricted Software',
                                                    desc='Warning: ITAR Restricted Software')
        self.startupWindow.SetActive()  # 激活窗口
        self.startupWindow.SetTopmost(True)  # 设置为顶层
        self.startupWindow.ButtonControl(Name="Continue Startup").Click(waitTime=0.01)

    def open_a_scenario(self):
        self.stkWindow = auto.WindowControl(searchDepth=1, Name='STK 11',
                                                desc='STK 11窗口')
        self.stkWindow.SetActive()  # 激活窗口
        self.stkWindow.SetTopmost(True)  # 设置为顶层
        self.stkWindow.ButtonControl(Name="Open a Scenario").Click(waitTime=0.01)
        self.stkWindow.EditControl(Name="文件名(N):").SendKeys("E:\\300-Work\\2025\STK\Scenario1\Scenario1.sc")
        self.stkWindow.ButtonControl(Name="打开(O)").Click(waitTime=0.01)
        sleep(5)

    def scenario_config(self):
        self.scenarioWindow = auto.WindowControl(searchDepth=1, SubName='STK 11',
                                            desc='STK 11 scenario窗口')
        for _ in range(10):
            if not self.scenarioWindow.Exists(0, 0):
                sleep(2)
                self.scenarioWindow = auto.WindowControl(searchDepth=1, SubName='STK 11',
                                                         desc='STK 11 scenario窗口')
            else:
                break
        self.scenarioWindow.SetActive()  # 激活窗口
        self.scenarioWindow.SetTopmost(True)  # 设置为顶层
        # auto.MoveTo(164, 184)
        # auto.Click(164, 184, waitTime=0)
        # auto.Click(164, 184, waitTime=0)
        rect = self.scenarioWindow.PaneControl(Name="Object Browser").BoundingRectangle
        auto.MoveTo(rect.left + 82, rect.top + 72)
        auto.Click(rect.left + 82, rect.top + 72, waitTime=0)
        auto.Click(rect.left + 82, rect.top + 72, waitTime=0)
        self.logger.info("1111111111111111111111")
        self.logger.info(rect)

    # def gotoScientific(self):
    #     self.calcWindow.ButtonControl(AutomationId='TogglePaneButton', desc='打开导航').Click(waitTime=0.01)
    #     self.calcWindow.ListItemControl(AutomationId='Scientific', desc='选择科学计算器').Click(waitTime=0.01)
    #     clearButton = self.calcWindow.ButtonControl(AutomationId='clearEntryButton', desc='点击CE清空输入')
    #     if clearButton.Exists(0, 0):
    #         clearButton.Click(waitTime=0)
    #     else:
    #         self.calcWindow.ButtonControl(AutomationId='clearButton', desc='点击C清空输入').Click(waitTime=0.01)
    #
    # def getKeyControl(self):
    #     automationId2key = {'num0Button': '0', 'num1Button': '1', 'num2Button': '2', 'num3Button': '3',
    #                         'num4Button': '4', 'num5Button': '5', 'num6Button': '6', 'num7Button': '7',
    #                         'num8Button': '8', 'num9Button': '9', 'decimalSeparatorButton': '.', 'plusButton': '+',
    #                         'minusButton': '-', 'multiplyButton': '*', 'divideButton': '/', 'equalButton': '=',
    #                         'openParenthesisButton': '(', 'closeParenthesisButton': ')'}
    #
    #     calckeys = self.calcWindow.GroupControl(ClassName='LandmarkTarget')
    #     keyControl = {}
    #     for control, depth in auto.WalkControl(calckeys, maxDepth=3):
    #         if control.AutomationId in automationId2key:
    #             self.logger.info(control.AutomationId)
    #             keyControl[automationId2key[control.AutomationId]] = control
    #     return keyControl
    #
    # def calculate(self, expression, keyControl):
    #     expression = ''.join(expression.split())
    #     if not expression.endswith('='):
    #         expression += '='
    #         for char in expression:
    #             keyControl[char].Click(waitTime=0)
    #     self.calcWindow.SendKeys('{Ctrl}c', waitTime=0.1)
    #     return auto.GetClipboardText()
    #
    # def calc_demo1(self):
    #     """计算器示例1
    #
    #     :return
    #     """
    #     self.gotoScientific()
    #     # calc = auto.WindowControl(Name="计算器")
    #     calc_list = ["二", "加", "八", "等于"]
    #     for i in range(0, len(calc_list)):
    #         self.calcWindow.ButtonControl(Name=calc_list[i]).Click(waitTime=0.2)
    #     # calc_result = self.calcWindow.TextControl(AutomationId='CalculatorResults').Name
    #     self.calcWindow.SendKeys('{Ctrl}c', waitTime=0.1)
    #     calc_result = auto.GetClipboardText()
    #     print(calc_result)
    #
    # def calc_demo2(self):
    #     """计算器示例2
    #
    #     :return :
    #     """
    #     self.gotoScientific()  # 选择科学计算器
    #     keyControl = self.getKeyControl()  # 获取按键控件
    #     result = self.calculate('(1 + 2 - 3) * 4 / 5.6 - 7', keyControl)
    #     print('(1 + 2 - 3) * 4 / 5.6 - 7 =', result)
    #     self.calcWindow.CaptureToImage('calc.png', x=7, y=0, width=-14, height=-7)  # 截图
    #     # self.calcWindow.GetWindowPattern().Close() # 关闭计算机


if __name__ == "__main__":
    ui = uiautoSTK()
    # ui.calc_demo1()
    ui.continue_startup()
    ui.open_a_scenario()
    ui.scenario_config()




