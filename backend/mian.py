#!/usr/bin/env python
# -*- coding: utf-8 -*-

# @Time    : 2024/2/5 11:00                              
# @Author  :  zhengzongwei<zhengzongwei@foxmail.com>

from app import create_app

app = create_app('development')
if __name__ == '__main__':
    app.run()
