#!/usr/bin/python3
# -*-coding:utf-8-*-
# @Time:    2021/6/17 15:31
# @Author:  haiyong
# @File:    test_click.py

import click

@click.command()
@click.option('--field', '-f', type=str, help='字段', multiple=True)
@click.option('--display-filter', '-Y', prompt='display-filter', help='条件')
# @click.option('--display-filter', '-Y', prompt='display-filter', type=(str, int, float, bool), help='条件')
@click.option('--count', '-c', default=2, prompt='count', help='计数', count=True)
# @click.help_option('--help', '-h', help='帮助信息')
# @click.option('--password', '-p', prompt=True, hide_input=True, confirmation_prompt=True)
@click.password_option('--password', '-p', prompt=True, hide_input=True, confirmation_prompt=True)
def cli(field, display_filter,count,password):
    """Simple program that greets NAME for a total of COUNT times."""
    # click.echo(f'{field} {display_filter} {count}')
    click.echo(f'the password is {password}')

if __name__ == '__main__':
    cli()








