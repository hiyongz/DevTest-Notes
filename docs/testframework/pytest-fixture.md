# pytest fixture 用法
xUnit style 结构的 fixture用于初始化测试函数， pytest fixture是对传统的 xUnit 架构的setup/teardown功能的改进。pytest fixture为测试准备一个良好的测试环境，测试函数使用的每个 fixture通常有一个参数(以 fixture 命名)，测试函数通过参数访问它们。本文将介绍pytest fixture的一些基本用法。

<!--more-->

## @pytest.fixture

```python
import pytest

@pytest.fixture()
def login():
    print("登录")
    return 8

class Test_Demo():
    def test_case1(self):
        print("\n开始执行测试用例1")
        assert 1 + 1 == 2

    def test_case2(self, login):
        print("\n开始执行测试用例2")
        print(login)
        assert 2 + login == 10

    def test_case3(self):
        print("\n开始执行测试用例3")
        assert 99 + 1 == 100

if __name__ == '__main__':
    pytest.main()
```

test_case2需要调用login方法（或者获取login的返回值），pytest 将会寻找并调用`@pytest.fixture`标记的login() 方法。

结果：

```python
PASSED                           [ 33%]
开始执行测试用例1
登录
PASSED                           [ 66%]
开始执行测试用例2
8
PASSED                           [100%]
开始执行测试用例3
```



## 共享 fixture 函数：conftest.py

在测试过程中，多个测试文件可能都要调用 fixture 函数，可以将其移动到 conftest.py 文件中。conftest.py 文件中的 fixture 函数不需要在测试函数中导入，可以被 pytest 自动识别，查找顺序从测试类开始，然后是测试模块，然后是 conftest.py 文件，最后是内置插件和第三方插件。

conftest.py ：

```python
import pytest
@pytest.fixture()
def login():
    print("登录")
    return 8
```

测试用例：

```python
import pytest

class Test_Demo():
    def test_case1(self):
        print("\n开始执行测试用例1")
        assert 1 + 1 == 2

    def test_case2(self, login):
        print("\n开始执行测试用例2")
        print(login)
        assert 2 + login == 10

    def test_case3(self):
        print("\n开始执行测试用例3")
        assert 99 + 1 == 100


if __name__ == '__main__':
    pytest.main()
```

结果：

```python
PASSED                           [ 33%]
开始执行测试用例1
登录
PASSED                           [ 66%]
开始执行测试用例2
8
PASSED                           [100%]
开始执行测试用例3
```

## yield方法

使用yield关键字可以实现setup/teardown的功能，在yield关键字之前的代码在case之前执行，yield之后的代码在case运行结束后执行

```python
import pytest

@pytest.fixture()
def login():
    print("登录")
    yield
    print("退出登录")

class Test_Demo():
    def test_case1(self):
        print("\n开始执行测试用例1")
        assert 1 + 1 == 2

    def test_case2(self, login):
        print("\n开始执行测试用例2")
        assert 2 + 8 == 10

    def test_case3(self):
        print("\n开始执行测试用例3")
        assert 99 + 1 == 100


if __name__ == '__main__':
    pytest.main()
```

结果：

```python
PASSED                      [ 33%]
开始执行测试用例1
登录
PASSED                      [ 66%]
开始执行测试用例2
退出登录
PASSED                      [100%]
开始执行测试用例3

```

## addfinalizer方法


addfinalizer也可以实现环境的清理，实现与yield方法相同的效果，跟yield不同的是需要注册作为终结器使用的函数。

```python
import pytest

@pytest.fixture()
def login(request):
    print("登录")
    def demo_finalizer():
        print("退出登录")
    # 注册demo_finalizer为终结函数
    request.addfinalizer(demo_finalizer)

class Test_Demo():
    def test_case1(self):
        print("\n开始执行测试用例1")
        assert 1 + 1 == 2

    def test_case2(self, login):
        print("\n开始执行测试用例2")
        assert 2 + 8 == 10

    def test_case3(self):
        print("\n开始执行测试用例3")
        assert 99 + 1 == 100


if __name__ == '__main__':
    pytest.main()
```

结果：

```python
PASSED               [ 33%]
开始执行测试用例1
登录
PASSED               [ 66%]
开始执行测试用例2
退出登录
PASSED               [100%]
开始执行测试用例3
```



## fixture 作用范围：Scope

fixture 作用范围可以为module、class、session和function，默认作用域为function。

- **function**：每一个函数或方法都会调用
- **class**：每一个类调用一次
- **module**：每一个.py文件调用一次
- **session**：是多个文件调用一次
### scope="function"
```python
import pytest

@pytest.fixture(scope="function")
def login():
    print("登录...")

class Test_Demo():
    def test_case1(self, login):
        print("\n开始执行测试用例1")
        assert 1 + 1 == 2

    def test_case2(self, login):
        print("\n开始执行测试用例2")
        assert 2 + 8 == 10

    def test_case3(self, login):
        print("\n开始执行测试用例3")
        assert 99 + 1 == 100


if __name__ == '__main__':
    pytest.main()
```

结果：

```python
登录...
PASSED                      [ 33%]
开始执行测试用例1
登录...
PASSED                      [ 66%]
开始执行测试用例2
登录...
PASSED                      [100%]
开始执行测试用例3
```
### scope="class"

一个class里面多个用例都调用了此fixture，那么只在class里所有用例开始前执行一次

```python
import pytest

@pytest.fixture(scope="class")
def login():
    print("登录...")

```

结果：

```python
登录...
PASSED                      [ 33%]
开始执行测试用例1
PASSED                      [ 66%]
开始执行测试用例2
PASSED                      [100%]
开始执行测试用例3
```



## fixture自动应用

### autouse参数

autouse设置为True时，自动调用fixture功能。由于默认作用域为function，不指定scope则每个方法都会调用fixture方法。

```python
import pytest

@pytest.fixture(autouse=True)
def login():
    print("登录...")

class Test_Demo():
    def test_case1(self):
        print("\n开始执行测试用例1")
        assert 1 + 1 == 2

    def test_case2(self):
        print("\n开始执行测试用例2")
        assert 2 + 8 == 10

    def test_case3(self):
        print("\n开始执行测试用例3")
        assert 99 + 1 == 100


if __name__ == '__main__':
    pytest.main()
```

结果：

```python
登录...
PASSED                    [ 33%]
开始执行测试用例1
登录...
PASSED                    [ 66%]
开始执行测试用例2
登录...
PASSED                    [100%]
开始执行测试用例3
```

### @pytest.mark.usefixtures()

在测试方法上加@pytest.mark.usefixtures()

```python
import pytest

@pytest.fixture()
def login():
    print("登录...")

@pytest.mark.usefixtures("login")
class Test_Demo():
    def test_case1(self):
        print("\n开始执行测试用例1")
        assert 1 + 1 == 2

    def test_case2(self):
        print("\n开始执行测试用例2")
        assert 2 + 8 == 10

    def test_case3(self):
        print("\n开始执行测试用例3")
        assert 99 + 1 == 100


if __name__ == '__main__':
    pytest.main()
```

结果：

```python
登录...
PASSED                [ 33%]
开始执行测试用例1
登录...
PASSED                [ 66%]
开始执行测试用例2
登录...
PASSED                [100%]
开始执行测试用例3
```

## fixture函数参数化

如果多条用例都需要调用相同参数，可以将fixture函数参数化。fixture 函数将执行每个参数值，fixture通过固定参数request传递。

```python
import pytest

@pytest.fixture(scope="module", params=[
    [1, 1, 2],
    [2, 8, 10],
    [99, 1, 100]
])
def data(request):
    yield request.param

class Test_Demo():
    def test_case1(self):
        print("\n开始执行测试用例1")
        assert 2 + 8 == 10

    def test_case2(self, data):
        print("\n开始执行测试用例2")
        assert data[0] + data[1] == data[2]

    def test_case3(self):
        print("\n开始执行测试用例3")
        assert 99 + 1 == 100


if __name__ == '__main__':
    pytest.main()
```

结果：

```python
PASSED                     [ 20%]
开始执行测试用例1
PASSED              [ 40%]
开始执行测试用例2
PASSED              [ 60%]
开始执行测试用例2
PASSED              [ 80%]
开始执行测试用例2
PASSED                     [100%]
开始执行测试用例3
```











