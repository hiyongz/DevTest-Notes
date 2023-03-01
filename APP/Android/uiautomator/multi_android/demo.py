import asyncio


class Test:
    storage = []  # class level field

    def __init__(self, name):
        self.name = name  # instance level field

    async def do_work(self):
        """just add some digits to class level field"""
        for i in range(3):
            Test.storage.append(i)
            print(f"{self.name}: {Test.storage}")
            await asyncio.sleep(1)


class TestWrapper:
    def __init__(self, n):
        self.n = n

    async def run(self):
        # await asyncio.gather(*(Test(f"Cor-{i}").do_work() for i in range(self.n)))
        await asyncio.gather(*(Test(f"Cor-{i}").do_work() for i in range(self.n)))


if __name__ == '__main__':
    asyncio.run(TestWrapper(3).run())