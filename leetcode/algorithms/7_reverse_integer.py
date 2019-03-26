#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 7. Reverse Integer
def test_reverse_integer():
    '''
    思路：
    时间复杂度：O(n) 64 ms
    '''
    def reverse_integer(x):
        s = str(x)
        length = len(s)
        index = length-1
        res = 0

        if x < 0:
            i = 1
            index -= 1
        else:
            i = 0

        for j in range(length-1, i-1, -1):
            res += int(s[j])*pow(10, index)
            index -= 1

        if x < 0:
            res = -res

        if res < -2147483648 or res > 2147483647:
            return 0
        else:
            return res


    '''
    思路：
    时间复杂度：O(n)  56 ms
    '''
    def reverse_integer2(x):
        res = 0
        flag = True if x < 0 else False
        x = abs(x)
        while x:
            tail = x % 10
            res = res * 10 + tail
            x = x // 10

        res = -res if flag else res
        if res < -2147483648 or res > 2147483647:
            return 0
        else:
            return res


    print()
    print(reverse_integer2(-123))
