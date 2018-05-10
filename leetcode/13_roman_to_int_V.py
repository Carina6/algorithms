#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 13. Roman to Integer
def test_int_to_roman():
    '''
    思路：
    时间复杂度：O(n)
    '''
    def roman_to_int(s):
        r_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        res = 0
        for i in range(len(s)-1):
            if r_d[s[i]] < r_d[s[i+1]]:
                res -= r_d[s[i]]
            else:
                res += r_d[s[i]]

        return res + r_d[s[-1]]

    '''
    思路：
    时间复杂度：O(1)
    '''
    def int_to_roman2(s):
        i, res = len(s)-1, 0
        while i >= 0:
            if s[i] == 'I':
                res += 1
                i -= 1
            if s[i] == 'V':
                if i-1 >= 0 and s[i-1] == 'I':
                    res += 4
                    i -= 2
                else:
                    res += 5
                    i -= 1
            if s[i] == 'X':
                if i-1 >= 0 and s[i-1] == 'I':
                    res += 9
                    i -= 2
                else:
                    res += 10
                    i -= 1
            if s[i] == 'L':
                if i - 1 >= 0 and s[i - 1] == 'X':
                    res += 40
                    i -= 2
                else:
                    res += 50
                    i -= 1
            if s[i] == 'C':
                if i-1 >= 0 and s[i-1] == 'X':
                    res += 90
                    i -= 2
                else:
                    res += 100
                    i -= 1
            if s[i] == 'D':
                if i - 1 >= 0 and s[i - 1] == 'C':
                    res += 400
                    i -= 2
                else:
                    res += 500
                    i -= 1
            if s[i] == 'M':
                if i - 1 >= 0 and s[i - 1] == 'C':
                    res += 900
                    i -= 2
                else:
                    res += 1000
                    i -= 1
        return res

    print()
    print(int_to_roman2('MCMXCIV'))
