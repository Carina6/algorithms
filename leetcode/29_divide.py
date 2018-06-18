#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 29. Divide Two Integers
def test_devide():
    '''
    思路：
    时间复杂度：
    '''

    def devide(dividend, divisor):
        res = 0
        a, b = abs(dividend), abs(divisor)

        while a >= b:
            temp, i = b, 1
            while a >= temp:
                a = a - temp
                res += i
                i <<= 1       # i<<=1等价于  i=i*2, 左移两位即乘2
                temp <<= 1

        if dividend * divisor < 0:
            res = -res

        return min(2147483647, max(res, -2147483648))

    print()
    print(devide(-2147483648, -1))
