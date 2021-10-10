#!/usr/bin/python3
#-*-coding:utf-8-*-
# @Time:    2020/5/25 20:37
# @Author:  haiyong
# @File:    test_tag.py
import json

import pytest
import yaml
from jsonpath import jsonpath

from test_requests.api.tag import Tag


class TestTag:
    tag = Tag()
    test_data = tag.yaml_load('test_tag.data.yaml')

    @classmethod
    def setup_class(cls):
        pass
        # cls.tag = Tag()
    def setup(self):
        pass

    @pytest.mark.parametrize("name_old,name_new",test_data)
    def test_all(self,name_old,name_new):
        data = self.tag.get()
        for name in [name_old,name_new]:
            # tag_id = jsonpath(self.tag.get(), '$..tag[?(@.name=="wangwu")].id')
            tag_id = self.tag.json_path(data, f'$..tag[?(@.name=="{name}")].id')
            if tag_id:
                self.tag.delete(tag_id[0])
        # self.tag.add("wangwu")
        assert self.tag.add(name_old)["errcode"] == 0
        # tag_id = jsonpath(self.tag.get(), '$..tag[?(@.name=="wangwu")].id')[0]
        tag_id = self.tag.json_path(self.tag.get(), f'$..tag[?(@.name=="{name_old}")].id')[0]
        assert self.tag.update(tag_id, name_new)["errcode"] == 0

    def test_get(self):
        print(json.dumps(Tag().get(),indent=2))
        assert self.tag.get()['errcode'] == 0
    def test_add(self):
        assert self.tag.add(tag_name = "add demo")['errcode'] == 0

    def test_delete(self):
        print(Tag().delete('etQKd-CgAAI70aMYm4j37aJyTo0EMRmw'))

    def test_update(self):
        print(Tag().update('etQKd-CgAAE6Zdmx89xoc_LYuIyLWwNw', 'wangwu'))








