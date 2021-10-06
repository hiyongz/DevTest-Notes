# pytest 的setup/teardown方法
PyTest支持xUnit style 结构， setup() 和 teardown() 方法用于初始化和清理测试环境，可以保证测试用例的独立性。pytest的setup/teardown方法包括：模块级别(setup_module/teardown_module)、函数级别(setup_function/teardown_function)、类级别(setup_class/ teardown_class)、方法级别(setup_method/teardown_methond或者setup/teardown)。

<!--more-->

## 模块级别

模块中的第一个测试用例开始前执行setup_module方法，模块中的最后一个测试用例结束后运行teardown_module方法。

```python
import pytest

def setup_module():
    print("初始化。。。")

def teardown_module():
    print("清理。。。")

class Test_Demo():
    def test_case1(self):
        print("开始执行测试用例1")
        assert 1 + 1 == 2

    def test_case2(self):
        print("开始执行测试用例2")
        assert 2 + 8 == 10

    def test_case3(self):
        print("开始执行测试用例3")
        assert 99 + 1 == 100
```

结果：

```python
模块初始化。。。
PASSED                     [ 33%]开始执行测试用例1
PASSED                     [ 66%]开始执行测试用例2
PASSED                     [100%]开始执行测试用例3
模块清理。。。
```

## 函数级别

 setup_function/teardown_function在每个测试函数前后运行，只对函数用例生效，不在类中。

```python
import pytest

def setup_function():
    print("初始化。。。")

def teardown_function():
    print("清理。。。")

def test_case1():
    print("开始执行测试用例1")
    assert 1 + 1 == 2

def test_case2():
    print("开始执行测试用例2")
    assert 2 + 8 == 10

def test_case3():
    print("开始执行测试用例3")
    assert 99 + 1 == 100
```



结果：

```python
test_setup_teardown2.py::test_case1 初始化。。。
PASSED                               [ 33%]开始执行测试用例1
清理。。。

test_setup_teardown2.py::test_case2 初始化。。。
PASSED                               [ 66%]开始执行测试用例2
清理。。。

test_setup_teardown2.py::test_case3 初始化。。。
PASSED                               [100%]开始执行测试用例3
清理。。。

```

## 类级别


类级别函数 setup_class/teardown_class 对类有效，位于类中，在测试类中前后调用一次。

```python
class Test_Demo():
    def setup_class(self):
        print("初始化。。。")

    def teardown_class(self):
        print("清理。。。")

    def test_case1(self):
        print("开始执行测试用例1")
        assert 1 + 1 == 2

    def test_case2(self):
        print("开始执行测试用例2")
        assert 2 + 8 == 10

    def test_case3(self):
        print("开始执行测试用例3")
        assert 99 + 1 == 100
```

结果：

```python
初始化。。。
PASSED                    [ 33%]开始执行测试用例1
PASSED                    [ 66%]开始执行测试用例2
PASSED                    [100%]开始执行测试用例3
清理。。。
```

## 方法级别

方法级别函数 setup_method/teardown_method和setup/teardown对类有效，也位于类中，这两个效果一样，在测试类中每个测试方法前后调用一次。

```python
class Test_Demo():
    def setup_method(self):
        print("初始化。。。")

    def teardown_method(self):
        print("清理。。。")

    def test_case1(self):
        print("开始执行测试用例1")
        assert 1 + 1 == 2

    def test_case2(self):
        print("开始执行测试用例2")
        assert 2 + 8 == 10

    def test_case3(self):
        print("开始执行测试用例3")
        assert 99 + 1 == 100
```

结果：

```python
初始化。。。
PASSED                    [ 33%]开始执行测试用例1
清理。。。
初始化。。。
PASSED                    [ 66%]开始执行测试用例2
清理。。。
初始化。。。
PASSED                    [100%]开始执行测试用例3
清理。。。
```

























