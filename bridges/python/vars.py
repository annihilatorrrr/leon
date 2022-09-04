#!/usr/bin/env python
# -*- coding:utf-8 -*-

from os import path
from json import loads

with open(f'{path.dirname(path.realpath(__file__))}/../../package.json', 'r', encoding = 'utf8') as packagejsonfile:
    packagejson = loads(packagejsonfile.read())
useragent = 'Leon-Personal-Assistant/' + packagejson['version']
