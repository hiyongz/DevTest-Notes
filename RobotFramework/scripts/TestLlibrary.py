# -*-coding:utf-8-*-

class TestLlibrary():
    def __init__(self):
        pass

    def test_sub(self, a, b, results=None):
        """两数相减
        """
        if float(a) - float(b) == float(results):
            return True
        else:
            raise RuntimeError("%s - %s != %s"%(a,b,results))

    def test_add(self, a, b, c):
        """两数相加

        :a: value1

        :b: value2

        :c: 预期结果

        Example:
        | Test Add | 2 | 3 | 5 |

        """
        if float(a) + float(b) == float(c):
            return True
        else:
            raise RuntimeError("%s + %s != %s"%(a,b,c))


