# Python协程
文章[Python多线程与多进程](https://blog.csdn.net/u010698107/article/details/117265796)中介绍了并行，并发，多线程和多进程的概念。多线程 / 多进程是解决并发问题的模型之一，本文要介绍的协程也是实现并发编程的一种方式。协程使用的异步IO (asynchronous IO)不是多线程或者多进程的，它是一种单线程、单进程的设计。也就是说，协程可以实现并发调度，但它本身并不是并发的（单线程下的”并发“）。相比多线程和多进程，协程没有进程上下文切换导致的资源占用，运行效率更高。

<!--more-->


最开始服务器并发使用的是多线程 / 多进程的方式，随着互联网的快速发展，网络用户数大量增长，遇到了C10K 瓶颈，也就是同时连接到服务器的客户端数量超过 10000 个，导致服务器无法提供正常服务，解决这个问题的其中一个方案就是异步编程。NGINX 提出了**事件循环**，通过启动一个统一的调度器，让调度器来决定一个时刻去运行哪个任务，于是省去了多线程中启动线程、管理线程、同步锁等各种开销。Node.js中使用 async / await  解决**回调地狱（callback hell）**问题。

Python 2 使用生成器实现协程，Python2.5 中，使用yield 关键字使生成器有了记忆功能，Python 3.7 提供了新的基于 asyncio 和 async / await 的方法。除了Python，协程也在其它语言中得到实现，比如 golang 的 goroutine，luajit 的 coroutine，scala 的 actor 等，本文主要介绍Python中协程的使用方法。


协程(Coroutine)允许执行被挂起与被恢复，在执行任务（task）A时可以随时中断去执行任务B，通过调度器来进行任务自由切换，这一整个过程中只有一个线程在执行。协程是协作式多任务的的轻量级线程，协程之间的切换不需要涉及任何系统调用或任何阻塞调用。

在IO密集型的多线程实现中，如果I/O 操作非常频繁，多线程会进行频繁的线程切换，并且线程数不能无限增加，所以使用协程非常好的方法。python 协程可以使用asyncio 模块实现，下面先来介绍asyncio。

# Asyncio
先来区分一下 Sync（同步）和 Async（异步）的概念。
- 同步指操作一个接一个地执行，下一个操作必须等上一个操作完成后才能执行。
- 异步指不同操作间可以相互交替执行，如果其中的某个操作被 block 了，程序并不会等待，而是会找出可执行的操作继续执行。

Asyncio 是单线程的，它只有一个主线程，但是可以进行多个不同的任务（task），这里的任务，就是特殊的 future 对象。这些任务被一个叫做 event loop 的对象所控制，event loop 对象控制任务的交替执行，直到所有任务完成，可以把这里的任务类比成多线程里的多个线程。

在Python 3.7 以上版本中，可以使用asyncio库来实现协程，可参考官方文档：[https://docs.python.org/3/library/asyncio-eventloop.html](https://docs.python.org/3/library/asyncio-eventloop.html)，下面看一个协程例子：

```python
import asyncio
import time

async def worker_1():
    print('worker_1 start')
    await asyncio.sleep(2)
    print('worker_1 done')

async def worker_2():
    print('worker_2 start')
    await asyncio.sleep(1)
    print('worker_2 done')

async def main():
    task1 = asyncio.create_task(worker_1())
    task2 = asyncio.create_task(worker_2())
    tasks = [task1,task2]
    print('before await')
    await asyncio.gather(*tasks)
    # for task in tasks:
    #     await task
    #     print(task._state)
    
start = time.time()
asyncio.run(main())
end = time.time()
print('Running time: %s Seconds'%(end-start))
```


先来介绍一下代码中使用到的魔法工具：

- async 修饰词将main，worker_1，worker_2方法声明为异步函数，当调用异步函数时，会返回一个协程对象（coroutine object）：  
  
    ```python
    <coroutine object worker_1 at 0x000002A65D14EC48>
    ```

- await：同步调用，阻塞程序，执行对应的协程函数。await asyncio.sleep(5)表示程序暂停等待5s，await worker_1() 则会执行 worker_1() 函数，当前的调用执行结束后才触发下一次调用。

-  async 和 await 关键字一般组合使用，如果任务执行的过程需要等待，则将其放入等待状态的列表中，然后继续执行预备状态列表里的任务。

- asyncio.create_task()：创建任务，任务创建后就会被调度执行，进入事件循环等待运行。使用这种方式创建任务后，就不会出现阻塞。

- await asyncio.gather(*tasks, return_exception=False)：运行tasks序列的所有任务，等待所有任务都结束才结束主程序，单星号`*`解包任务列表，也可以这样写：

  ```python
  for task in tasks:
     await task
  ```

- asyncio.run：运行，运行时拿到 event loop对象，运行完成后关闭，这是Python3.7+引入的方法。以前的版本可以使用如下方式：

    ```python
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    finally:
        loop.close()
    ```

    


运行一下代码，执行结果：

```python
before await
worker_1 start
worker_2 start
worker_2 done
worker_1 done
Running time: 2.0120482444763184 Seconds
```

执行流程如下：

1. asyncio.run(main())，事件循环开启
2. asyncio.create_task()创建任务task1 和 task2 ，进入事件循环等待运行，打印“before await”。
3. await task1 执行，事件调度器开始调度 worker_1。
4. worker_1 开始运行，运行到 await asyncio.sleep(2)， 从当前任务切出，事件调度器开始调度 worker_2。
5. worker_2 开始运行，运行到 await asyncio.sleep(1) ，从当前任务切出。
6. 1s后，worker_2 的 sleep 完成，事件调度器将控制权重新传给 task_2，输出 'worker_2 done'，task_2 完成任务，从事件循环中退出。
7. 事件调度器在 await task1 处继续等待
8. 2s后，worker_1 的 sleep 完成，事件调度器将控制权重新传给 task_1，task_1 完成任务，从事件循环中退出；
9. 协程所有任务结束，事件循环结束。

到这里，想必你已经知道协程的概念和asyncio的使用方法了，下面来实现一个使用协程爬虫的程序。

# 协程爬虫

爬虫是一个比较典型的I/O密集型任务，除了使用多线程实现外，也可以用协程来实现。实际上线程能实现的，协程也都能做到。

下面使用协程来实现抓取博客[https://hiyongz.github.io/](https://hiyongz.github.io/)上的所有文章，获取博客名称、发布时间和字数。

单线程版本：

```python
import time

import requests
from bs4 import BeautifulSoup

def main():
    baseurl = "https://hiyongz.github.io"
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
    }
    # init_page = requests.get(url).content
    init_page = requests.get(url=baseurl, headers=header).content
    init_soup = BeautifulSoup(init_page, 'lxml')

    # 获取文章页数
    nav_tag = init_soup.find('nav', class_="pagination")
    page_number_tag = nav_tag.find_all('a', class_="page-number")
    page_number = int(page_number_tag[1].text)
    article_num = 0
    for num in range(page_number):
        if num >=1:
            url = baseurl + f'/page/{num+1}/'
        else:
            url = baseurl

        init_page = requests.get(url=url, headers=header).content
        init_soup = BeautifulSoup(init_page, 'lxml')
        all_articles = init_soup.find('div', class_="content index posts-expand")
        for each_article in all_articles.find_all('header', class_="post-header"):
            all_a_tag = each_article.find_all('a')

            article_name = all_a_tag[0].text
            article_url = all_a_tag[0].attrs['href']

            response_item = requests.get(url=baseurl+article_url, headers=header).content
            soup_item = BeautifulSoup(response_item, 'lxml')
            time_tag = soup_item.find('time')
            publish_time = time_tag.text
            word_tag = each_article.find_all(title="本文字数")
            word_count = word_tag[0].text
            word_count = word_count.strip().split('\n')[1]
            article_num = article_num + 1
            print(f'{article_name} {baseurl+article_url} {publish_time} {word_count}')

    print(f'一共有{article_num}篇博客文章')

start = time.time()
main()
end = time.time()
print('Running time: %s Seconds'%(end-start))
```

执行结果（部分）：

```python
markdown基本语法介绍 https://hiyongz.github.io/posts/markdown-basic-syntax/ 2021-06-12 6.8k
Python中的闭包 https://hiyongz.github.io/posts/python-notes-for-function-closures/ 2021-06-10 2.4k
算法笔记：位运算 https://hiyongz.github.io/posts/algorithm-notes-for-bitwise-operation/ 2021-06-08 2.8k
常见搜索算法（二）：二分查找 https://hiyongz.github.io/posts/algorithm-notes-for-binary-search/ 2021-06-03 1.1k
.............
一共有124篇博客文章
Running time: 107.27503871917725 Seconds
```

使用协程（由于requests 库不兼容 asyncio， 下面使用aiohttp 库进行接口请求）：

```python
import time

import requests
from bs4 import BeautifulSoup
import asyncio
import aiohttp


async def fetch_content(url, header):
    async with aiohttp.ClientSession(
            headers=header, connector=aiohttp.TCPConnector(ssl=False)
    ) as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    baseurl = "https://hiyongz.github.io"
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
    }
    article_names, article_urls,publishs_time,words_count = [], [], [], []
    init_page = requests.get(url=baseurl, headers=header).content
    init_soup = BeautifulSoup(init_page, 'lxml')
    # 获取文章页数
    nav_tag = init_soup.find('nav', class_="pagination")
    page_number_tag = nav_tag.find_all('a', class_="page-number")
    page_number = int(page_number_tag[1].text)
    for num in range(page_number):
        if num >= 1:
            url = baseurl + f'/page/{num+1}/'
        else:
            url = baseurl
        # article_names, article_urls, publishs_time, words_count = [], [], [], []
        init_page = requests.get(url=url, headers=header).content
        init_soup = BeautifulSoup(init_page, 'lxml')
        all_articles = init_soup.find('div', class_="content index posts-expand")

        for each_article in all_articles.find_all('header', class_="post-header"):
            all_a_tag = each_article.find_all('a')
            article_name = all_a_tag[0].text
            article_url = all_a_tag[0].attrs['href']

            article_names.append(article_name)
            article_urls.append(baseurl+article_url)

    tasks = [fetch_content(url, header) for url in article_urls]
    article_num = len(article_urls)
    pages = await asyncio.gather(*tasks)

    for article_name, article_url, page in zip(article_names, article_urls, pages):
        soup_item = BeautifulSoup(page, 'lxml')
        time_tag = soup_item.find('time')
        publish_time = time_tag.text
        word_tag = soup_item.find_all(title="本文字数")
        word_count = word_tag[0].text
        word_count = word_count.strip().split('\n')[1]
        print('{} {} {} {}'.format(article_name, article_url,publish_time,word_count))
    print(f'一共有{article_num}篇博客文章')

start=time.time()
asyncio.run(main())
end=time.time()
print('Running time: %s Seconds'%(end-start))
```

执行结果（部分）：

```python
一共有124篇博客文章
Running time: 14.071799755096436 Seconds
```

可以看到速度提升了很多。

# 多线程、多进程和协程如何选择

在[Python多线程与多进程](https://blog.csdn.net/u010698107/article/details/117265796)中介绍了多线程和多进程，它们都有各自的应用场景，在实际应用中，如何选择呢？

-  I/O 密集型任务，并且 I/O 操作很慢，需要很多任务协同实现，使用协程。
-  I/O 密集型任务，但是 I/O 操作很快，只需要有限数量的任务/线程，使用多线程就可以，当然也可以使用协程。
-  CPU 密集型任务，使用多进程。

# 总结

本文主要介绍了协程的概念以及python中协程的实现方法，注意asyncio 是单线程的，通过内部 event loop 机制实现并发地运行多个不同的任务，从而实现并发的效果。还要注意的就是asyncio比多线程有更大的自主控制权，你需要知道程序在什么时候需要暂停、等待 I/O，在使用协程时要注意。

在I/O 操作多且慢的情况下使用协程比多线程效率更高，因为 Asyncio 内部任务切换远比线程切换的资源损耗要小；并且 Asyncio 可以开启的任务数量也比多线程多。





