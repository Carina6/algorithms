#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import product


# 17. Letter Combinations of a Phone Number
def test_letter_combinations():
    '''
    思路：
    时间复杂度：
    '''
    def letter_combinations(digits):
        res = []
        if not digits:
            return res

        c = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        temp = list(c[int(digits[0])])
        for i in range(1, len(digits)):
            if c[int(digits[i])] == '':
                continue
            elif len(temp) == 0:
                temp = c[int(digits[i])]
            else:
                temp = list(product(temp, c[int(digits[i])]))

            if len(temp[0]) == 2:
                res = []
                for j in range(len(temp)):
                    res.append(temp[j][0]+temp[j][1])
                temp = res

        return temp

    '''
    思路：
    时间复杂度：
    '''
    def letter_combinations2(digits):
        res = []
        if not digits:
            return res

        c = ['', '', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

        groups = product(*(c[int(d)] for d in digits if c[int(d)] != ''))
        res = [''.join(x) for x in groups]

        return res

    print()
    print(letter_combinations2('234'))
