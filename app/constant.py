#!/usr/bin/python3
# -*-coding:utf-8-*-

# **********************************************************
# * Author        : SnailCL
# * Create time   : 2020-05-21 13:48:21
# * Last modified : 2020-05-21 13:48:21
# * Filename      : constant.py
# * Description   :
# **********************************************************

import json


with open('./config.json', 'r', encoding='utf-8') as f:
    CONFIG_DICT = json.load(f)
