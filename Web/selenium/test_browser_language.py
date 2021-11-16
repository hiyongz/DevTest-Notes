#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/8/18 17:38
# @Author:  haiyong
# @File:    test_browser_language.py
"""
设置浏览器语言
"""
from time import sleep

import pytest
from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.firefox.options import Options
# from selenium.webdriver.ie.options import Options

class TestBrowserLan():
    def setup(self):
        pass

    def teardown_method(self):
        self.driver.quit()
        pass

    @pytest.mark.skip()
    def test_chrome(self):
        # browser_locale = 'en-US'
        browser_locale = 'ru'
        chrome_driver_path = 'C:/Python27/chromedriver.exe'
        options = Options()
        options.add_argument("--lang={}".format(browser_locale))
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path,
                                   chrome_options=options)
        self.driver.get('https://www.baidu.com')

    # @pytest.mark.skip()
    def test_opera(self):
        browser_locale = 'en-US'
        options = Options()
        options.add_argument("--lang={}".format(browser_locale))
        driver_path = 'C:/Python27/operadriver.exe'
        # driver_path = 'D:/testing_tools/chromedriver85/operadriver.exe'
        self.driver = webdriver.Opera(executable_path=driver_path,options=options)
        self.driver.get('https://www.baidu.com')
        sleep(10)

    @pytest.mark.skip()
    def test_firefox(self):
        browser_locale = 'fr'
        driver_path = 'C:/Python27/geckodriver.exe'
        # profile = webdriver.FirefoxProfile()
        # profile = webdriver.FirefoxProfile(profile_directory='C:/Users/DELL/AppData/Local/Mozilla/Firefox/Profiles')
        profile = webdriver.FirefoxProfile()
        profile.set_preference('intl.accept_languages', 'fr')

        self.driver = webdriver.Firefox(executable_path=driver_path,
                                    firefox_profile=profile)
        self.driver.get('https://www.baidu.com')
        # browser.get('about:preferences')

    @pytest.mark.skip()
    def test_firefox2(self):
        options = Options()
        profile = webdriver.FirefoxProfile()
        profile.set_preference('intl.accept_languages', 'de-DE')
        self.driver = webdriver.Firefox(options=options,firefox_profile=profile)
        self.driver.get('https://www.baidu.com')
        sleep(10)

    # @pytest.mark.skip()
    def test_360(self):
        option=webdriver.ChromeOptions()
        option.binary_location=r'D:/software/360Chrome/Chrome/Application/360chrome.exe'

        browser_locale = 'fr-FR'
        # options = Options()
        option.add_argument("--lang={}".format(browser_locale))

        self.driver=webdriver.Chrome(r'C:/Python27/chromedriver.exe',options=option)
        self.driver.get('https://www.baidu.com')
        sleep(10)

    # @pytest.mark.skip()
    def test_2345(self):
        option=webdriver.ChromeOptions()
        option.binary_location=r'C:/Program Files (x86)/2345Soft/2345Explorer/2345Explorer.exe'
        self.driver = webdriver.Chrome(r'C:/Python27/chromedriver.exe',options=option)
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys("test")
        self.driver.find_element_by_id('su').click()
        sleep(10)
    @pytest.mark.skip()
    def test_liebao(self):
        option=webdriver.ChromeOptions()
        option.binary_location=r'C:/Users/DELL/AppData/Local/liebao/liebao.exe'
        self.driver = webdriver.Chrome(r'C:/Python27/chromedriver.exe',options=option)
        self.driver.get('https://www.baidu.com')
        self.driver.find_element_by_xpath('//*[@id="kw"]').send_keys("test")
        self.driver.find_element_by_id('su').click()
        sleep(10)
    @pytest.mark.skip()
    def test_Ie(self):
        # option=webdriver.IeOptions()
        # option.binary_location=r'C:/Program Files (x86)/Maxthon5/Bin/Maxthon.exe'
        self.driver = webdriver.Ie()#,options=option
        self.driver.get('https://www.baidu.com')
        self.driver.implicitly_wait(5)
        self.driver.find_element_by_id('kw').send_keys("test")
        self.driver.find_element_by_id('su').click()


    @pytest.mark.skip()
    def test_broser_lan(self):
        self.driver = webdriver.Chrome()
        self.driver.get('chrome://settings/')
        print(self.driver.execute_script("return window.navigator.language;"))
        lang = self.driver.execute_script("return window.navigator.language;")
        assert lang.lower() == 'zh-CN'.lower()
if __name__ == '__main__':
    pytest.main()












