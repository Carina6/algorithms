#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-26 23:37
# @Author  : hlliu


# 找出字符数组中只出现三次，且最早出现完三次的字符
def test_first_3_times():

    def method1(str):
        if str is None or len(str) < 3:
            return None

        map = dict()
        for s in str:
            map[s] = map.get(s) + 1 if map.get(s) is not None else 1

        arr=[]
        for key,value in map.items():
            if value==3:
                arr.append(key)
        if len(arr) == 0:
            return None

        for s in str[::-1]:
            if len(arr) == 1:
                return arr[0]
            if s in arr:
                arr.remove(s)

    print(method1('aabcbba'))
