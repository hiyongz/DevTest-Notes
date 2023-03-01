import asyncio


class Testdemo:
    storage = []  # class level field

    def __init__(self, name):
        self.name = name  # instance level field

    def do_work(self):
        """just add some digits to class level field"""
        for i in range(3):
            exec(f'self.name{i}=i')
            Testdemo.storage.append(i)
            # print(f"{self.name}: {Test.storage}")
            print(eval(f"self.name{i}"))


if __name__ == '__main__':
    t = Testdemo(2)
    t.do_work()
