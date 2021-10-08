# iOS APP自动化：class chain定位方法

在[iOS APP自动化：predicate定位](https://blog.csdn.net/u010698107/article/details/120318075)中介绍了iOS APP的predicate定位方法，本文介绍与XPath语法比较类似的class chain定位方法。


## class chain 定位
class chain 定位方法由**[mykola-mokhnach](https://github.com/mykola-mokhnach)**开发，和XPath比较类似，可以实现分层查询，但它的查询性能更高，通过将class chain查询映射到一系列的XCUITest调用中，仅查找子节点，不像XPath那样递归地查询整个UI树。

class chain 支持Predicate字符串匹配，下面介绍class chain 定位方法。

### 儿子节点搜索

选择儿子元素，类似于XPath语法中的反斜杠`/`。

```bash
XCUIElementTypeWindow[`label BEGINSWITH "text"`][-1] # 选择label以foo开头的最后一个
XCUIElementTypeWindow/XCUIElementTypeButton[3] # 选择window的儿子元素XCUIElementTypeButton的第3个（索引从1开始）
XCUIElementTypeWindow/*[3]  # 选择window的第3个儿子元素
XCUIElementTypeWindow # 选择所有子窗口
XCUIElementTypeWindow[2] # 选择第二个窗口
XCUIElementTypeWindow[2]/XCUIElementTypeAny # 选择第二个子窗口的所有子元素
```



### 子孙节点搜索

类似于XPath语法中的双反斜杠`//`

```bash
**/XCUIElementTypeCell[`name BEGINSWITH "A"`][-1]/XCUIElementTypeButton[10] # 选择name以A开头的最后一个Cell元素的第10个子元素
**/XCUIElementTypeCell[`name BEGINSWITH "B"`] # 选择name以B开头的所有Cell元素
**/XCUIElementTypeCell[`name BEGINSWITH "C"`]/XCUIElementTypeButton[10] # 选择name以C开头的第一个Cell元素的第10个子元素
**/XCUIElementTypeCell[`name BEGINSWITH "D"`]/**/XCUIElementTypeButton # 选择name以D开头的第一个Cell元素下所有后代Button
```

使用class chain定位是需要注意以下几点：
- Predicate字符串要写到中括号中，并且使用反引号包裹。
- Predicate表达式应该写在索引前面

## class chain定位示例
使用[facebook-wda](https://github.com/openatx/facebook-wda)进行元素点击操作：

```python
s = c.session('com.apple.Preferences') # 打开设置

s(classChain='XCUIElementTypeWindow/**/XCUIElementTypeCell[`label BEGINSWITH "屏幕"`]').click() # 点击【屏幕使用时间】
s(classChain='**/XCUIElementTypeCell[`label BEGINSWITH "屏幕"`]').click()
s(classChain='**/XCUIElementTypeTable/*[`name == "通知"`]').click() # 点击【通知】
s(classChain='**/XCUIElementTypeCell[7]').click() # 点击【通知】
```

上面的定位语句也可以使用XPath语法，对应如下：
```python
s(xpath='//XCUIElementTypeWindow//XCUIElementTypeCell[starts-with(@label,"屏幕")]').click()
s(xpath='//XCUIElementTypeCell[starts-with(@label,"屏幕")]').click()
s(xpath='//XCUIElementTypeTable/*[@name="通知"]').click()
s(xpath='//XCUIElementTypeCell[7]').click()
```

XPath定位效率比class chain低，建议使用class chain来进行定位。

**参考文档：**

1. [https://github.com/facebookarchive/WebDriverAgent/wiki/Class-Chain-Queries-Construction-Rules](https://github.com/facebookarchive/WebDriverAgent/wiki/Class-Chain-Queries-Construction-Rules)

2. [https://github.com/appium/appium-xcuitest-driver/pull/391](https://github.com/appium/appium-xcuitest-driver/pull/391)

