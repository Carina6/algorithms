#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-28 21:41
# @Author  : hlliu
from random import choice


# 左移m位
def move(arr, m):
    n = len(arr)
    m = m % n
    return arr[m:]+arr[:m]


def rand(arr, n):
    res = []
    for i in range(n):
        index = choice(range(len(arr) - i))
        res.append(arr[index])
        arr[index] = arr[len(arr) - i - 1]

    return res


if __name__ == '__main__':
    # print(move([1,2,3,4,5,6],1))
    print(rand([1,2,3,4,5,6],4))





