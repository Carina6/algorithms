#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 22. Generate Parentheses
def test_generate_parentheses():
    '''
    思路：
    时间复杂度：
    '''

    def generate_parentheses(n):
        res = []

        def generator(res, s, open, close, n):
            if len(s) == 2 * n:
                res.append(s)

            if open < n:
                generator(res, s + '(', open + 1, close, n)
            if close < open:
                generator(res, s + ')', open, close + 1, n)

        generator(res, '', 0, 0, n)
        return res

    print()
    print(generate_parentheses(2))
