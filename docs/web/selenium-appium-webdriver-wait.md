# selenium/appium 等待方式介绍
UI自动化测试过程中，执行某个动作后，页面元素的加载（ajax动态加载）需要一定的时间，selenium WebDriver提供了几种等待方式，Appium也继承了WebDriver API，所以selenium和appium 等待的实现方式相同。下面介绍WebDriver的等待方式。
<!--more-->

## HTML 页面加载
HTML 页面加载、解析过程：
1. 浏览器向服务器发起请求，浏览器先查询本地（浏览器或者本机）DNS缓存，如果没有，向DNS 服务器发起 域名解析请求
2. 浏览器拿到域名对应的IP地址后，建立与服务器的 TCP/IP 连接（3次握手，断开连接进行4次挥手）
3. 向服务器发送 http / https 请求，服务器进行后台内部处理，进行HTTP响应，返回状态和浏览器请求的内容
4. 浏览器接收到http数据包后进行解析
    * 解析HTML页面代码，遇到静态资源（js、css、图片等）则发起请求，过程和前面的步骤一样。
    * 顺序是从上到下进行加载、渲染，下载和渲染同时进行
    * js文件的加载会**阻塞**HTML内容的加载
    * CSS样式表下载完成之后会跟之前的样式表一起进行解析，会对之前的元素重新渲染

渲染过程主要包括以下步骤：
* 解析HTML，生成 DOM Tree
* 同时解析CSS，生成CSS规则树CSSOM
* 合并 DOM 和 CSSOM，生成 Render Tree
* 根据Render Tree进行渲染和展示
* 如果遇到Javascript代码会阻塞渲染，JS执行完成后，浏览器重新渲染
* 遇到`</html>`后结束渲染。

## 强制等待
强制等待，线程休眠一定时间，一般不推荐：
```python
time.sleep(3)
```
## 隐式等待
在服务端等待，设置一个等待时间，轮询查找(默认0.5秒)元素是否出现，如果达到设置的等待时间还没出现就抛出异常。
```python
driver.implicitly_wait(TIMEOUT) # TIMEOUT单位为秒
```
## 显式等待
在客户端等待，在代码中自定义等待条件，可针对于某个特定的元素或者条件设置等待时间，满足条件时继续执行代码。使用WebDriverWait类和expected_conditions类来实现，WebDriverWait类包括了until()和 until_not两种方法，通过判断条件是否为真进行等待，每隔一段时间(默认为0.5秒)进行条件判断，如果条件成立，则执行下一步,否则继续等待，直到超过设置的最长时间。

```python
WebDriverWait(self.driver, timeout, poll_frequency=0.5, ignored_exceptions=None).until(expected_conditions. visibility_of_element_located(LOCATOR))
```
* timeout：超时时间，单位为秒
* poll_frequency：检测的间隔步长，默认为0.5s
* ignored_exceptions：超时后的抛出的异常信息，默认抛出NoSuchElementExeception异常。
* until：当某元素出现或什么条件成立则继续执行。
* until_not：与until相反, 当某元素消失或什么条件不成立则继续执行。

expected_conditions类提供了很多期望条件：
```python
title_is
title_contains
presence_of_element_located
visibility_of_element_located
visibility_of
presence_of_all_elements_located
text_to_be_present_in_element
text_to_be_present_in_element_value
frame_to_be_available_and_switch_to_it
invisibility_of_element_located
element_to_be_clickable
staleness_of
element_to_be_selected
element_located_to_be_selected
element_selection_state_to_be
element_located_selection_state_to_be
alert_is_present
```

也可以使用lambda表达式
```python
WebDriverWait(driver, timeout).until(lambda x:x.find_element_by_id("someld") 
```
示例代码：
```python
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def test_wait(self):
    self.driver.find_element(By.XPATH,'the_xpath_path1').click()
    ## 方法1
    def wait(x):
    # 定义等待条件
    	return self.driver.find_elements(By.XPATH,'the_xpath_path2')
    WebDriverWait(self.driver, 10).until(wait)
    WebDriverWait(self.driver, 10).until_not(wait)    
    
    ## 方法2
    WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(By.XPATH, 'the_xpath_path2'))
    ##  方法3
    WebDriverWait(self.driver, 10).until(lambda x:x.find_element_by_id("someld")	
```

## 小结
WebDriver隐式等待和显式等待可参考官方文档：[https://selenium-python.readthedocs.io/waits.html](https://selenium-python.readthedocs.io/waits.html)， 本文介绍了三种等待方式：
* 强制等待：一般不推荐
* 隐式等待：尽量默认都加上，时间限定在3-6s，不要太长。
* 显式等待：用来处理隐式等待无法解决的一些问题，显式等待时间可以设置长一点

除了上面介绍的三种等待方式，WebDriver还有两个等待方法：set_script_timeout和set_page_load_timeout。
set_script_timeout设置等待execute_async_script（Javascript / AJAX 调用 ）执行完成，set_page_load_timeout设置等待页面加载完成。
```python
driver.set_script_timeout(5)
driver.set_page_load_timeout(5)
```



