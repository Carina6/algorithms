#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/8/8 13:46
# @Author: hlliu


class Solution:
    def Fibonacci(self, n):
        # write code here
        if n == 0:
            return 0
        elif n == 1:
            return 1
        res_n_1 = 1
        res_n_2 = 0
        res_n = 0
        for i in range(2, n+1):
            print(i)
            res_n = res_n_1+res_n_2
            res_n_2 = res_n_1
            res_n_1 = res_n
        return res_n


if __name__ == '__main__':
    s = Solution()
    res = s.Fibonacci(5)
    print(res)