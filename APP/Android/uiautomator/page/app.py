#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/6/28 17:45
# @Author:  haiyong
# @File:    app.py

# app初始化，关闭操作
import uiautomator2 as u2
from page.main import Main

class App():
    _device = 'SNHVB20C18002195'
    _appPackage = 'com.tenda.router.app'
    _appActivity = '.activity.Anew.Splash.SplashActivity'

    def connect(self):
        self.d = u2.connect(self._device)
        self.d.set_new_command_timeout(300)  # accessibility服务的最大空闲时间，超时将自动释放
        self.d.implicitly_wait(5)  # 隐式等待，元素查找等待时间（默认20s）
        return self

    def start(self):
        self.connect()
        self.d.app_start(self._appPackage, self._appActivity)
        return self

    def install(self):
        self.d.app_install('http://some-domain.com/some.apk')

    def stop(self):
        self.d.app_stop(self._appPackage)

    def restart(self):
        pass

    def main(self):
        return Main(self._driver)
