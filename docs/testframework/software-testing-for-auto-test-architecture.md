# 浅谈自动化测试



从事自动化测试工作有一段时间了，今天来简单聊聊。


<!--more-->


我们现在处于信息化时代到智能化时代的转型阶段，加上去年疫情的关系，数字经济迅速发展，比如远程教育、远程办公，网红经济等。各行各业开始数字化转型，国家互联网信息办公室发布的[《数字中国发展报告（2020年）》](http://www.cac.gov.cn/2021-06/28/c_1626464503226700.htm)指出，我国数字经济总量跃居世界第二，软件业务收入从2016年的4.9万亿元增长至2020年的8.16万亿元。

数字产业化和产业数字化离不开软件的支持，现在技术更新迭代很快，企业要满足新消费群体需求，占领市场，必须不断创新，做好产品，提高产品交付质量与效率。在产品开发中，最重要的就是提升软件研发效能，使用瀑布模式已经不能满足产品快速迭代的需求了。近些年提出了一些用于提升开发效率的流程及方法，比如Scrum敏捷（Agile）开发、DevOps、持续交付、持续集成等。这些理念、工具的流行，进一步推动了测试左移和测试右移，软件测试成为敏捷交付的最大瓶颈及挑战，对测试人员的要求也越来越高。

突破这一瓶颈关键在于实现持续测试，持续测试的范畴远远超出了自动化测试，涉及到整个产品开发周期，这里仅谈谈我对自动化测试的理解。

## 软件开发模式


在软件开发中可能会用到TDD(测试驱动开发, Test-Driven Development), BDD(行为驱动开发, Behavior Driven Development）和 ATDD(验收测试驱动开发, Acceptance Test Driven Development)这些工具。

TDD是使用自动化单元测试来推动整个开发的进行，单元测试用例脚本一般由开发人员自己编写，测试人员也可以参与，比如可以提供测试用例、提供关键业务场景等。测试人员需要具备一定的编程能力、逻辑分析能力，这样才能和开发人员设计出更复杂更全面的业务场景用例。

BDD是对TDD的扩展，用于定义行为的语言非常简洁，团队中每个人（开发、QA和业务人员）都能理解。不涉及技术具体如何实现，仅定义系统最终的行为或者系统应该如何行为。判断是否满足需求，易于使用。这有利于规避由于错误理解需求或者不满足需求而产生的BUG，确保每个人理解需求，且保持一致。

ATDD也是在开发之前编写测试用例。整个团队协作定义验收标准，开发过程中，通过适当的测试用例进行验收测试，而验收测试用例是从用户的角度来编写的，这样团队能够灵活地适应项目目标。ATDD/BDD中使用的自动化测试工具中最常用的就是 [Robot Framework](https://robotframework.org/)。当然，也可以使用单元测试框架。

总的来说，TDD侧重于功能具体实现，BDD和ATDD类似，BDD关注系统行为，ATDD更侧重于采集准确的需求。其实这三种软件开发模式都要求测试人员提前介入，测试人员扮演着非常重要的角色，也参与了软件开发的整个生命周期。因此测试人员需要了解大量业务知识及技术，这样才能更好的与开发人员进行合作。

那么自动化测试一般在什么时候介入呢？

## 测试金字塔中的自动化

如果你是软件测试人员，你可能听说过agile开发中的测试金字塔。

![](software-testing-for-auto-test-architecture/test-pyramid.png)

<center><font size="2">图片来源：https://martinfowler.com/bliki/TestPyramid.html</font></center>

在敏捷开发中，应该把更多的测试放在单元测试这一层，单元测试越全面，这个底座越坚固，如图所述成本也会越低。因此在Unit这一层，应该采取TDD开发模式，使用更多的单元测试。

TDD使用的测试框架一般使用[xUnit](https://en.wikipedia.org/wiki/XUnit)框架，比如python语言的unitest、pytest，Java的JUnit、TestNG等。

> xUnit是单元测试框架的总称，其架构来自于Smalltalk的SUnit，SUnit是Kent Beck在1998年设计的。在Smalltalk中引入该框架后，Kent Beck和Erich Gamma将其移植到Java中，最终在当前使用的大多数编程语言中获得了支持。所以将这些语言使用SUnit架构的单元测试框架称为xUnit。——[维基百科](https://en.wikipedia.org/wiki/XUnit)

中间层（service）包括各种API，接受来自UI的请求并返回响应。这一层可以采用BDD和ATDD开发模式。自动化测试中主要使用接口自动化测试，重点在功能。下面介绍一些可能用到的测试工具：

- [Robot Framework](https://robotframework.org/)：可用于接口功能测试
- [Apache JMeter](https://jmeter.apache.org/)：接口功能，也可用于性能测试
- [Postman](https://www.postman.com/)：接口功能测试
- [Requests](https://github.com/psf/requests)：HTTP接口测试库
- [mitmproxy](https://mitmproxy.org/)：基于python的代理工具
- [Charles](https://www.charlesproxy.com/)：支持HTTP代理/ HTTP监控/反向代理
- ......

金字塔最顶层与与用户交互的实际UI了，到了这一层，大部分功能测试已经完成，这一层的测试工作应该是最少的。这一层可以使用的UI自动化测试工具有：

- [Robot Framework](https://robotframework.org/)：可用于UI自动化测试，它包括了大量的测试库，比如seleniumlibrary、appiumlibrary等。
- [Selenium](https://github.com/SeleniumHQ/selenium)：Web自动化测试框架，支持多种语言。
- [playwright](https://playwright.dev/)：微软开发的Web UI自动化测试工具，支持Node.js、Python、C# 和 Java语言。
- [Appium](http://appium.io/)：可用于iOS、 Android和 Windows 桌面平台原生、移动 Web 和混合应用测试，支持多种语言。
- [AirtestProject](https://airtest.netease.com/)：网易游戏推出的一款跨平台的UI自动化测试框架，支持Android原生app、iOS app、微信小程序等UI测试。其中[airtest](https://github.com/AirtestProject/Airtest)是一个基于图像识别的自动化测试框架，[Poco](https://github.com/AirtestProject/Poco)是基于UI元素识别的测试框架。
- [Uiautomator2](https://blog.csdn.net/u010698107/article/details/118468802)：基于Python的Android APP UI自动化测试工具。
- [facebook-wda](https://blog.csdn.net/u010698107/article/details/120396046)：基于Python的 iOS APP UI自动化测试库
- [WebDriverAgent](https://github.com/appium/WebDriverAgent)：Facebook推出的iOS移动测试框架
- [tidevice](https://github.com/alibaba/taobao-iphone-device)：阿里开源的支持运行在Mac，Linux，Windows上，用于与iOS设备进行通信的工具，可以用它来实现在Windows上开展iOS APP自动化测试。
- [Android monkey](https://blog.csdn.net/u010698107/article/details/111437735)：AndroidAPP稳定性测试工具
- [AppCrawler](https://github.com/seveniruby/AppCrawler)：基于appium的稳定性测试工具，支持Android和IOS
- Fastbot：字节开源的稳定性测试工具，包括[Fastbot_Android](https://github.com/bytedance/Fastbot_Android) 和 [Fastbot_iOS](https://github.com/bytedance/Fastbot_iOS)。
- ......

在UI自动化测试中，除了上面提到的测试框架外，还需要学会UI元素定位语法，比如Xpath定位，CSS Selector定位（[参考这里](https://blog.csdn.net/u010698107/article/details/111415888)），iOS应用中的[predicate](https://blog.csdn.net/u010698107/article/details/120318075)、[class chain](https://blog.csdn.net/u010698107/article/details/120395943)等。

通常情况下，基本功能没有问题之后，还会进行非功能测试，比如对Web服务的压力测试、负载测试、接口性能测试，对移动APP的稳定性、H5性能、耗电量、健壮性、弱网测试等。另外还有安全测试，关于相应的工具这里就不一一列举了（主要是我用的比较少）。

要实现CI/CD(持续集成/持续交付) ，在打包、触发测试、部署等环节都要实现自动化。因此，除了上面提到的测试工具，测试人员还需要了解一些持续集成相关工具的使用或者二次开发，比如[jenkins](http://jenkins-ci.org/)、[travis-ci](https://travis-ci.org/) 、容器技术等。如果要自己开发测试管理平台，还得了解一些前端和后端知识，比如数据库、Vue.js、web开发框架等。

## 结语

从上面的介绍可以看出，自动化测试是敏捷测试中的重要组成部分，测试人员需要提高自己的编程和自动化测试技能，培养自己的敏捷测试思维，持续改进测试方法，提升测试效率。

下面总结几点我对开展自动化测试的理解：

1. 开展自动化之前，识别哪些模块需要自动化是有必要的，因为不是每个自动化都有助于提升效率，不要为了自动化而自动化。
2. 测试越早介入越好，如果无法进行单元测试，可以开展更多的接口自动化测试，这样在UI测试中BUG会更少，成本会更低。
3. 不要局限于某个测试工具，只要能满足你的测试需求就可以，但在选择工具时，最好这个工具可以集成到你的持续集成系统中。
4. 没有一套系统平台是可以满足所有业务需求的，需要你根据实际业务来选择，最终目的是实现产品快速迭代。

先说这些了，可能理解的不是很全面，今后再补充。



