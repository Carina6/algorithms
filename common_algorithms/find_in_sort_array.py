#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/8/5 11:09
# @Author: hlliu

# 从左下角或者右上角开始查找


class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        if array is None or len(array) == 0:
            return False

        r_n = len(array)
        c_n = len(array[0])

        i = r_n - 1
        j = 0
        while i >= 0 and j < c_n:
            if array[i][j] == target:
                return True
            if array[i][j] < target:
                j+=1
            else:
                i-=1
        return False