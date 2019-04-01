#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/3/29 12:44
# @Author: hlliu


def test_x_pow_n():

    def method1(x, n):
        tmp = x
        res = 1

        while n:
            if n&1 == 1:
                res *= tmp
            tmp = tmp*tmp
            n = n >> 1
        return res

    print(method1(2,3))