#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/6/13 7:55
# @Author:  hiyongz
# @File:    test_douban_top2_coroutine.py

# https://movie.douban.com/top250
import functools
import json
import time
from typing import List, Dict

import requests
from bs4 import BeautifulSoup
import asyncio
import aiohttp

def count_time(func):
    # 统计函数执行时间
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()    # 1
        value = func(*args, **kwargs)
        end_time = time.perf_counter()      # 2
        run_time = end_time - start_time    # 3
        print(f"{func.__name__} 执行时间为：{run_time:.4f} 秒")
        return value
    return wrapper_timer

async def fetch_content(url, header):
    # with open("douban_cookies.txt",'r') as f:
    #     # cookies = json.load(f)
    #     cookies = json.load(f)
    async with aiohttp.ClientSession(
            headers=header, connector=aiohttp.TCPConnector(ssl=False)
    ) as session:

        async with session.get(url) as response:
            r = await response.text()
            return r
@count_time
async def main():
    baseurl = "https://hiyongz.github.io/"
    header = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
    }

    movie_names, urls_to_fetch, release_dates, movie_imgs = [], [], [], []
    for i in range(0, 10):
        url = baseurl + "?start=" + str(i * 25)
        init_page = await fetch_content(url, header)
        init_soup = BeautifulSoup(init_page, 'lxml')

        all_movies = init_soup.find('ol', class_="grid_view")
        for each_movie in all_movies.find_all('div', class_="item"):
            all_a_tag = each_movie.find_all('a')
            img_tag = each_movie.find_all('img')

            movie_name = img_tag[0]['alt']
            movie_img = img_tag[0]['src']
            url_to_fetch = all_a_tag[1]['href']
            movie_names.append(movie_name)

            movie_imgs.append(movie_img)
            urls_to_fetch.append(url_to_fetch)

    tasks = [fetch_content(url, header) for url in urls_to_fetch]
    pages = await asyncio.gather(*tasks)
    for movie_name, movie_img, page in zip(movie_names, movie_imgs, pages):
        movie_soup = BeautifulSoup(page, 'lxml')
        release_tag = movie_soup.find_all('span', property="v:initialReleaseDate")
        release_date = [d.text for d in release_tag]
        release_date = '/'.join(release_date)

        print(f'{movie_name} {release_date} {movie_img}')


asyncio.run(main())
