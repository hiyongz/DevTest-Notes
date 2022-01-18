#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2022/01/28 10:26
# @Author:  hiyongz
# @File:    app.py

from flask import Flask, escape, request

app = Flask(__name__)


@app.route('/')
def index():
    return "<h1>Index Page</h1>"


@app.route('/hello', methods=['get'])
def hello():
    name = request.args.get("name", "World")
    return f'<h1>Hello, {escape(name)}!</h1>' \
           f'<p>Method: {request.method}</p>' \
           f'<p>Url: {request.path}</p>'


if __name__ == '__main__':
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=1234,
    )

    app.run(**config)
