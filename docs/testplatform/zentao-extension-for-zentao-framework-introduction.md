# 禅道二次开发（二）：禅道框架介绍


进行禅道二次开发前有必要学习一下禅道使用的框架，本文将简单介绍zentaoPHP框架以及禅道的目录结构。


## zentaoPHP框架

禅道项目使用zentaoPHP框架，基于b/s架构开发。

### 基本原理

zentaoPHP框架支持MVC（Model-View-Controller）软件架构模式，把软件系统分为三个基本部分：

- 模型（Model）：实现程序的功能、数据管理和数据库设计。对数据库的增删改查可以放在这一层。
- 控制器（Controller）：负责转发用户请求，对请求进行处理，组织各种业务逻辑，准备数据。
- 视图（View）：负责渲染数据，图形界面设计，通过HTML方式呈现给用户。

zentaoPHP框架的基本原理：

1. 通过apache服务将请求转交给index.php（`\zentao\app\htdocs\index.php`），由它来进行资源调度。
2. index.php加载框架文件，初始化应用，解析URI请求，得到请求对应对模块名、方法和参数。比如URL：`<zentao-url>/zentao/testcase-browse-1.html` 模块名为testcase，方法名为browse，1为参数。
3. 然后加载相应模块的control方法，model方法，然后渲染模板（view文件）、呈献给用户。

### 数据库操作

zentaoPHP框架提供了用于操作数据库的对象类DAO，在`\lib\dao\dao.class.php` 中定义，加载框架时会自动生成 `$this->dao` 对象，可以在control, model，view层直接使用 `$this->dao` 来执行各种方法。

查询数据库使用 `fetch` 系列方法，增删改相关方法使用 `exec()` 方法。

比如禅道中查询所有用例：

```php
$this->dao->select('*')->from(TABLE_CASE)
    ->where('deleted')->eq(0)
    ->fetchAll('id');
```

插入用例：

```php
$this->dao->insert(TABLE_CASE)->data($case)->autoCheck()->exec();
```

更新用例：

```php
$this->dao->update(TABLE_CASE)->data($case)->autoCheck()->where('id')->eq((int)$caseID)->exec();
```

删除用例：

```php
$this->dao->delete()->from(TABLE_CASE)->where('id')->eq($Caseid)->exec();
```

### 数据验证

zentaoPHP将数据验证放在了model层，提供了数据过滤的方法，包括了数据修正和数据验证。过滤方法在 `\lib\filter\filter.class.php` 文件中定义。

数据修正以禅道testcase模块创建用例方法为例，查看`\module\testcase\model.php`中的create方法：

```php
$case   = fixer::input('post')
    ->add('status', $status)
    ->add('version', 1)
    ->add('fromBug', $bugID)
    ->setDefault('openedBy', $this->app->user->account)
    ->setDefault('openedDate', $now)
    ->setIF($this->config->systemMode == 'new' and $this->app->tab == 'project', 'project', $this->session->project)
    ->setIF($this->app->tab == 'execution', 'execution', $this->session->execution)
    ->setIF($this->post->story != false, 'storyVersion', $this->loadModel('story')->getVersion((int)$this->post->story))
    ->remove('steps,expects,files,labels,stepType,forceNotReview')
    ->setDefault('story', 0)
    ->cleanInt('story,product,branch,module')
    ->join('stage', ',')
    ->get();
```

- 首先调用fixer类的input方法，参数post表示是从`$_POST` 这个变量中获取数据。
- `add()`方法是向数据中增加变量。
- `setDefault()`方法表示当这个变量没有传值的时候，设成默认值。
- `setIF()` 方法第一个参数是判断条件，后面两个分别是key和value。当条件为true时，设置`$key = $value`。
- `remove()` 方法用于删除不需要的字段。
- `cleanInt()`将变量转换为int类型。
- `join('stage', ',')`将stage使用`,`连接起来。
- get方法返回一个经过修正的数据集合。

数据验证使用check相关方法：

```php
$this->dao->insert(TABLE_CASE)->data($case)
    ->autoCheck()
    ->batchCheck($this->config->testcase->create->requiredFields, 'notempty')
    ->exec();
```

data方法将修正过的数据传递给dao对象，然后通过autoCheck()对其进行自动检查。batchCheck()方法会对一批字段进行非空的验证。

使用`dao::isError()`判断是否有错误，`dao::getError()`方法获取报错信息。

### 分页

以测试用例浏览页面为例，在testcase模块的control文件中的browse方法完成分页的功能，相关代码如下：

```php
public function browse($recTotal, $recPerPage, $pageID)
{
    /* Load pager. */
    $this->app->loadClass('pager', $static = true);
    $pager = new pager($recTotal, $recPerPage, $pageID);
    $sort  = common::appendOrder($orderBy);

    /* Get test cases. */
    $cases = $this->testcase->getTestCases($productID, $branch, $browseType, $browseType == 'bysearch' ? $queryID : $suiteID, $moduleID, $sort, $pager);
    if(empty($cases) and $pageID > 1)
    {
        $pager = pager::init(0, $recPerPage, 1);
        $cases = $this->testcase->getTestCases($productID, $branch, $browseType, $browseType == 'bysearch' ? $queryID : $suiteID, $moduleID, $sort, $pager);
    }
}
```

分页相关的参数主要包括recTotal, recPerPage和pageID这三个参数。

在model中定义的`getTestCases`方法，接收`pager`对象，并在dao查询的时候，调用`pager($pager)`方法来生成分页语句，返回用例数据: 

```php
public function getTestCases($pager)
{
    return $this->dao->select(*)->from(TABLE_PROJECTCASE)->page($pager)->fetchAll();
}
```

然后将pager对象和用例数据赋值给view模板：

```php
public function browse($recTotal, $recPerPage, $pageID)
{
    /* Load pager. */

    /* Get test cases. */
    
    /* 赋值到模板。*/
    $this->view->pager           = $pager;
    $this->view->cases           = $cases;
}
```

在view模板中调用show()方法显示分页链接：

```php
<?php $pager->show('right', 'pagerjs');?>
```

### 其它

zentaoPHP还提供了一些方法，比如生成链接方法`createLink()`，重定向`locate()`，加载指定模块`loadModel()` 等。

还提供了html，js和css类，其中html类可用于生成html标签：

- `html::a($href, $title, $target, $misc)`，生成超链接。
- `html::input($name, $value, $attr)` 生成文本框。
- `html::select($name, $options, $selected, $attr)`，生成select标签。
- ......

JS类提供了一些js方法，比如：

- `js::alert($message)`：生成一个警告框。
- `js::locate($url, $target)`：页面跳转。
- `js::reload($window)`：窗口重载。

上面仅对zentaoPHP框架进行了简单介绍，更详细内容可参考官方文档，

下面介绍禅道的基本目录结构。

## 禅道目录结构

在[禅道二次开发（一）：开发环境配置](https://blog.csdn.net/u010698107/article/details/123319019)中介绍了在Linux中安装禅道的方法，这里介绍一下它的主要目录结构。

### 顶级目录

进入`/opt/zbox/app/zentao` 目录，禅道目录结构如下：

```bash
.
├── api
├── bin
├── config
├── db
├── doc
├── framework
├── lib
├── module
├── sdk
├── tmp
└── www

```

- `api`：接口目录。
- `bin`：存放禅道的一些命令行脚本。
- `config`：存放禅道运行的主配置文件和数据库配置文件。
- `db`：历次升级的数据库脚本和完整的建库脚本。
- `doc`：文档。
- `framework`：框架核心目录，禅道php框架的核心类文件，里面包含了router, control, model和helper的定义文件。
- `lib`：常用的类。比如html，js和css类、数据库DAO类、数据验证fixer类等。
- `module`：模块目录，存放具体的功能模块。
- `sdk`：PHP sdk类。
- `tmp`：存放禅道程序运行时的临时文件。
- `www`：存放各种样式表文件，js文件，图片文件，以及禅道的入口程序`index.php`。

### config目录

`config` 目录存放禅道配置文件。

```bash
.
├── config.php
├── ext
├── filter.php
├── index.html
├── my.php
├── routes.php
├── timezones.php
└── zentaopms.php

```

- `config.php`：ZenTaoPHP的config文件
- `ext`：扩展目录
- `filter.php`：数据过滤规则文件
- `my.php`：可以覆盖config.php中的配置
- `routes.php`：API路由
- `timezones.php`：时区
- `zentaopms.php`：配置文件，存放了数据库的定义。

### www目录

```bash
.
├── api.php
├── checktable.php
├── data
├── favicon.ico
├── index.php
├── init.php
├── js
├── ok.txt
├── robots.txt
├── theme
├── tip4japanese.html
└── x.php

```

- `data`：上传附件所在的目录。
- `js`：存放js脚本文件，禅道用到的各种jquery插件和相应的功能函数。
- `theme`：主题文件，包含了css文件和图片文件。
- `.htaccess`：apache下面使用的url重写规则文件。
- `favicon.ico`：禅道图标文件
- `index.php`：整个禅道的入口程序，所有的请求都是通过index.php来进行转发。

### module目录

module目录下面的模块分别对应了禅道里面的某一个功能模块。整个禅道的功能，就是由这些模块组合而成。部分功能模块：

```bash
.
├── bug
├── caselib
├── common
├── execution
├── task
├── qa
├── testcase
├── testreport
├── testsuite
└── testtask
```

#### testcase模块

以测试用例模块testcase为例，目录结构如下：

```bash
.
├── config.php
├── control.php
├── css
├── ext
├── js
├── lang
├── model.php
└── view
```

- `config.php`：存放当前模块的配置项，也可以覆盖全局性的配置。
- `control.php`：模块对应的控制器类文件。是整个testcase模块所有页面的入口。也就是说，testcase相关的页面浏览都可以在这个文件里面找到相应的方法定义。
- `model.php`：模块对应的业务逻辑类文件，提供testcase相关数据库操作方法。
- `view`：存放的各个方法的视图文件。比如testcase浏览页面，对应的模板就是browse.html.php。
- `css`：testcase模块的样式表文件。
- `js`：testcase模块的Javascript脚本文件。
- `lang`：存放testcase模块的语言文件。zh-cn对应中文简体，zh-tw中文繁体，以此类推。如果需要修改禅道里面某些字段的名称或者配置，修改相应的文件即可。
- `ext`：二次开发文件存放目录

#### common公用模块

common公用模块里面存储的是禅道的公用功能，比如公用的语言文件、模板文件、model文件等。

- `common/model.php` 提供了其他模块都有可能用到的一些方法。比如权限检查`hasPriv()`，菜单打印`printMainMenu()`等功能。
- `common/view` 目录提供了公用的模板。比如 `header.html.php` 是模板公用的头文件；`footer.html.php`是模板公用的页脚文件；`error.html.php` 则是公用的出错信息提示的模板文件。还包含了各种jquery插件的初始化代码模板，比如`colorbox.html.php` 。
- `common/lang`设置了公用的语言项。`lang/zh-ch.php`存储公用的语言文件。

**参考资料：**

1. zentaoPHP框架：https://devel.easycorp.cn/book/zentaophphelp/about-10.html
1. https://www.zentao.net/book/zentaopmshelp/40.html

