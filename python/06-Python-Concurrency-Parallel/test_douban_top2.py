#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2021/6/13 7:55
# @Author:  hiyongz
# @File:    test_douban_top2.py

# https://movie.douban.com/top250

import requests
from bs4 import BeautifulSoup

def main():
    baseurl = "https://movie.douban.com/top250"
    header = {
'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36'
}
    article_num = 0
    for i in range(0, 10):
        url = baseurl + "?start=" + str(i * 25)
        init_page = requests.get(url=url,headers=header).content
        init_soup = BeautifulSoup(init_page, 'lxml')

        all_movies = init_soup.find('ol', class_="grid_view")
        for each_movie in all_movies.find_all('div', class_="item"):
            all_a_tag = each_movie.find_all('a')
            img_tag = each_movie.find_all('img')

            movie_name = img_tag[0]['alt']
            movie_img = img_tag[0]['src']
            url_to_fetch = all_a_tag[1]['href']


            movie_message = requests.get(url=url_to_fetch,headers=header).content
            movie_soup = BeautifulSoup(movie_message, 'lxml')
            release_tag = movie_soup.find_all('span',property="v:initialReleaseDate")
            release_date = [d.text for d in release_tag]
            release_date = '/'.join(release_date)


            print(f'{movie_name} {release_date} {movie_img}')

main()