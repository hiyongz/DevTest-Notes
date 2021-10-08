

# 测试开发小记

<p align="center">
  <a ><img src="https://img.shields.io/badge/%E5%85%AC%E4%BC%97%E5%8F%B7-%E6%B5%8B%E8%AF%95%E5%BC%80%E5%8F%91%E5%B0%8F%E8%AE%B0-brightgreen.svg?style=plastic&logo=WeChat" alt="公众号"></a>
  <a href="https://blog.csdn.net/u010698107"><img src="https://img.shields.io/badge/csdn-CSDN-red.svg" alt="csdn"></a>
  <a href="https://www.cnblogs.com/hiyong/"><img src="https://img.shields.io/badge/cnblogs-博客园-blue.svg" alt="csdn"></a> 
</p>

## 前言

在线文档地址：[https://devtest-notes.readthedocs.io/](https://devtest-notes.readthedocs.io/)

在工作学习过程中经常发现以前遇到过的问题还要重新借助搜索引擎查找一番，很多知识以前学过，发现再次遇到的时候还是有点陌生，其实我们遇到的很多问题是重复的，根据艾宾浩斯遗忘曲线，随着时间推移，记忆率会下降，所以忘记以前的学过的是合理的。大概是在2018年的时候开始使用印象笔记，记录整理学习笔记。而随着用的时间一长，发现收集了太多文章，很少去消化整理，笔记也很混乱。

在2019年，开始重新整理笔记，对笔记进行分类、整理，分类之后发现有一个大致的知识框架了，这种有序的状态感觉非常好。偶然了解到学习金字塔和费曼学习法，发现我前面大多是在输入，不停的收集整理，属于被动学习。发现通过带着问题学习知识，并转化为自己的语言确实记忆会更深刻一些，而且理解会更加深入。然后就开始写文章，也就是输出，发现在写文章过程中对知识的理解会更加深入，更加系统，比如会查询一下这个技术的原理，以及其它扩展用法，不仅仅是解决当前问题。

此外，在后面遇到这个技术相关的用法时，会把它更新到以前的文章中，不断完善。一点一点的向这个框架中填充内容，查漏补缺，将知识串起来。当然，由于时间和精力的关系，无法过于全面和详细，房子慢慢盖嘛！

此项目主要记录测试相关的代码和笔记，目的是为了构建我在测试方面的知识体系，偶然光临本项目，皆为缘分，希望对你有所帮助，如有错误之处，欢迎指正！


## 主要内容
测试用例主要使用Python语言编写，Python相关笔记在这个项目：[hiyongz/PythonNotes](https://github.com/hiyongz/PythonNotes) 。

Linux笔记：[hiyongz/ShellNotes](https://github.com/hiyongz/ShellNotes) 。

Golang笔记：[hiyongz/GolangNotes](https://github.com/hiyongz/GolangNotes) 。

Web自动化测试

- [Selenium自动化测试框架介绍](https://devtest-notes.readthedocs.io/zh/latest/web/selenium-architecture-introduce.html)
- [Web元素定位方法](https://devtest-notes.readthedocs.io/zh/latest/web/selenium_webelement_locator.html)
- [selenium 元素操作](https://devtest-notes.readthedocs.io/zh/latest/web/selenium-webelement-operate.html)
- [xpath & CSS Selector定位](https://devtest-notes.readthedocs.io/zh/latest/web/selenium-xpath-and-CSS-Selector-locator.html)
- [Selenium ActionChains、TouchAction方法](https://devtest-notes.readthedocs.io/zh/latest/web/selenium-actionchains-touchaction.html)
- [Selenium switch_to方法](https://devtest-notes.readthedocs.io/zh/latest/web/selenium-switch_to.html)
- [Select下拉框](https://devtest-notes.readthedocs.io/zh/latest/web/selenium-select.html)
- [Selenium 不同浏览器测试](https://devtest-notes.readthedocs.io/zh/latest/web/selenium-browsers.html)
- [selenium 执行JavaScript脚本](https://devtest-notes.readthedocs.io/zh/latest/web/selenium-javascript.html)
- [selenium/appium 等待方式介绍](https://devtest-notes.readthedocs.io/zh/latest/web/selenium-appium-webdriver-wait.html)
- [Selenium Grid：在多个主机上并行执行自动化脚本](https://devtest-notes.readthedocs.io/zh/latest/web/selenium-grid-for-parallel-execute-script.html)
- [键盘输入keycode](https://devtest-notes.readthedocs.io/zh/latest/web/selenium-appium-keycode.html)

APP自动化测试

- [Android ADB原理及常用命令](https://devtest-notes.readthedocs.io/zh/latest/app/appium-adb.html)
- [Android手机管理平台搭建：STF和atxserver2](https://devtest-notes.readthedocs.io/zh/latest/app/app-testing-for-stf-platform.html)
- [Appium 介绍及环境安装](https://devtest-notes.readthedocs.io/zh/latest/app/appium-install-and-architecture.html)
- [App控件定位](https://devtest-notes.readthedocs.io/zh/latest/app/appium-android-controls.html)
- [Appium元素定位（一）](https://devtest-notes.readthedocs.io/zh/latest/app/appium-locator.html)
- [Appium元素定位（二）：uiautomator定位](https://devtest-notes.readthedocs.io/zh/latest/app/appium-locator-uiautomator.html)
- [Appium控件交互](https://devtest-notes.readthedocs.io/zh/latest/app/appium-locator-operate.html)
- [Android WebView 测试](https://devtest-notes.readthedocs.io/zh/latest/app/appium-android-webview.html)
- [AppCrawler自动遍历测试](https://devtest-notes.readthedocs.io/zh/latest/app/appium-automatic-traversal-test-appcrawler.html)
- [自动遍历测试之Monkey工具](https://devtest-notes.readthedocs.io/zh/latest/app/appium-automatic-traversal-test-monkey.html)
- [App自动化测试工具Uiautomator2](https://devtest-notes.readthedocs.io/zh/latest/app/app-testing-tools-for-uiautomator2.html)
- [App自动化测试工具Airtest](https://devtest-notes.readthedocs.io/zh/latest/app/app-testing-tools-for-airtestproject.html)
- [Windows上实现iOS APP自动化测试：tidevice + WDA + facebook-wda / appium](https://devtest-notes.readthedocs.io/zh/latest/app/app-testing-for-ios-app-on-windows.html)
- [iOS APP自动化：predicate定位](https://devtest-notes.readthedocs.io/zh/latest/app/app-testing-for-ios-location-with-predicate-locator.html)

接口自动化测试

- [接口测试简介及 Web 服务架构](https://devtest-notes.readthedocs.io/zh/latest/api/api-test-and-web-protocol.html)
- [Postman安装与使用](https://devtest-notes.readthedocs.io/zh/latest/api/api-test-postman-guide.html)
- [接口测试框架Requests](https://devtest-notes.readthedocs.io/zh/latest/api/api-test-requests.html)
- [cURL工具介绍及简单使用](https://devtest-notes.readthedocs.io/zh/latest/api/api-test-curl-guide.html)
- [charles SSL证书安装](https://devtest-notes.readthedocs.io/zh/latest/api/api-test-charles-ca-certificate-install.html)
- [接口测试代理工具charles mock测试](https://devtest-notes.readthedocs.io/zh/latest/api/api-test-charles-guide.html)
- [mitmproxy 代理工具介绍：rewrite和map local实现](https://devtest-notes.readthedocs.io/zh/latest/api/api-test-mitmproxy-guide.html)

性能测试

- [JMeter性能测试：JMeter安装及脚本录制回放](https://devtest-notes.readthedocs.io/zh/latest/perf/performance-testing-using-jmeter.html)
- [JMeter性能测试：JMeter多用户并发模拟及压测结果分析](https://devtest-notes.readthedocs.io/zh/latest/perf/performance-testing-jmeter-concurrency.html)
- [JMeter性能监控系统：Jmeter + InfluxDB + Grafana](https://devtest-notes.readthedocs.io/zh/latest/perf/performance-testing-for-performance-monitoring-system.html)
- [系统性能监控：Prometheus + Grafana 监控服务器性能](https://devtest-notes.readthedocs.io/zh/latest/perf/performance-monitoring-for-server-with-prometheus.html)

安全测试

- [Nmap扫描工具介绍](https://devtest-notes.readthedocs.io/zh/latest/security/api-test-security-testing-nmap-tool.html)
- [hydra暴力破解工具](https://devtest-notes.readthedocs.io/zh/latest/security/api-test-security-testing-hydra-tool.html)
- [Netdiscover网络扫描工具](https://devtest-notes.readthedocs.io/zh/latest/security/api-test-security-testing-netdiscover-tool.html)

持续集成

- [Docker搭建持续集成平台Jenkins](https://devtest-notes.readthedocs.io/zh/latest/CI/container-docker-for-jenkins-install.html)
- [持续集成平台Jenkins介绍](https://devtest-notes.readthedocs.io/zh/latest/CI/continuous-integration-for-jenkins.html)
- [持续集成：jenkins + pytest + selenium + Git + Allure自动化测试](https://devtest-notes.readthedocs.io/zh/latest/CI/continuous-integration-for-jenkins-example.html)
- [持续集成：Jenkins API简单使用](https://devtest-notes.readthedocs.io/zh/latest/CI/continuous-integration-for-jenkins-api.html)
- [使用jenkins实现hexo博客自动发布](https://devtest-notes.readthedocs.io/zh/latest/CI/continuous-integration-for-jenkins-blog-build.html)
- [使用GitHub Actions实现Hexo博客自动发布](https://devtest-notes.readthedocs.io/zh/latest/CI/continuous-integration-for-blog-build-with-github-actions.html)

**下面是我的公众号【测试开发小记】，会不定时发布测试开发相关笔记以及一些读书笔记，欢迎关注。**
<p align="center">
  <a><img src="docs\img\wechat.png" alt="微信公众号" width="30%" height="30%" ></a>
</p>




























