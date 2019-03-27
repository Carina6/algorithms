#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 66. Plus One
def test_plus_one():
    '''
    思路：
    时间复杂度：
    '''

    def method1(digits):
        num = 0
        for i in range(len(digits)):
            num += digits[i] * pow(10, len(digits) - 1 - i)
        return [int(x) for x in str(num + 1)]

    print()
    print(method1([1, 2, 3]))
