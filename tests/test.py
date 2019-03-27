#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/23 下午11:41
# @Author  : hlliu
from models.generator import tree_node_generator


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


def test3():
    arr = [1,2,3,4,5,6]
    for i in arr[1::2]:
        print(i)


def test4():
    arr = [1,2,3,4,5,6]
    node = tree_node_generator(arr)
    print(node)
