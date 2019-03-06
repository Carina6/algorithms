#!/usr/bin/env python
# -*- coding: utf-8 -*-
from queue import LifoQueue


# 20. Valid Parentheses
def test_valid_parentheses():
    '''
    思路：
    时间复杂度：
    '''
    def is_valid(s):
        stack = LifoQueue()
        for i in s:
            if not stack.empty():
                top = stack.get()
                if top+i not in ['{}', '[]', '()']:
                    stack.put(top)
                    stack.put(i)
            else:
                stack.put(i)

        return stack.empty()

    '''
    思路：
    时间复杂度：
    '''
    def is_valid2(s):
        stack = LifoQueue()
        for i in s:
            if i == '(':
                stack.put(')')
            elif i == '{':
                stack.put('}')
            elif i == '[':
                stack.put(']')
            elif stack.empty() or stack.get() != i:
                return False

        return stack.empty()

    '''
    思路：
    时间复杂度：
    '''
    def is_valid3(s):
        s_len = len(s)
        t_s = s.replace('()', '').replace('[]', '').replace('{}', '')
        while len(t_s) != 0 and s_len > len(t_s):
            s_len = len(t_s)
            t_s = t_s.replace('()', '').replace('[]', '').replace('{}', '')
        return not t_s

    print()
    print(is_valid3('([])'))
