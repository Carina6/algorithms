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

        if s[0] not in ['-', '+', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] or len(s) == 0:
            return res

        i = 1 if s[0] in ['-', '+'] else 0
        while i < len(s):
            if s[i] in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                res = res * 10 + int(s[i])
                i += 1
            else:
                break

        if s[0] == '-':
            res = -res

        if res < -2147483648:
            res = -2147483648
        elif res > 2147483647:
            res = 2147483647

        return res

    print()
    print(str_to_int('010'))
