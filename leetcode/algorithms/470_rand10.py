#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 470. Implement Rand10() Using Rand7()
from random import choice


def test_rand10():
    def method1():
        i = 7
        while i > 6:  # 生成rand2, 也可生成rand6，接近rand7，耗时少
            i = rand7()
        j = 6
        while j > 5:  # 生成rand5
            j = rand7()
        if i % 2 == 0:
            return j
        else:
            return j + 5

    def rand7():
        return choice([1, 2, 3, 4, 5, 6, 7])

    print()
    print(method1())
