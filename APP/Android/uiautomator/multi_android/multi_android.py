#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2023/2/27
# @Author:  hiyongz
# @File:    multi_android.py

from uiautomator2 import exceptions as u2exceptions

import os
import datetime
import logging
import configparser
import asyncio
import uiautomator2 as u2


class Loggers(object):
    """日志记录器

    记录日志，支持命令行窗口和保存到文件。
    Attributes:
        log_level: 最低的日志严重级别
        log_dir: 日志存放目录
        fmt: 日志格式化输出样式
    """
    def __init__(self, log_level = logging.INFO, log_dir = 'log', fmt = '%(asctime)s - %(levelname)s: %(message)s'):
        filename = 'log_' + datetime.datetime.now().strftime('%Y%m%d-%H-%M') + '.log'
        abspath = os.path.dirname(os.path.abspath(__file__)) # 脚本绝对路径
        logpath = os.path.join(abspath, log_dir) # 日志保存路径
        if not os.path.exists(logpath):
            os.mkdir(logpath)
        logname = os.path.join(logpath, filename)

        self.logger = logging.getLogger(filename)
        format_str  = logging.Formatter(fmt)  # 设置日志格式
        self.logger.setLevel(log_level)  # 设置日志级别

        stream_handler = logging.StreamHandler()  # 输出到控制台
        stream_handler.setFormatter(format_str)

        file_handler = logging.FileHandler(logname, mode='a') # 输出到文件
        file_handler.setFormatter(format_str)
        
        self.logger.addHandler(stream_handler)
        self.logger.addHandler(file_handler)


class App(Loggers):
    """打开手机应用并刷新
    
    """
    def __init__(self):
        super().__init__()
        # self._appPackage = 'com.tenda.router.app'
        # self._appActivity = '.activity.Anew.Splash.SplashActivity'

        self.apps = ['weibo', 'douyin', 'xiaohongshu', 'taobao', 'douyu']
        # self.apps = ['weibo', 'douyin']

        self._weiboPackage        = 'com.sina.weibo'
        self._weiboActivity       = '.SplashActivity'
        self._douyinPackage       = 'com.ss.android.ugc.aweme'
        self._douyinActivity      = '.splash.SplashActivity'
        self._xiaohongshuPackage  = 'com.xingin.xhs'
        self._xiaohongshuActivity = '.index.v2.IndexActivityV2'
        self._taobaoPackage       = 'com.taobao.taobao'
        self._taobaoActivity      = 'com.taobao.tao.welcome.Welcome'
        self._douyuPackage        = 'air.tv.douyu.android'
        self._douyuActivity       = 'tv.douyu.view.activity.launcher.DYSplashLauncherActivity'
        self.refreshNum = 5 # 连续刷新次数

        # 读取手机序列号
        path          = os.path.dirname(os.path.realpath(__file__))
        configpath    = os.path.join(path, 'config.ini')
        self.config   = configparser.ConfigParser() # 类实例化
        self.config.read(configpath)
        self._devices = self.config.items('phone_serial')
        for app in self.apps:
            for device in self._devices:
                refresh_countvar = device[0] + '_' + app
                exec(f'self.{refresh_countvar} = 0')

    def connect(self):
        """连接手机
        :param: 无
        :return: 无
        """
        self.phones = []
        for phone_serial in self._devices:
            try:
                exec(f'self.{phone_serial[0]} = u2.connect(phone_serial[1])')
                exec(f'self.{phone_serial[0]}.set_new_command_timeout(300)')
                exec(f'self.{phone_serial[0]}.implicitly_wait(5)')
                self.phones.append(phone_serial[0])
                self.logger.info("%s 连接成功！"%phone_serial[0])
                exec(f'self.{phone_serial[0]}.unlock()') # 点亮屏幕并解锁
            except RuntimeError as e:
                self.logger.error("%s %s"%(phone_serial[0], e))

    async def open_weibo(self, phone):
        """打开微博并刷新
        
        :param phone: 手机别名，是connect()方法连接成功的手机
        :return: 无
        """
        try:
            exec(f'self.{phone}.app_start(self._weiboPackage, self._weiboActivity)')
            # 判断是否打开成功
            self.status = False
            exec(f'self.{phone}.app_start(self._weiboPackage,".VisitorMainTabActivity")')
            exec(f'self.status=self.{phone}.wait_activity(".VisitorMainTabActivity", timeout=5)')
            if self.status:
                exec(f'self.{phone}.swipe_ext("down", scale=0.8)') # 刷新
                exec(f'self.{phone}_weibo += 1') # 刷新次数计数
                exec(f'self.logger.info("%s 第 %s 次刷新微博"%(phone, self.{phone}_weibo))')
            else:
                self.logger.warning("%s 微博首页进入失败"%phone)
                exec(f'self.{phone}.app_start(self._weiboPackage, ".VisitorMainTabActivity", wait=True, stop=True)')
        except RuntimeError as e:
            self.logger.error("%s %s"%(phone, e))

    async def open_douyin(self, phone):
        """打开抖音并刷新
        
        :param phone: 手机别名
        :return: 无
        """
        try:
            exec(f'self.{phone}.app_start(self._douyinPackage, self._douyinActivity)')        
            self.status = False
            exec(f'self.{phone}.app_start(self._douyinPackage,self._douyinActivity)')
            exec(f'self.status=self.{phone}.wait_activity(self._douyinActivity, timeout=5)')
            if self.status:
                exec(f'self.{phone}.swipe_ext("down", scale=0.8)') # 刷新
                exec(f'self.{phone}_douyin += 1') # 刷新次数计数
                exec(f'self.logger.info("%s 第 %s 次刷新抖音"%(phone, self.{phone}_douyin))')
            else:
                self.logger.warning("%s 抖音首页进入失败"%phone)
                exec(f'self.{phone}.app_start(self._douyinPackage,self._douyinActivity, wait=True, stop=True)')
        except RuntimeError as e:
            self.logger.error("%s %s"%(phone, e))

    async def open_xiaohongshu(self, phone):
        """打开小红书并刷新
        
        :param phone: 手机别名
        :return: 无
        """
        try:
            exec(f'self.{phone}.app_start(self._xiaohongshuPackage, self._xiaohongshuActivity)')        
            self.status = False
            exec(f'self.{phone}.app_start(self._xiaohongshuPackage,".index.v2.IndexActivityV2")')
            exec(f'self.status=self.{phone}.wait_activity(".index.v2.IndexActivityV2", timeout=5)')
            if self.status:
                exec(f'self.{phone}.swipe_ext("down", scale=0.8)') # 刷新
                exec(f'self.{phone}_xiaohongshu += 1') # 刷新次数计数
                exec(f'self.logger.info("%s 第 %s 次刷新小红书"%(phone, self.{phone}_xiaohongshu))')
            else:
                self.logger.warning("%s 小红书首页进入失败"%phone)
                exec(f'self.{phone}.app_start(self._xiaohongshuPackage, ".index.v2.IndexActivityV2", wait=True, stop=True)')
        except RuntimeError as e:
            self.logger.error("%s %s"%(phone, e))

    async def open_taobao(self, phone):
        """打开淘宝并刷新
        
        :param phone: 手机别名
        :return: 无
        """
        try:
            exec(f'self.{phone}.app_start(self._taobaoPackage, self._taobaoActivity)')
            
            self.status = False
            exec(f'self.{phone}.app_start(self._taobaoPackage,"com.taobao.tao.TBMainActivity")')
            exec(f'self.status=self.{phone}.wait_activity("com.taobao.tao.TBMainActivity", timeout=5)')
            if self.status:
                exec(f'self.{phone}.xpath("""//*[@content-desc="首页"]""").click()') # 点击首页刷新
                exec(f'self.{phone}_taobao += 1') # 刷新次数计数
                exec(f'self.logger.info("%s 第 %s 次刷新淘宝"%(phone, self.{phone}_taobao))')
            else:
                self.logger.warning("%s 淘宝首页进入失败"%phone)
                exec(f'self.{phone}.app_start(self._taobaoPackage, "com.taobao.tao.TBMainActivity", wait=True, stop=True)')
        except RuntimeError as e1:
            self.logger.error("%s %s"%(phone, e1))
        except u2exceptions.XPathElementNotFoundError as e2:
            self.logger.error("%s 微博首页刷新失败"%(phone))

    async def open_douyu(self, phone):
        """打开斗鱼并刷新
        
        :param phone: 手机别名
        :return: 无
        """
        try:
            exec(f'self.{phone}.app_start(self._douyuPackage, self._douyuActivity)')
            
            self.status = False
            exec(f'self.{phone}.app_start(self._douyuPackage, "com.douyu.module.home.pages.main.MainActivity")')
            exec(f'self.status=self.{phone}.wait_activity("com.douyu.module.home.pages.main.MainActivity", timeout=5)')
            if self.status:
                exec(f'self.{phone}.swipe_ext("down", scale=0.8)') # 下拉刷新
                exec(f'self.{phone}_douyu += 1') # 刷新次数计数
                exec(f'self.logger.info("%s 第 %s 次刷新斗鱼"%(phone, self.{phone}_douyu))')
            else:
                self.logger.warning("%s 斗鱼首页进入失败"%phone)
                exec(f'self.{phone}.app_start(self._douyuPackage, "com.douyu.module.home.pages.main.MainActivity", wait=True, stop=True)')
        except RuntimeError as e:
            self.logger.error("%s %s"%(phone, e))
    
    async def main(self):
        """协程任务创建主函数
        
        :param: 无
        :return: 无
        """
        i = 1
        tasks = []
        for app in self.apps:
            for i in range(self.refreshNum):
                for phone in self.phones:
                    exec(f'task{i} = asyncio.create_task(self.open_{app}("{phone}"))')  
                    exec(f'tasks.append(task{i})')
                    i += 1
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    app = App()
    while True:
        app.connect()
        asyncio.run(app.main())


