#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/6/13 7:55
# @Author:  hiyongz
# @File:    test_douban_top2_coroutine.py

# https://movie.douban.com/top250
# https://movie.douban.com/top250
import csv
import functools
import time

import requests
import yaml
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
    articles = {}
    articles_num = {}

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
        group_tag = soup_item.find('span', class_="post-time")
        group_tag2 = group_tag.find_all('span', itemprop="name")
        article_categories = [c.text for c in group_tag2]  # 文章分类

        publish_time = time_tag.text
        word_tag = soup_item.find_all(title="本文字数")
        word_count = word_tag[0].text
        word_count = word_count.strip().split('\n')[1]
        print('{} {} {} {}'.format(article_name, article_url,publish_time,word_count))

        for cate in article_categories:
            articles_num.setdefault(cate, 0)
            articles_num[cate] = articles_num[cate] + 1

            article_link = '[' + article_name + ']' + '(' + article_url + ')'

            # articles.setdefault(cate, {})
            # articles[cate].setdefault(articles_num[cate], article_link)
            articles.setdefault(cate, [])
            articles[cate].append(article_link)

    with open("articles.yaml", "w", encoding="utf-8") as f:
        yaml.dump(articles, f, default_flow_style=False, allow_unicode=True)


    print(f'一共有{article_num}篇博客文章')


start=time.time()
asyncio.run(main())
end=time.time()
print('Running time: %s Seconds'%(end-start))

