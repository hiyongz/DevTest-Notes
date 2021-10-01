# -*- coding: utf-8 -*-
import ConfigParser
import os,sys


def ParserCfg(filename):
    kargs = {}
    cf = ConfigParser.ConfigParser()
    cf.read(filename.replace("\\", "/"))
    for opt in cf.sections():
        if opt:
            kargs[opt] = {}
    for opt in kargs.keys():
        for k, v in cf.items(opt):
            kargs[opt][k] = v
    return kargs