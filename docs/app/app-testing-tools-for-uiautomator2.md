# App自动化测试工具Uiautomator2

[UI Automator](https://developer.android.com/training/testing/ui-automator.html)是 google 在 Android4.1 版本发布时推出的一款用Java编写的Android UI 自动化测试工具，基于Android Accessibility 服务，Accessibility 服务用于帮助残疾用户使用Android设备和应用。在后台运行，并在accesbilityevents触发时接收系统回调。

<!--more-->

UI Automator可以跨进程操作（被测应用和UiAutomator是两个独立的进程），可以对第三方App进行测试，获取屏幕上任意一个APP的任意一个控件属性，并对其进行任意操作。
1. 测试脚本只能使用Java语言
2. 执行时需要将脚本打包成jar或者apk包上传到设备上才能运行

python UIAutomator2是一个可以使用Python对Android设备进行UI自动化操作的库，底层基于Google Ui Automator。其原理是在手机上使用http rpc服务将UiAutomator中的功能开放出来，然后再将这些http接口封装成Python库。本文档介绍UIAutomator2的使用方法。



## uiautomator2安装

uiautomator2的GitHub仓库地址为：[https://github.com/openatx/uiautomator2](https://github.com/openatx/uiautomator2)

python安装：

```sh
pip3 install -U uiautomator2
```
查看是否安装成功
```sh
uiautomator2 --help
```
对于UI元素的查看，可以使用uiautomatorviewer或者Appium inspector，uiautomatorviewer经常用不了，Appium inspector又比较麻烦，推荐一个交weditor的工具，安装简单，使用也方便，直接在浏览器上查看。这三个工具的安装和使用方法可参考这一篇文章：[App控件定位](https://blog.csdn.net/u010698107/article/details/111431111)。

## App初始化

### 连接设备

```python
d = u2.connect_usb(serial) # serial：android设备序列号，通过adb devices命令获取
d = u2.connect(serial) 
d = u2.connect("10.0.0.1") # 通过无线连接设备，10.0.0.1为手机IP地址，需要保证手机和电脑可以相互ping通（连接到同一个局域网）。
d = u2.connect("10.0.0.1:7912") # adb connect 10.0.0.1:5555
```

设置newCommandTimeout和隐式等待
```python
d.set_new_command_timeout(300)  # accessibility服务的最大空闲时间，超时将自动释放
d.implicitly_wait(5)  # 隐式等待，元素查找等待时间（默认20s）
```


### 安装卸载apk

```python
d.app_install('http://some-domain.com/some.apk')
d.app_uninstall("package_name") # 卸载APK
```


### 打开、停止App

打开APP
```python 
d.app_start(appPackage) # appPackage：包名，先通过atx-agent解析apk包的mainActivity，然后调用am start -n $package/$activity启动
d.app_start(appPackage, appActivity) # 指定appPackage和appActivity，其实就是执行adb shell am start -n appPackage/.appActivity
d.app_start(appPackage, appActivity, wait = False, stop = False, use_monkey = False) # wait: 等待app启动 stop：启动app之前先停止（需要appPackage和 appActivity） use_monkey：使用monkey命令启动app（未指定appActivity时可使用此参数）
```

停止APP：

```python
d.app_stop(appPackage) # 强制停止应用，相当于adb shell am force-stop <appPackage>
d.app_clear(appPackage) # 停止并清除应用数据与缓存，相当于adb shell pm clear <appPackage>
d.app_stop_all() # 强制停止所有第三方应用（除了'com.github.uiautomator' 和 'com.github.uiautomator.test'）
d.app_stop_all(excludes=['com.examples.demo']) # 停止除了com.github.uiautomator 和 com.github.uiautomator.test和com.examples.demo以外的应用
```

## 获取设备应用信息

### 获取应用信息
```sh
>>> d.app_info("com.android.settings")
{u'packageName': u'com.android.settings', u'label': u'Param\xe8tres', u'mainActivity': u'com.android.settings.HWSettings', u'versionName': u'10.1.0.300', u'versionCode': 10010300, u'size': 132202855}

# 当前应用信息
>>> d.app_current()
```


### 获取设备信息
```python
>>> d.info
{u'displayRotation': 0, u'displaySizeDpY': 780, u'displaySizeDpX': 360, u'screenOn': True, u'currentPackageName': u'com.android.systemui', u'productName': u'HLK-AL10', u'displayWidth': 1080, u'sdkInt': 29, u'displayHeight': 2224, u'naturalOrientation': True}
>>>
```

获取详细设备信息
```sh
>>> d.device_info
{u'product': None, u'udid': u'SNHVB20C18002195-d8:a4:91:4f:5c:1e-HLK-AL10', u'brand': u'HONOR', u'cpu': {u'hardware': u'Hisilicon Kirin810', u'cores': 8}, u'usingBeganAt': u'0001-01-01T00:00:00Z', u'provider': None, u'owner': None, u'display': {u'width': 1080, u'height': 2340}, u'battery': {u'status': 5, u'scale': 100, u'temperature': 340, u'level': 100, u'acPowered': False, u'usbPowered': True, u'health': 2, u'voltage': 4355, u'wirelessPowered': False, u'technology': u'Li-poly', u'present': True}, u'version': u'10', u'presenceChangedAt': u'0001-01-01T00:00:00Z', u'agentVersion': u'0.10.0', u'memory': {u'total': 5810780, u'around': u'6 GB'}, u'hwaddr': u'd8:a4:91:4f:5c:1e', u'model': u'HLK-AL10', u'arch': u'', u'serial': u'SNHVB20C18002195', u'sdk': 29}
```


获取分辨率：
```sh
>>> d.window_size()
(1080, 2340)
```
获取设备序列号
```sh
>>> d.serial
u'SNHVB20C18002195'
```

获取手机IP地址
```sh
>>> d.wlan_ip
u'192.168.0.191'
```

### 其它

列出所有运行中的APP：
```python
d.app_list_running() # adb shell pm list packages
```

打开网页
```python
d.open_url("https://www.baidu.com") # adb shell am start -a android.intent.action.VIEW -d https://www.baidu.com 
```



## UI元素定位

### 基本选择器

通过属性值定位，支持下面的参数：

- `text`, `textContains`, `textMatches`, `textStartsWith`
- `className`, `classNameMatches`
- `description`, `descriptionContains`, `descriptionMatches`, `descriptionStartsWith`
- `checkable`, `checked`, `clickable`, `longClickable`
- `scrollable`, `enabled`,`focusable`, `focused`, `selected`
- `packageName`, `packageNameMatches`
- `resourceId`, `resourceIdMatches`
- `index`, `instance`

```python
d(className="android.widget.TextView", text="行情")
d(className="android.widget.TextView", textMatches="^行.*")
```

### 相对选择器

子孙节点定位

```python
d(resourceId="android:id/tabs").child(text="行情")
d(resourceId="android:id/tabs").child_by_text("行情")
d(resourceId="android:id/tabs").child_by_description("description")
d(resourceId="android:id/tabs").child_by_instance("instance")
```

兄弟节点定位

```python
d(className="android.widget.ImageView").sibling(text="行情")
```

相对定位

- `d(A).left(B)`： A的左边元素B
- `d(A).right(B)`：A的右边元素B
- `d(A).up(B)`：A的上边元素B
- `d(A).down(B)`：A的下边元素B

![](app-testing-tools-for-uiautomator2/uiautomator2-xueqiu.png)
```python
d(text="雪球").right(text="行情")
d(text="交易").left(text="行情")

```

### 多个实例

查看和选择实例

```python
print(d(className="android.widget.RadioButton").count)
print(len(d(className="android.widget.RadioButton")))
d(className="android.widget.RadioButton")[0].click() # 点击匹配到的第二个元素
```

执行结果：

```python
4
4
```

也可以使用instance参数选择：

```python
d(className="android.widget.RadioButton", instance=1).click() # 使用匹配到的第2个元素
```

### XPath定位

Java uiautoamtor默认不支持xpath，xpath定位是UIAutomator2扩展的一个功能。

```python
d.xpath('//*[@text="行情"]').wait(10.0).click()
d.xpath('//*[@text="行情"]').click()
d.xpath('//*[@text="行情"]').exists
d.xpath('//*[@text="行情"]').all()

```

xpath语法可参考[Web自动化测试：xpath & CSS Selector定位](https://blog.csdn.net/u010698107/article/details/111415888)

## 元素操作方法

### 点击
点击UI元素
```python
ele = d(text="微信")
ele.click(timeout=None, offset=None) # timeout：单位秒，等待元素出现；offset：默认为中心 (0.5, 0.5)
ele.long_click(duration = 0.5, timeout=None) # duration：点击时间；timeout：等待元素出现

ele.click_exists(timeout=10.0)
ele.click_gone(timeout=10.0, interval=1.0) # 
```

点击像素坐标
```python
d.click(x,y) # 点击像素坐标
d.double_click(x, y, duration=0.1) # 双击像素坐标
d.long_click(x, y, duration=0.5) # 长按
```

### 文本输入

文本值获取、输入与清除

```python
d(text="行情").get_text() # 获取元素文本

d(resourceId="com.xueqiu.android:id/action_search").click() # 点击搜索
d(resourceId="com.xueqiu.android:id/search_input_text").set_text("招商银行")  # 输入文本
d(resourceId="com.xueqiu.android:id/search_input_text").clear_text()  # 清除文本输入框文本
```

### 等待wait
等待appActivity出现
```sh
>>> d.wait_activity(".HWSettings", timeout=10)
True
```

等待元素

```python
d(text="Settings").wait(timeout=3.0) # 等待元素出现
d(text="Settings").wait_gone(timeout=1.0) # 等待元素消失
```

### WatchContext

```python
with d.watch_context() as ctx:
    ctx.when("^立即(下载|更新)").when("取消").click() # 当同时出现 （立即安装 或 立即取消）和 取消 按钮的时候，点击取消
    ctx.when("同意").click()
    ctx.when("确定").click()
    # 上面三行代码是立即执行完的，不会有什么等待
    
    ctx.wait_stable() # 开启弹窗监控，并等待界面稳定（两个弹窗检查周期内没有弹窗代表稳定）

    # 使用call函数来触发函数回调
    # call 支持两个参数，d和el，不区分参数位置，可以不传参，如果传参变量名不能写错
    # eg: 当有元素匹配仲夏之夜，点击返回按钮
    ctx.when("仲夏之夜").call(lambda d: d.press("back"))
    ctx.when("确定").call(lambda el: el.click())
```

### Toast操作

手机页面显示toast

```python
d.toast.show("Hello world")
d.toast.show("Hello world", 1.0) # 显示1s
```

获取toast

```python
d.toast.get_message(wait_timeout=5.0, cache_timeout=10.0, "default message") 
assert "Hello world" in d.toast.get_message(5.0, default="") # 断言toast信息
d.toast.reset() # 清除toast缓存
```



### 滑动swipe

根据像素坐标滑动
```python
d.swipe(fx, fy, tx, ty, duration = None, steps = None) # 从(fx, fy)滑到(tx, ty)，1 steps大概5ms，如果设置了steps，会忽略duration参数
```
基于UI对象的滑动
```python
ele = d(text="微信")
ele.swipe(direction, steps=10) # 从UI元素中心开始滑动，direction包括"left", "right", "up", "down" 4个方向。
```

## SwipeExt 扩展功能

```python
d.swipe_ext("right") # 右滑，可选4个方向："left", "right", "up", "down"
d.swipe_ext("right", scale=0.9) # 默认0.9, 滑动距离为屏幕宽度的90%
d.swipe_ext("right", box=(0, 0, 100, 100)) # 在 (0,0) -> (100, 100) 这个区域做滑动

# 实践发现上滑或下滑的时候，从中点开始滑动成功率会高一些
d.swipe_ext("up", scale=0.8) # 代码会vkk

# 还可以使用Direction作为参数
from uiautomator2 import Direction

d.swipe_ext(Direction.FORWARD) # 页面下翻, 等价于 d.swipe_ext("up"), 只是更好理解
d.swipe_ext(Direction.BACKWARD) # 页面上翻
d.swipe_ext(Direction.HORIZ_FORWARD) # 页面水平右翻
d.swipe_ext(Direction.HORIZ_BACKWARD) # 页面水平左翻
```

### 拖动drag_to

```python
d(text="Settings").drag_to(x, y, duration=0.5) # 从Settings UI对象拖动到(x,y)位置
d(text="Settings").drag_to(text="Clock UI", duration=0.2) # 拖动Settings UI对象到Clock UI对象，时间为200ms
```

### 手势操作

手势放大缩小

```python
d(text="Settings").pinch_in(percent=100, steps=10) # 缩小
d(text="Settings").pinch_out() # 放大
```



### UI元素状态和信息

判断UI元素是否存在

```python
d(text="行情").exists
d.exists(text="行情")
d(text="行情").exists(timeout=3)
```

获取元素信息

```python
$ d(text="行情").info
{'bounds': {'bottom': 1274, 'left': 255, 'right': 285, 'top': 1253}, 'childCount': 0, 'className': 'android.widget.TextView', 'contentDescription': None, 'packageName': 'com.xueqiu.android', 'resourceName': 'com.xueqiu.android:id/tab_name', 'text': '行情', 'visibleBounds': {'bottom': 1274, 'left': 255, 'right': 285, 'top': 1253}, 'checkable': False, 'checked': False, 'clickable': False, 'enabled': True, 'focusable': False, 'focused': False, 'longClickable': False, 'scrollable': False, 'selected': True}
```

获取元素坐标

```python
x, y = self.d(text="行情").center() # 元素中心点
x, y = self.d(text="行情").center(offset=(0, 0)) # 元素左上点坐标
```

### 截图

截取UI对象

```python
im = d(text="行情").screenshot()
im.save("行情.jpg")
```

设备截图

```python
d.screenshot("saved.jpg")
d.screenshot().save("saved.png")
cv2.imwrite('saved.jpg', d.screenshot(format='opencv'))
```

## 按键操作

uiautomator2支持一些按键事件，比如home、back等

```python
d.press("home") # 点击home键；也可以使用keycode：d.press(0x03) 效果一样
d.press("back") # 返回；d.press(0x04)
```

按键对应的keycode可以到 [https://developer.android.com/reference/android/view/KeyEvent.html](https://developer.android.com/reference/android/view/KeyEvent.html) 查看。

还支持以下按键名：home、back、left、right、up、down、center、menu、search、enter、delete ( or del)、recent (recent apps)、volume_up、volume_down、volume_mute、camera、power。

其它方法：

```python
d.screen_on() # 点亮屏幕
d.screen_off() # 关闭屏幕
d.info.get('screenOn') # 屏幕是否点亮
d.unlock() # 解锁：点亮屏幕并解锁，需禁用锁屏密码
```

## 命令行操作

获取指定设备的当前包名和activity

```sh
$ python3 -m uiautomator2 --serial SNHVB20C18002195 current
{
    "package": "com.android.settings",
    "activity": ".HWSettings",
    "pid": 11040
}

# python3 -m uiautomator2 可以简写为uiautomator2

$ uiautomator2 --serial SNHVB20C18002195 current
{
    "package": "com.android.settings",
    "activity": ".HWSettings",
    "pid": 11040
}
```

screenshot: 截图
```sh
$ uiautomator2 screenshot screenshot.jpg
```

uninstall： 卸载
```sh
$ uiautomator2 uninstall <package-name> # 卸载一个包
$ uiautomator2 uninstall <package-name-1> <package-name-2> # 卸载多个包
$ uiautomator2 uninstall --all # 全部卸载
```

stop: 停止应用
```sh
$ uiautomator2 stop com.example.app # 停止一个app
$ uiautomator2 stop --all # 停止所有的app
```

## 图像匹配
uiautomator2提供了图像匹配的方法，使用方法如下：

先安装依赖：
```bash
pip3 install -U "uiautomator2[image]" -i https://pypi.doubanio.com/simple
```
提供了 match() 和 click() 两个接口：
```python
img = "target.png" 
d.image.match(img) # 图像匹配。返回一个dict, eg: {"similarity": 0.9, "point": [200, 300]}
d.image.click(imdata, timeout=10) # 点击。轮询查找图片，当similarity>0.9时，执行点击操作
```

作者说这个功能还在完善中，经测试体验确实不是很好。 click()方法点击速度很慢，平均4s才找到图片并完成点击操作。match() 方法基本不能用，页面中没有此图片内容，而返回的相似度也达到99%。

我在[App自动化测试工具Airtest](https://blog.csdn.net/u010698107/article/details/118468631)中介绍了基于图像识别的自动化测试框架Airtest，它在图片识别上操作效率很高，图像匹配速度很快。而airtest、appium和uiautomator2不能一起使用，因为它们使用的uiautomator server不一样，不能同时运行。因此无法直接使用airtest 弥补uiautomator2在图像识别上的缺陷。

那么是否可以只调用airtest图像匹配相关的方法呢？如果你了解Airtest图像识别原理，就知道这肯定是可行的。这里我就不介绍Airtest图像识别具体是怎么实现的了，下面直接给出uiautomator2如何调用Airtest提供的图像识别方法代码。

```python
import uiautomator2 as u2
from airtest.aircv.aircv import *
from airtest.aircv.template_matching import *

class ImageMatch():
    def __init__(self):
        self._device = '127.0.0.1:7555'
        self._appPackage = 'com.xueqiu.android'
        self._appActivity = '.common.MainActivity'

    def init_device(self):
        self.d = u2.connect_usb(self._device)
        self.d.set_new_command_timeout(300)
        self.d.app_start(self._appPackage, self._appActivity)

    def match_img(self, img, threshold=0.8):
        """图片匹配
        :img: 图片，APP中截取的图片
        :threshold: 阈值
        """
        best_match = self._img_matching(img, threshold=threshold)
        try:
            similarity = best_match["confidence"]
            print("相似度: %s" % similarity)
            return similarity
        except Exception as e:
            raise RuntimeError(e)

    def touch_img(self, img, threshold=0.8):
        """根据图片点击
        :img: 图片，APP中截取的图片
        :threshold: 阈值
        """
        best_match = self._img_matching(img, threshold=threshold)
        try:
            self.d.click(*best_match['result'])
        except Exception as e:
            raise RuntimeError(e)

    def _img_matching(self, img, threshold=0.8):
        """在当前页面匹配目标图片
        :img: 目标图片
        :threshold: 相似度阈值
        :return 返回相似度大于阈值的图片信息，例如: {'result': (177, 2153), 'rectangle': ((89, 2079), (89, 2227), (265, 2227), (265, 2079)), 'confidence': 0.7662398815155029, 'time': 0.08855342864990234}
        """
        im_source = self.d.screenshot(format='opencv')
        im_target = imread(img)
        temp = TemplateMatching(im_target, im_source)
        setattr(temp, 'threshold', threshold)
        best_match = temp.find_best_result()
        if best_match is None:
            raise AssertionError("没有匹配到目标图片")
        # print("similarity: %s"%best_match["confidence"])
        return best_match

if __name__ == '__main__':
    im = ImageMatch()
    im.init_device()
    
    img = "target.png"
    im.match_img(img)
    im.touch_img(img)
```

图像匹配的核心代码是 `_img_matching()` 方法，使用了airtest提供的TemplateMatching类，基于kaze算法进行图像识别。

airtest图像匹配效率很高，它提供的图像匹配方法可以弥补uiautomator2在图像匹配上的缺陷。

## pytest + Uiautomator2实例
下面来写一个使用pytest测试框架的小例子。

测试步骤：

1. 打开雪球app
2. 进入行情页面
3. 点击搜索
4. 输入“招商银行”
5. 点击股票代码03968
6. 断言股票价格

Python代码：

```python
#!/usr/bin/python3
# -*-coding:utf-8-*-

import uiautomator2 as u2

class TestU2():
    def setup(self):
        self._device = '127.0.0.1:7555'
        self._appPackage = 'com.xueqiu.android'
        self._appActivity = '.common.MainActivity'

        self.d = u2.connect_usb(self._device)
        self.d.set_new_command_timeout(300)
        self.d.app_start(self._appPackage, self._appActivity)

    def teardown(self):
        # self.d.app_stop(self._appPackage)
        pass

    def test_uiautomator2(self):
        # 点击 行情
        self.d(className="android.widget.TextView", text="行情").click()
        search_ele = self.d(resourceId="com.xueqiu.android:id/action_search").wait(timeout=3.0)
        assert search_ele == True
        
        # 点击 搜索
        self.d(resourceId="com.xueqiu.android:id/action_search").click()
        
        # 输入
         self.d(resourceId="com.xueqiu.android:id/search_input_text").set_text("招商银行")  # set the text

		# 点击 搜索结果
        self.d.xpath('//*[@text="03968"]').wait(3).click()
        
        # 读取股价
        wait_price = self.d(resourceId="com.xueqiu.android:id/current_price")[0].wait(timeout=3.0)
        if wait_price:
            current_price = self.d(resourceId="com.xueqiu.android:id/current_price")[0].get_text()
            assert float(current_price) < 60
        else:
            assert False
```



