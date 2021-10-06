# iOS APP自动化：predicate定位
在iOS APP自动化测试中，最基本的操作就是元素定位了。与Android APP自动化测试一样，iOS也支持 ( XCUITest 或 UIAutomation测试框架) 使用属性值定位，比如id、className等元素属性，然而，有时候属性值并不是唯一的，[appium](http://appium.io/)、[facebook-wda](https://github.com/openatx/facebook-wda)等框架也封装了XPath定位方法，使用XPath和属性值定位方法基本可以定位到99%的元素。但是在性能方面，XPath的定位速度相对较慢，我们可以选择iOS特有的定位策略： predicate 和 class chain定位方法。本文介绍predicate定位方法， class chain定位将在下一篇文章中介绍。

<!--more-->

## Predicate语法

Predicate定位是iOS原生支持的定位方式，定位速度比较快，它可以通过使用多个匹配条件来准确定位某一个或某一组元素。

### 基本比较

| 符号       | 说明     | 示例           |
| ---------- | -------- | -------------- |
| `=`, `==`  | 等于     | name == "通知" |
| `>`        | 大于     | name > 10      |
| `<`        | 小于     | name < 10      |
| `>=`, `=>` | 大于等于 | name >= 10     |
| `<=`, `=<` | 小于等于 | name <= 10     |
| `!=`, `<>` | 不等于   | name != "通知" |



### 集合操作

| 符号           | 说明                       | 示例                                 |
| -------------- | -------------------------- | ------------------------------------ |
| `ANY` , `SOME` | 满足表达式的任意元素       | ANY children.age < 18                |
| `ALL`          | 满足表达式的所有元素       | ALL children.age < 18                |
| `NONE`         | 不包含满足表达式的任意元素 | NONE children.age < 18               |
| `IN`           | 元素在集合中               | name IN { 'Ben', 'Melissa', 'Nick' } |
| `BETWEEN`      | 位于某个范围               | 1 BETWEEN { 0 , 33 }                 |
| array[index]   | 数组array中指定索引的元素  |                                      |
| `array[FIRST]` | 数组中的第一个元素         |                                      |
| `array[LAST]`  | 数组中的最后一个元素       |                                      |
| `array[SIZE]`  | 指定数组大小               |                                      |



### 布尔值

| 符号             | 说明  | 示例 |
| ---------------- | ----- | ---- |
| `TRUEPREDICATE`  | TRUE  |      |
| `FALSEPREDICATE` | FALSE |      |

### 逻辑运算符

| 符号        | 说明   | 示例 |
| ----------- | ------ | ---- |
| `AND`, `&&` | 逻辑与 | `name="通知" AND label="通知"` |
| `OR`,  `||`     | 逻辑或 |      |
| `NOT`, `!` | 逻辑非 | |

### 字符串比较

| 关键字        | 说明             | 示例                     |
| ------------ | ---------------- | ------------------------ |
| `BEGINSWITH` | 以某个字符串开始 | `name BEGINSWITH "屏幕"` |
| `ENDSWITH`   | 以某个字符串结束 | `name ENDSWITH "时间"` |
| `CONTAINS`   | 包含             | `name CONTAINS "使用时间"` |
| `LIKE`       | 通配符      | `name LIKE '*Total: $*' ` |
| `MATCHES` | 正则匹配 | `value MATCHES '.*of 7'` |

默认情况下，字符串比较是大小写和变音敏感的，可以在关键字后面加上`[cd]`，`[c]`不区分大小写，`[d]`表示不区分变音符号。

> 变音符号是附加在字母上的符号，用于提示发音或区分相似的单词。很多语言使用变音符，比如法语、西班牙语等。比如法语单词：Pêche 桃子

## Predicate定位示例
使用[facebook-wda](https://github.com/openatx/facebook-wda)进行元素操作示例：

```python
s = c.session('com.apple.Preferences') # 打开设置

s(predicate='name == "通知"').click()
s(predicate='name IN {"通知"}').click()
s(predicate='name="通知" AND label="通知"').click()

s(predicate='name BEGINSWITH "屏幕"').click() # 点击屏幕使用时间
s(predicate='name ENDSWITH "时间"').click()
s(predicate='name CONTAINS "使用时间"').click()
s(predicate='name LIKE "*使用*"').click()
s(predicate='name MATCHES ".*使用时间$"').click()
s(predicate='name MATCHES "^屏幕.*"').click()

s(predicate='name CONTAINS[c] "apple"').click()

s(predicate='visible==true AND name ENDSWITH "时间"').click()
```

**参考文档：**

1. [http://appium.io/docs/cn/writing-running-appium/ios/ios-predicate/](http://appium.io/docs/cn/writing-running-appium/ios/ios-predicate/)
2. [https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/Articles/pSyntax.html](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Predicates/Articles/pSyntax.html)



