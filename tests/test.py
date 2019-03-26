#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/23 下午11:41
# @Author  : hlliu


def test():
    s= 'ababcdef'
    t = set()
    for i in s:
        t.add(s)

    n=len(s)
    m=len(t)

    l = 0
    for i in range(n-m):
        j = i+m
        tmp = 0
        while j <=n:
            if ss in s[i:j]:
                tmp= j-i
                break
            else:
                j+=1
        if tmp<l:
            l = tmp

    print(l)


def test2():
    map = dict()
    print(map.get("a"))
