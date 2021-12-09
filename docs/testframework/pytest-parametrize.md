# pytest 参数化用例
在 [pytest fixture 用法](https://hiyong.gitee.io/posts/pytest-fixture/) 中介绍了pytest.fixture()可以参数化fixture函数，@pytest.mark.parametrize 可以为测试方法或者测试类定义多组变量。本文将分享使用@pytest.mark.parametrize 实现参数化用例。

<!--more-->

## 使用方法

@pytest.mark.parametrize(argnames, argvalues)

* **argnames**：参数化变量名，可以是string(逗号分割) 、list 和 tuple类型
  * @pytest.mark.parametrize("a, b", [(1,2),(3,4)])
  * @pytest.mark.parametrize(["a","b"], [(1,2),(3, 4)])
  * @pytest.mark.parametrize(("a", "b"), [(1,2),(3,4)])

* **argvalues**：参数化的值

## 参数化实例1

```python
import pytest

class Test_Demo():
    @pytest.mark.parametrize("a, b, result", [(1, 1, 2), (2, 8, 10)])
    def test_case1(self, a, b, result):
        print("\n开始执行测试用例1")
        assert a + b == result
```

结果：

```python
PASSED                 [ 50%]
开始执行测试用例1
PASSED                [100%]
开始执行测试用例1
```

## 参数化实例2

```python
import pytest
data = [(1, 1, 2),
         (2, 8, 10),
         (99, 1, 100)
         ]

class Test_Demo():
    @pytest.mark.parametrize("a, b, result", data)
    def test_case1(self, a, b, result):
        print("\n开始执行测试用例1")
        assert a + b == result


if __name__ == '__main__':
    pytest.main()
```

结果：

```python
PASSED                [ 33%]
开始执行测试用例1
PASSED               [ 66%]
开始执行测试用例1
PASSED             [100%]
开始执行测试用例1
```

## 参数化实例3

data.yaml文件内容：

```yaml
-
  - 1
  - 1
  - 2
-
  - 2
  - 8
  - 10
-
  - 99
  - 1
  - 100
```



```python
import pytest
import yaml

class Test_Demo():
    @pytest.mark.parametrize(["a","b","result"],yaml.safe_load(open("./data.yaml")))
    def test_case1(self, a, b, result):
        print("\n开始执行测试用例1")
        assert a + b == result
        
```



结果：

```python
PASSED                [ 33%]
开始执行测试用例1
PASSED               [ 66%]
开始执行测试用例1
PASSED             [100%]
开始执行测试用例1
```

## 数据驱动

数据驱动参数化的应用，数据量小的测试用例可以使用代码的参数化来实现数据驱动，数据量大的情况下可以使用一种结构化的文件(例如csv、yaml、xml、db、 excel、json等)来存储数据，然后在测试用例中读取这些数据。









