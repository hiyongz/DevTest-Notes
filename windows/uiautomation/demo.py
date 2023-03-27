#-*-coding:utf-8-*-
# @Time:    2023/03/04 21:12
# @Author:  zhanghaiyong
# @File:    getCpuIdle.py
# @description: 读取DUT CPU idle数据
# 执行方式：python getCpuIdle.py -d 30 -n 6

import datetime
import logging
import os
import argparse
import sys
from time import sleep
import uiautomation as auto
import subprocess

class ArgParser():
    """读取输入参数

    """
    def __init__(self):
        self.usage = "读取无线网卡信息"

    def arg_parser(self):
        self.parser = argparse.ArgumentParser(description = self.usage)
        # 添加参数
        self.parser.add_argument("-d", "--duration", help = "读取时间，单位秒", default=5)
        self.parser.add_argument("-n", "--number", help = "读取次数", default=3)
        self.parser.add_argument("-p", "--path", help = "日志保存路径")
        args          = self.parser.parse_args()
        self.duration = args.duration
        self.num      = args.number
        self.logpath  = args.path

class Loggers(ArgParser):
    """日志记录器

    记录日志，支持命令行窗口和保存到文件。
    Attributes:
        console_level: 输出到控制台最低的日志严重级别
        file_level: 保存到文件最低的日志严重级别
        fmt: 日志格式化输出样式
        datefmt: 时间格式化
    """
    def __init__(self, console_level = logging.INFO, file_level = logging.INFO, fmt = '%(asctime)s - %(levelname)s: %(message)s', datefmt='%Y%m%d-%H:%M:%S'):
        super().__init__()
        self.arg_parser()
        self.filename = 'wlan-log_' + datetime.datetime.now().strftime('%Y%m%d') + '.log'
        
        self.fmt      = fmt
        self.datefmt  = datefmt
        self.console_level = console_level
        self.file_level    = file_level
    
    def myLogger(self):
        # 创建自定义 logger
        logging.root.setLevel(logging.NOTSET)
        self.logger = logging.getLogger(__name__)

        if self.logpath:
            logpath = self.logpath
        else:
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

class automationLibrary():
    def WindowControl(self, **kwargs):
        window = auto.WindowControl(**kwargs)
        return window


class dfjhSetting():

    def __init__(self):
        self.dfjhWindow = auto.WindowControl(
        searchDepth=1, Name='DFJH', desc='转盘控制软件窗口')
        
    def dfghActive(self):
        self.dfjhWindow.SetActive() # 激活窗口
        self.dfjhWindow.SetTopmost(True)# 设置为顶层
    
    def gotomanualControl(self):
        # 点击手动控制
        self.dfjhWindow.TabItemControl(Name='手动控制').Click(waitTime=1)
        Execution_ProfileText = self.dfjhWindow.TextControl(SubName="Execution Profile", AutomationId = "-31933")
        for i in range(3):
            if Execution_ProfileText.Exists(0,0):
                return
            else:
                self.dfjhWindow.TabItemControl(Name='手动控制').Click(waitTime=1)
        print("进入手动控制窗口失败")
        sys.exit()

    def getCurrentPositionX(self):
        curPosControl = self.dfjhWindow.EditControl(AutomationId='1207')
        curPos_X = curPosControl.GetValuePattern().Value
        return curPos_X

    def addAngle(self):
        # 角度+ : X+
        self.dfjhWindow.ButtonControl(AutomationId="1193").Click(waitTime=2)
        print(self.getCurrentPosition())

    def subtractAngle(self):
        # 角度- : X-
        self.dfjhWindow.ButtonControl(AutomationId="1192").Click(waitTime=2)
        print(self.getCurrentPosition())

    def __getState(self, Name, AutomationId):
        checkbox = self.dfjhWindow.CheckBoxControl(searchDepth=6, Name=Name, ClassName='Button', AutomationId=AutomationId)
        toggleState = checkbox.GetTogglePattern().ToggleState
        return checkbox, toggleState
    
    def axisToggleOn(self, Name, AutomationId):
        checkbox, state = self.__getState(Name, AutomationId)
        if state == 0:
            checkbox.Click()

    def axisToggleOff(self, Name, AutomationId):
        checkbox, state = self.__getState(Name, AutomationId)
        if state == 1:
            checkbox.Click()

    def angleSetX(self, angle):
        """设置X轴角度
        
        :param angle: 角度值
        :return : 无
        """
        if float(angle) % 30 != 0 or float(angle) > 360:
            print("error")

        curPos = self.getCurrentPositionX()
        curPos = float(curPos)
        angle  = int(angle)

        if (angle > 180 and curPos > 0) or (angle < 180 and curPos < 0):
            self.resetX()
            curPos = self.getCurrentPositionX()
            curPos = float(curPos)

        if int(angle) <= 180:
            diffangle = curPos - angle
            step = int(abs(diffangle)/30)
            print(step)
            if diffangle < 0:
                for i in range(step):
                    self.addAngle()
            elif diffangle > 0:
                for i in range(step):
                    self.subtractAngle()
        else:
            angle = 360 - angle
            diffangle = abs(curPos) - angle
            step = int(abs(diffangle)/30)
            print(step)
            if diffangle < 0:
                for i in range(step):
                    self.subtractAngle()
            elif diffangle > 0:
                for i in range(step):
                    self.addAngle()

    def resetX(self):
        self.axisToggleOn('X', '1201')
        self.axisToggleOff('Y', '1202')
        self.axisToggleOff('Z', '1203')
        self.axisToggleOff('T', '1204')
        
        self.dfjhWindow.ButtonControl(Name='执行回零', AutomationId="1205").Click(waitTime=1)
        curPos = self.getCurrentPositionX()
        curPos = int(curPos)
        for i in range(20):
            if curPos == 0:
                return
            else:
                sleep(0.5)

        print("回零操作失败")
        sys.exit()


class cpuInfo(Loggers):
    """读取DUT CPU信息

    """
    def __init__(self):
        super().__init__()
        self.logger = Loggers().myLogger()

    def notepad_demo(self):
        """返回DUT CPU Idle值

        :return cpuIdle: CPU Idle值
        """
        subprocess.Popen('notepad.exe')# 从桌面的第一层子控件中找到记事本程序的窗口WindowControl
        notepadWindow = auto.WindowControl(searchDepth=1, ClassName='Notepad')
        print(notepadWindow.Name)# 设置窗口前置
        notepadWindow.SetTopmost(True)


    def dfjh_demo1(self):
        dfgh = dfjhSetting()
        dfgh.dfghActive()
        dfgh.gotomanualControl()
        curpos = dfgh.getCurrentPositionX()
        print(curpos)
        dfgh.addAngle()
        dfgh.subtractAngle()
        dfgh.resetX()
        


    def dfjh_demo2(self):
        
        dfjhWindow = auto.WindowControl(
        searchDepth=1, Name='DFJH', desc='转盘控制软件窗口')
        dfjhWindow.SetActive() # 激活窗口
        dfjhWindow.SetTopmost(True)# 设置为顶层

        # 点击手动控制
        dfjhWindow.TabItemControl(Name='手动控制').Click(waitTime=0.01)
        
        curPos_X = dfjhWindow.EditControl(AutomationId='1207')
        print(curSpeed_X.GetValuePattern().Value)
        
        
        # 角度+ : X+
        dfjhWindow.ButtonControl(AutomationId="1193").Click(waitTime=2)
        print(curSpeed_X.GetValuePattern().Value)

        # 角度- : X-
        # dfjhWindow.ButtonControl(AutomationId="1192").Click()

        # 清0

        # 读取当前角度值


    def attrobot_demo(self):
        rfWindow = auto.WindowControl(
        searchDepth=1, SubName='attrobot3自动化测试平台', desc='attrobot3自动化测试平台窗口')
        rfWindow.SetActive() # 激活窗口
        rfWindow.SetTopmost(True)# 设置为顶层

        # 复选框
        
        autosave_checkbox = rfWindow.CheckBoxControl(searchDepth=5, SubName='Autosave', ClassName='Button', AutomationId='167')
        print(autosave_checkbox.GetTogglePattern().ToggleState)
        if autosave_checkbox.GetTogglePattern().ToggleState==0:    #checkbox ToggleState
            autosave_checkbox.Click()
        elif(autosave_checkbox.GetTogglePattern().ToggleState==1):
            autosave_checkbox.Click()

        Execution_ProfileText = rfWindow.TextControl(SubName="Execution Profile", AutomationId = "-31933")
        if Execution_ProfileText.Exists(0,0):
            print("存在")


    def calc_demo1(self):
        """返回DUT CPU Idle值

        :return cpuIdle: CPU Idle值
        """        
        # 显示搜索控件所遍历的控件数和搜索时间
        # uiautomation.DEBUG_SEARCH_TIME =True# 设置全局搜索超时时间为1秒
        # uiautomation.SetGlobalSearchTimeout(1)# 创建计算器窗口控件

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
    # ci = cpuInfo()
    # ci.notepad_demo()
    # ci.calc_demo1()
    # ci.calc_demo2()
    # ci.dfjh_demo1()
    # ci.attrobot_demo()

    def angleSetX(angle):
        """设置X轴角度
        
        :param angle: 角度值
        :return : 无
        """
        # curPos = self.getCurrentPositionX()
        curPos = '0.0000'
        curPos = float(curPos)

        diffangle = curPos - angle
        step = int(abs(diffangle)/30)
        print(step)
        if diffangle < 0:


    angleSetX(30)


