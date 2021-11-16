# markdown基本语法介绍
目前主要使用typora进行来笔记整理，使用MarkDown编辑文章非常方便简洁，我的[Hexo博客](https://hiyong.gitee.io/)就是使用MarkDown来编写的，本文整理常用的Markdown语法以及与HTML的混用。

<!--more-->

## MarkDown基本语法
### 目录
* **[横线](#横线)**
* **[标题](#标题)**
* **[段落](#段落)**
* **[文本](#文本)**
    * [文字高亮](#文字高亮)
    * [换行](#换行)
    * [斜体、粗体、删除线](#斜体、粗体、删除线)
* **[引用](#引用)**
    * [引用分段](#引用分段)
    * [引用嵌套](#引用嵌套)
    * [引用中使用其它语法](#引用中使用其它语法)
* **[列表](#列表)**
    * [无序列表](#无序列表)
    * [有序列表](#有序列表)
* **[代码块](#代码块)**
* **[链接](#链接)** 
    * [链接格式化](#链接格式化)
    * [图片链接](#图片链接)
    * [参考链接](#参考链接)
* **[锚点](#锚点)**
* **[图片](#图片)**
* **[表格](#表格)**
    * [对齐](#对齐)
    * [使用其他语法](#使用其他语法)
* **[复选框](#复选框)**
* **[表情](#表情)**
* **[diff语法](#diff语法)**
* **[字符转义](#字符转义)**
* **[HTML](#HTML)**
* **[typora](#typora)**
* **[CSDN和博客园图片大小和居中设置](#CSDN和博客园图片大小和居中设置)**
    * [CSDN](#CSDN)
    * [博客园](#博客园)

### 横线

`***、---、___`可以显示横线效果，注意横线前后要加一个空行。
___

### 标题

| Markdown        | HTML              |
| --------------- | ----------------- |
| # 一级标题      | `<h1>一级标题</h1>` |
| ## 二级标题     | `<h2>二级标题</h2>` |
| ### 三级标题    | `<h3>三级标题</h3>` |
| #### 四级标题   | `<h4>四级标题</h4>` |
| ##### 五级标题  | `<h5>五级标题</h5>` |
| ###### 六级标题 | `<h6>六级标题</h6>` |

一级标题和二级标题也可以分别通过在标题文字下面添加`==`和`--`来实现。`=`和`-`个数大于等于2就可以。
```markdown
一级标题 
==

二级标题 
--
```

### 段落
分段使用空行就行了


### 文本

#### 文字高亮
可以使用一对反引号来突出部分文字：

| 语法                                                         | 效果     |
| ------------------------------------------------------------ | -------- |
| `==高亮==`：typora中的markdown扩展语法，<br />需要开启才可使用 | ==高亮== |
| ```linux` ``                                                 | `linux`  |



#### 换行
在上一行文本后面补两个空格（大于大于2个空格），  
这样下一行的文本就换行了。

HTML语法：

| 语法                          | 效果 |
| ----------------------------- | ---- |
| `<p>第一行<br>第二行</p>` | <p>第一行<br/>第二行</p> |

在两行文本直接加一个空行会分段。
#### 斜体、粗体、删除线

|Markdown语法|HTML语法|效果|
|----|-----|----|
|`*斜体1*`|`<em>斜体</em>`|*斜体1*|
|`_斜体2_`|| _斜体2_|
|`**粗体1**`|`<strong>粗体</strong>`|**粗体1**|
|`__粗体2__`||__粗体2__|
|`这是一个 ~~删除线~~`||这是一个 ~~删除线~~|
|`***斜粗体1***`|`<strong><em>斜粗体</em></strong>`|***斜粗体1***|
|`___斜粗体2___`||___斜粗体2___|
|`__*斜粗体3*__`||__*斜粗体3*__|
|`**_斜粗体4_**`||**_斜粗体4_**|
|`***~~斜粗体删除线1~~***`||***~~斜粗体删除线1~~***|
|`~~***斜粗体删除线2***~~`||~~***斜粗体删除线2***~~|
|Markdown没有下划线语法|`<u>下划线</u>`|<u>下划线</u>|

斜体、粗体、删除线可混合使用  
**粗体和斜体建议使用星号**


### 引用
在引用段落前面添加符号`>`。

#### 引用分段
```markdown
> 段落1
>
> 段落2
```
> 毫不犹豫地，监听员按下了发射键，高功率电波带着那条简短但可能拯救另一个文明的信息飞向黑暗的太空：
这个世界收到了你们的信息。
> 
> 我是这个世界的一个和平主义者，我首先收到信息是你们文明的幸运，警告你们：不要回答！不要回答！不要回答！！！
> 
> 你们的方向上有千万颗恒星，只要不回答，这个世界就无法定位发出源。
> 如果回答，发射器将被定位，你们的文明将遭到入侵，你们的世界将被占领！
> 不要回答！不要回答！！不要回答！！！

#### 引用嵌套
```markdown
> 不要回答！
>> 不要回答！！
>>> 不要回答！！！
```

> 不要回答！
> > 不要回答！！
> >
> > > 不要回答！！！

#### 引用中使用其它语法
```
> ## 监听员
> 毫不犹豫地，监听员按下了发射键，高功率电波带着那条简短但可能拯救另一个文明的信息飞向黑暗的太空：
> 这个世界收到了你们的信息。
>
> 我是这个世界的一个和平主义者，我首先收到信息是你们文明的幸运，警告你们：
> - 不要回答！
> - 不要回答！
> - 不要回答！！！
>
> 你们的方向上有千万颗恒星，只要不回答，这个世界就无法定位发出源。
> 如果回答，发射器将被定位，你们的文明将遭到入侵，你们的世界将被占领！
> **不要回答！**
>
> 不要回答！！
>
> 不要回答！！！
```

### 列表
#### 无序列表
无序列表可以使用短横杠 (`-`), 星号 (`*`), 或者加号 (`+`)
```markdown
* 不要回答！
- 不要回答！！
+ 不要回答！！！
```
html语法：
```html
<ul>
<li>不要回答！</li>
<li>不要回答！！</li>
<li>不要回答！！！</li>
</ul>
```

效果：
* 不要回答！
- 不要回答！！
+ 不要回答！！！


多级无序列表
```markdown
* 不要回答！
    * 不要回答！！
```
效果：
* 不要回答！
    * 不要回答！！

#### 有序列表
在数字后面加一个点，再加一个空格。

```markdown
我是这个世界的一个和平主义者，我首先收到信息是你们文明的幸运，警告你们：
1. 不要回答！
2. 不要回答！
3. 不要回答！！！
```
html语法：
```html
<ol>
<li>First item</li>
<li>Second item</li>
<li>Third item</li>
</ol>
```
**效果：**
我是这个世界的一个和平主义者，我首先收到信息是你们文明的幸运，警告你们：  
1. 不要回答！
2. 不要回答！
3. 不要回答！！！

注意：数字可以不按顺序，渲染时会自动按数字顺序列出。

**多级有序列表**
```markdown
1. 不要回答！
       1. 不要回答！
2. 不要回答！！！
```

效果
1. 不要回答！
		1. 不要回答！
2. 不要回答！！！


### 代码块
- 缩进四个空格或一个Tab制表符。
- 在列表中时，缩进八个空格或两个Tab制表符。
- 三个反引号后面加上编程语言的名字（也可以不加），另起一行开始写代码，最后一行再加上三个反引号。


```python
print("hello world")
```

```Bash
echo "hello world" #Bash
```

要将文字表示为代码，用单个反引号将其括起来。例如：`Linux`

html语法：

```html
<code>Linux</code>
```

如果代码块内有反引号，可以使用两个反引号来转义：

``要将文字表示为代码，用单个`反引号`将其括起来。``

```html
<code>要将文字表示为代码，用单个`反引号`将其括起来。</code>
```

### 链接

**注意**：URL中如果有空格，使用`%20`进行URL编码。

链接地址可以是URL链接，也可以是本地文件路径。

|#|markdown语法|HTML语法|效果|
|---|----|-----|---|
|1|`[CSDN地址](https://blog.csdn.net/u010698107 "悬停显示：我的CSDN博客")`|`<a href="https://blog.csdn.net/u010698107 " title="悬停显示：我的CSDN博客">CSDN地址</a>`|[CSDN地址](csdn.png "悬停显示：我的CSDN博客")|
|2|`[我的文档](./example/testfile.md)`||[我的文档](./example/testfile.md)|

也可以直接在URL或者邮箱地址两边加尖括号将地址快速转化为链接：

```markdown
<https://blog.csdn.net/u010698107>
```

效果：<https://blog.csdn.net/u010698107>

#### 链接格式化

也可以对链接进行格式化，比如加粗，斜体等

```markdown
我的CSDN地址是：**[CSDN地址](https://blog.csdn.net/u010698107)**
我的CSDN地址是：*[CSDN地址](https://blog.csdn.net/u010698107)*
回到[`目录`](#目录)

```

#### 图片链接

图片链接[ ]里面是要显示的图片。  

`````
![](markdown-basic-syntax//img/csdn.png "我的CSDN")
`````

| #        | 语法                                                         | 效果                                                         |
| -------- | ------------------------------------------------------------ | ------------------------------------------------------------ |
![](markdown-basic-syntax/https://img-home.csdnimg.cn/images/20201124032511.png "我的CSDN")
| HTML     | `<a href="https://blog.csdn.net/u010698107" ><img src="https://img-home.csdnimg.cn/images/20201124032511.png"  alt="csdn" title="我的CSDN"></a>` | <a href="https://blog.csdn.net/u010698107" ><img src="csdn.png"  alt="csdn" title="我的CSDN"></a> |

鼠标悬停图标时显示的文字是图片的title

#### 参考链接

参考链接包括两部分：  

- 与文本保持内联的部分
- 存储在文件其他地方以使文本易于阅读的部分。

```markdown
[blog]:https://hiyongz.github.io/ "我的博客"

[我的博客][blog] 
# 或者
[blog][]
```

效果：
- [我的博客][blog]
- [blog][]

[blog]:https://hiyongz.github.io/ "我的博客"

### 锚点

每一个标题都是一个锚点，和HTML的锚点（`#`）类似，可以用它来实现页面内跳转。 

|#|语法|效果|
|---|---|---|
|markdown|`[目录](#目录 "悬停显示")`|[目录](#目录 "悬停显示")|
|HTML|`<a href="#目录" title="悬停显示">目录</a>`|<a href="#目录" title="悬停显示">目录</a>|

> 其中title可以不用设置。

也可以使用和参考链接一样的方式：
```css
[文章目录]: #目录

[目录][文章目录]
[文章目录][]
```
效果：

[目录][文章目录]
[文章目录][]

[文章目录]: #目录

### 图片

语法：
```markdown
![](markdown-basic-syntax/URL title)
```
alt和title对应HTML中的alt和title属性（都可省略）：
- alt表示图片显示失败时的替换文本
- title表示鼠标悬停在图片时的显示文本，注意要加引号。
- URL为图片的url地址，如果引用本仓库中的图片，直接使用**相对路径**。

|#|语法|效果|
|---|---|----|
![](markdown-basic-syntax/https://img-home.csdnimg.cn/images/20201124032511.png "CSDN logo")
|HTML|`<img src="https://img-home.csdnimg.cn/images/20201124032511.png" alt="CSDN" title="CSDN logo">`|<img src="csdn.png" alt="CSDN" title="CSDN logo"> |


### 表格
```markdown
| 表头1 | 表头2 | 表头3 |
| ----- | ----- | ----- |
| value | value | value |
| value | value | value |
```


#### 对齐
指定对齐方式
```markdown
| 左对齐 |   居中    | 右对齐 |
| :---- |:---------:| -----:|
|  left |  entered  | right |
|  left | centered  | right |
|  left | centered  | right |
```

效果：

| 左对齐 |   居中    | 右对齐 |
| :---- |:---------:| -----:|
|  left |  entered  | right |
|  left | centered  | right |
|  left | centered  | right |

#### 使用其他语法
表格单元中的内容可以可以使用其Markdown语法，如：  加粗、斜体、删除线等

| 表头1 |  表头2  |
| :---: |:---------:|
| <u>下划线</u> |  **加粗**  |
| ***斜体加粗*** | _斜体_ |
| `代码` | ~~~删除线~~~ |

### 复选框

语法：

```markdown
- [x] Python
- [ ] Java
```
效果：

- [x] Python
- [ ] Java

可以点击复选框来勾选或解除勾选，如果想要固定它，使它不可勾选，可以使用HTML语法：

```html
<p><input type="checkbox" name="category" checked disabled/> Python </p>
<p><input type="checkbox" name="category" disabled/> Java </p>
```

<p><input type="checkbox" name="category" checked disabled/> Python </p>
<p><input type="checkbox" name="category" disabled/> Java </p>

### 表情

Github的Markdown语法支持添加emoji表情，每个表情对应一个符号码（两个冒号包围的字符），比如`:laughing:`，:laughing:

所有支持的表情符号码，可以查询网页：[http://www.emoji-cheat-sheet.com](http://www.emoji-cheat-sheet.com)。

下面举几个例子：

|   语法   | 图标  |   语法   | 图标 |    语法    |  图标 |
| :--------: | :------: | :--------: | :------: | :----------: | :--------: |
| `:heart_eyes:` | :heart_eyes: | `:smile:`  | :smile:  | `:laughing:` | :laughing: |
| `:blush:`  | :blush:  | `:smiley:` | :smiley: | `:relaxed:`  | :relaxed:  |
|`:sunny:`|:sunny:|`:umbrella:`|:umbrella:|`:cloud:`|:cloud:|
|`:snowflake:`|:snowflake:|`:snowman:`|:snowman:|`:zap:`|:zap:|
|`:bamboo:`|:bamboo:|`:gift_heart:`|:gift_heart:|`:dolls:`|:dolls:|
|`:school_satchel:`|:school_satchel:|`:mortar_board:`|:mortar_board:|`:flags:`|:flags:|
|`:house:`|:house:|`:house_with_garden:`|:house_with_garden:|`:school:`|:school:|
|`:office:`|:office:|`:post_office:`|:post_office:|`:hospital:`|:hospital:|
|`:one:`|:one:|`:two:`|:two:|`:three:`|:three:|
|`:four:`|:four:|`:five:`|:five:|` :six:`| :six:|

### diff语法

GitHub 风格标记中的差异格式，在三个反引号后面写diff，内容中， `+ `开头表示新增，`- `开头表示删除。

```diff
-oldLine 
+newLine 
```

### 字符转义
如果要显示用于格式化Markdown文档的特殊字符，需要使用反斜杠（`\`）进行转义。

| Character |
| --------- |
| \         |
| `         |
| *         |
| _         |
| { }       |
| [ ]       |
| < >       |
| ( )       |
| #         |
| +         |
| -         |
| .         |
| !         |
| \|        |


### HTML
在前面介绍的Markdown语法中，我也列出了对应的HTML语法格式，许多Markdown应用都支持在Markdown文本中使用HTML语法。

有些时候HTML语法更好用，在需要更改元素的属性时，比如指定文本的颜色或更改图像的大小，需要使用到HTML语法。

| 语法                                                         | 效果                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| `<img src="./img/wechat.png" style="zoom:10%;"/>`            | <img src="wechat.png" style="zoom:10%;" />                   |
| `<center><font size="2">https://blog.csdn.net/u010698107</font></center>` | <center><font size="2">https://blog.csdn.net/u010698107</font></center> |
| `<font color="red">红色</font>`                              | <font color="red">红色</font>                                |
| `<div style="color:red">蓝色</div>`                          | <div style="color:blue">蓝色</div>                           |

<div style="color:blue">蓝色</div>

<center><font size="2">https://blog.csdn.net/u010698107</font></center>

### typora

typora是一个Markdown编辑器，我在[typora主题配置：公众号一键排版](https://blog.csdn.net/u010698107/article/details/117059599)中介绍了它的CSS样式使用方法，下面介绍一下typora的快捷键。

| 快捷键          | 说明         |
| --------------- | ------------ |
| ctrl+=          | 提高标题级别 |
| ctrl+-          | 降低标题级别 |
| ctrl+数字(1-6)  | 1-6级标题    |
| ctrl + B        | 加粗         |
| ctrl + I        | 斜体         |
| ctrl + U        | 下划线       |
| alt + shift+ 5  | 删除线       |
| ctrl + shift+ [ | 有序列表     |
| ctrl + shift+ ] | 无序列表     |
| ctrl + shift+ K | 多行代码块   |
| ctrl + shift+ I | 插入图片     |
| ctrl + K        | 链接         |
| ctrl + T        | 插入表格     |

### CSDN和博客园图片大小和居中设置

#### CSDN

设置图片大小，在图片url后面添加

```markdown
#pic_left 
#pic_center
#pic_right
```
```markdown
![](markdown-basic-syntax/https://img-blog.csdnimg.cn/img_convert/74dad4531df32c064c411b63dec66db1.png#pic_center =300x)
```
- =300x：指定宽为300，不指定高，自动缩放
- 如果要指定宽和高：=300x100
- 注意=前面有空格

#### 博客园
语法：
```markdown
<div align=center>
<img src="https://img2020.cnblogs.com/blog/2229336/202105/2229336-20210519222822372-875961918.png" width="40%" height="40%">
</div>
```

```text
align=center # 居中
align=left # 左对齐
align=right # 右对齐
```

****

|作者|hiyongz|
|---|---|
|个人博客|[博客地址](https://hiyongz.github.io/)|
|CSDN博客|[CSDN](https://blog.csdn.net/u010698107)|
|博客园|[博客园](https://www.cnblogs.com/hiyong/)|
|微信公众号|<img src="wechat.png" style="zoom:10%;" />|


****







