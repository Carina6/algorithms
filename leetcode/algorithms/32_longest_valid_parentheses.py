#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 32. Longest Valid Parentheses
from queue import LifoQueue


def test_longest_valid_parentheses():
    '''
    思路：
    时间复杂度：
    '''

    def longest_valid_parentheses(s):
        stack = LifoQueue()
        res, index, temp = 0, -1, 0
        for i in range(len(s)):
            if stack.empty():
                stack.put(s[i])
            else:
                top = stack.get()
                if top + s[i] == '()':
                    if i - index == 2:
                        temp += 2
                    else:
                        res = res if res > temp else temp
                        temp = 0
                else:
                    stack.put(top)
                    stack.put(s[i])
                    res = res if res > temp else temp
                    temp = 0
            index = i
        return res

    print()
    print(longest_valid_parentheses("(()"))
