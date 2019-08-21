#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-07 22:48
# @Author  : hlliu


class Solution:
    def NumberOf1(self, n):
        # write code here
        if n < 0:
            n = n & 0xffffffff
        count = 0
        while n != 0:
            count += 1
            n = (n-1) & n
        return count
