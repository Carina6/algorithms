#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 8. String to Integer (atoi)
def test_str_to_int():
    '''
    思路：
    时间复杂度：O(n)  64 ms
    '''
    def str_to_int(str):
        s = str.strip()
        res = 0

        if len(s) == 0 or s[0] not in ['-', '+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return res

        i = 1 if s[0] in ['-', '+'] else 0
        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1

        sign = -1 if s[0] == '-' else 1

        return max(-2**31, min(res*sign, 2**31-1))

    print()
    print(str_to_int(''))
