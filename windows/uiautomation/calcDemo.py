#-*-coding:utf-8-*-
# @Time:    2023/03/04 21:12
# @Author:  haiyongz
# @File:    getCpuIdle.py
# @description: 读取DUT CPU idle数据
# 执行方式：python getCpuIdle.py -d 30 -n 6

import datetime
import logging
import os
from time import sleep
import time
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
    def __init__(self, console_level = logging.INFO, file_level = logging.INFO, fmt = '%(asctime)s - %(levelname)s: %(message)s', datefmt='%Y%m%d-%H:%M:%S'):
        self.filename = 'wlan-log_' + datetime.datetime.now().strftime('%Y%m%d') + '.log'        
        self.fmt      = fmt
        self.datefmt  = datefmt
        self.console_level = console_level
        self.file_level    = file_level
    
    def myLogger(self):
        # 创建自定义 logger
        logging.root.setLevel(logging.NOTSET)
        self.logger = logging.getLogger(__name__)  
        abspath = os.path.dirname(os.path.abspath(__file__)) # 脚本绝对路径
        logpath = os.path.join(abspath, 'log') # 日志保存路径
        if not os.path.exists(logpath):
            os.mkdir(logpath)
        self.logname  = os.path.join(logpath, self.filename)

        # 创建处理器 handlers
        # console_handler = logging.StreamHandler() # 输出到控制台
        file_handler    = logging.FileHandler(self.logname, mode='a') # 输出到文件
        # console_handler.setLevel(self.console_level)
        file_handler.setLevel(self.file_level)

        # 设置日志格式
        format_str  = logging.Formatter(self.fmt, self.datefmt)  # 设置日志格式
        # 将格式器添加到处理器中
        # console_handler.setFormatter(format_str)
        file_handler.setFormatter(format_str)

        # 将处理器添加到logger
        # self.logger.addHandler(console_handler)
        self.logger.addHandler(file_handler)
        return self.logger

class uiautoCalc(Loggers):
    """读取DUT CPU信息

    """
    def __init__(self):
        super().__init__()
        self.logger = Loggers().myLogger()

    def calc_demo1(self):
        """返回DUT CPU Idle值

        :return cpuIdle: CPU Idle值
        """        
        # 显示搜索控件所遍历的控件数和搜索时间
        # uiautomation.DEBUG_SEARCH_TIME =True# 设置全局搜索超时时间为1秒
        # uiautomation.SetGlobalSearchTimeout(1)# 创建计算器窗口控件
        self.logger.info("1")
        calc = auto.WindowControl(Name="计算器")
        calc_list = ["二", "加", "八", "等于"]
        for i in range(0, len(calc_list)):
            calc.ButtonControl(Name=calc_list[i]).Click()
            time.sleep(0.5)
        calc_result = calc.TextControl(foundIndex=3).Name
        print(calc_result)


    def calc_demo2(self):
        """返回DUT CPU Idle值

        :return cpuIdle: CPU Idle值
        """        

        # 显示搜索控件所遍历的控件数和搜索时间
        auto.uiautomation.DEBUG_SEARCH_TIME =True# 设置全局搜索超时时间为1秒
        auto.uiautomation.SetGlobalSearchTimeout(1)# 创建计算器窗口控件
        calcWindow = auto.WindowControl(
            searchDepth=1, Name='计算器', desc='计算器窗口')
        if not calcWindow.Exists(0,0):
            subprocess.Popen('calc')# 设置窗口前置
        calcWindow.SetActive() # 激活窗口
        calcWindow.SetTopmost(True)# 设置为顶层
        calcWindow.ButtonControl(AutomationId='TogglePaneButton',
                                desc='打开导航').Click(waitTime=0.01)
        
        calcWindow.ListItemControl(AutomationId='Scientific',
                                desc='选择科学计算器').Click(waitTime=0.01)
        clearButton = calcWindow.ButtonControl(AutomationId='clearEntryButton',
                                            desc='点击CE清空所有输入')
        if clearButton.Exists(0,0):
            clearButton.Click(waitTime=0)
        else:
            calcWindow.ButtonControl(AutomationId='clearButton',
                                    desc='点击C清空所有输入').Click(waitTime=0)
        id2char ={'num0Button':'0','num1Button':'1','num2Button':'2','num3Button':'3','num4Button':'4','num5Button':'5','num6Button':'6','num7Button':'7','num8Button':'8','num9Button':'9','decimalSeparatorButton':'.','plusButton':'+','minusButton':'-','multiplyButton':'*','divideButton':'/','equalButton':'=','openParenthesisButton':'(','closeParenthesisButton':')'}
        char2Button ={}
        for c, d in auto.WalkControl(calcWindow, maxDepth=4):
            if c.AutomationId in id2char:
                char2Button[id2char[c.AutomationId]]= c
        
        
        def calc(expression):
            expression =''.join(expression.split())
            if not expression.endswith('='):
                expression +='='
                for char in expression:
                    char2Button[char].Click(waitTime=0)
            time.sleep(0.1)
            calcWindow.SendKeys('{Ctrl}c', waitTime=0.1)
            return auto.GetClipboardText()
        
        
        result = calc('1234 * (4 + 5 + 6) - 78 / 90.8')
        print('1234 * (4 + 5 + 6) - 78 / 90.8 =', result)
        result = calc('3*3+4*4')
        print('3*3+4*4 =', result)
        result = calc('2*3.14159*10')
        print('2*3.14159*10 =', result)
        calcWindow.CaptureToImage('calc.png', x=7, y=0, width=-14, height=-7)
        calcWindow.GetWindowPattern().Close()




if __name__ == "__main__":
    ui = uiautoCalc()
    ui.calc_demo1()
    # ci.calc_demo2()
    # ci.dfjh_demo1()
    # ci.attrobot_demo()
 


