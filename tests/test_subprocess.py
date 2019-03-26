#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-21 22:25
# @Author  : hlliu

import subprocess


def test_subprocess():
    process = subprocess.Popen("ping www.baidu.com -c 5", shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    out, error = process.communicate()
    print(out)
    print(error)

    # subprocess.call()
    # res = process.wait()
    # print(type(res))
