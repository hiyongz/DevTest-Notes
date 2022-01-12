# Robot Framework robot命令


在进行持续测试中，如果使用Robot Framework执行自动化用例，可以使用robot命令来执行用例，本文简单介绍robot命令的部分选项参数的用法。

<!--more-->

## robot命令选项

可以执行 `robot -h` 命令查看robot选项参数。或者访问 [https://robot-framework.readthedocs.io/en/2.8/_modules/robot/run.html](https://robot-framework.readthedocs.io/en/2.8/_modules/robot/run.html)

robot命令语法格式

```bash
robot [options] paths
python -m robot [options] paths
python path/to/robot [options] paths
java -jar robotframework.jar [options] paths
```

robot部分选项参数：

- `-t --test name *`：通过用例名选择测试用例
- `-s --suite name *`：通过套件名选择测试用例，通过 `*` 匹配任意用例，`?` 匹配任意字符
- `-i --include tag *`：通过标签名选择测试用例，支持3种方式：①单个标签，比如`tag*`、`tag1`；②`AND`或者`&`连接多个标签，例如`tag1&tag2`；③`NOT`连接多个标签，例如`tag*NOTtag1`，表示所有标签以`tag`开头的用例，但不包括`tag1`。
- `-e --exclude tag *`：不运行的标签用例。比`include`参数优先级高。
- `-d --outputdir dir`：设置测试输出路径
- `-l --log file`：指定HTML log文件名，默认为log.html
- `-r --report file`：指定HTML report文件名，默认为report.html
- `-T --timestampoutputs`：时间戳形式的日志文件名
- `-A --argumentfile path *`：从文件中读取参数

## robot使用实例

RF测试用例如下图：

![](test-framework-for-robotframework-pybot-options/rf-testcases-demo.png)




下面以这些测试用例为例，介绍如何使用robot命令执行指定用例。

### 执行整个项目

语法格式：

```bash
robot 项目路径
```

举例：
```bash
$ cd D:\ProgramWorkspace\DevTest-Notes\RobotFramework
$ robot -d D:/rf_results PO_demo/01_测试用例
```

### 执行某个测试套件
语法格式：

```bash
pybot 测试套件路径
```
举例：
```bash
$ robot -d D:/rf_results PO_demo/01_测试用例/登录测试-错误用户名+密码.robot
==============================================================================
登录测试-错误用户名+密码
==============================================================================
case_1.1_错误用户名+密码                                              | PASS |
------------------------------------------------------------------------------
case_1.2_错误用户名+正确密码                                          | PASS |
------------------------------------------------------------------------------
case_1.3_正确用户名+错误密码                                          | PASS |
------------------------------------------------------------------------------
登录测试-错误用户名+密码                                              | PASS |
3 critical tests, 3 passed, 0 failed
3 tests total, 3 passed, 0 failed
==============================================================================
Output:  D:\rf_results\output.xml
Log:     D:\rf_results\log.html
Report:  D:\rf_results\report.html
```



### 执行某个标签用例
语法格式：

```bash
pybot --include 标签名 项目路径
```

举例：

```bash
$ robot -d D:/rf_results --include login PO_demo/01_测试用例
部分日志...
==============================================================================
01 测试用例                                                           | PASS |
4 critical tests, 4 passed, 0 failed
4 tests total, 4 passed, 0 failed
==============================================================================
Output:  D:\rf_results\output.xml
Log:     D:\rf_results\log.html
Report:  D:\rf_results\report.html

```

### 执行某个用例
语法格式：

```bash
pybot --suite 测试套件路径 --test 测试用例名称 项目路径
```

举例：

```bash
$ robot -d D:/rf_results --suite 01_测试用例.登录测试-错误用 户名+密码 --test case_*.2* PO_demo
==============================================================================
PO demo
==============================================================================
PO demo.01 测试用例
==============================================================================
PO demo.01 测试用例.登录测试-错误用户名+密码
==============================================================================
case_1.2_错误用户名+正确密码                                          | PASS |
------------------------------------------------------------------------------
PO demo.01 测试用例.登录测试-错误用户名+密码                          | PASS |
1 critical test, 1 passed, 0 failed
1 test total, 1 passed, 0 failed
==============================================================================
PO demo.01 测试用例                                                   | PASS |
1 critical test, 1 passed, 0 failed
1 test total, 1 passed, 0 failed
==============================================================================
PO demo                                                               | PASS |
1 critical test, 1 passed, 0 failed
1 test total, 1 passed, 0 failed
==============================================================================
Output:  D:\rf_results\output.xml
Log:     D:\rf_results\log.html
Report:  D:\rf_results\report.html
```

### 参数文件
如果参数很多，可以将他们放在一个文件中，使用 `-A | --argumentfile` 参数来指定。

语法格式：
```bash
pybot --argumentfile 参数文件路径 项目路径
```

举例：
编写一个参数文件argfile.txt，内容如下：
```text
-T
--suite 
01_测试用例.登录测试-错误用户名+密码 
--test 
case_*.2*
```
执行：
```bash
$ robot -d D:/rf_results --argumentfile D:\rf_results\argfile.txt PO_demo
==============================================================================
PO demo
==============================================================================
PO demo.01 测试用例
==============================================================================
PO demo.01 测试用例.登录测试-错误用户名+密码
==============================================================================
case_1.2_错误用户名+正确密码                                          | PASS |
------------------------------------------------------------------------------
PO demo.01 测试用例.登录测试-错误用户名+密码                          | PASS |
1 critical test, 1 passed, 0 failed
1 test total, 1 passed, 0 failed
==============================================================================
PO demo.01 测试用例                                                   | PASS |
1 critical test, 1 passed, 0 failed
1 test total, 1 passed, 0 failed
==============================================================================
PO demo                                                               | PASS |
1 critical test, 1 passed, 0 failed
1 test total, 1 passed, 0 failed
==============================================================================
Output:  D:\rf_results\output-20220102-163828.xml
Log:     D:\rf_results\log-20220102-163828.html
Report:  D:\rf_results\report-20220102-163828.html
```


