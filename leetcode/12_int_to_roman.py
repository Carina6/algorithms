#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 12.Integer to Roman


def test_int_to_roman():
    '''
    思路：
    时间复杂度：O(n)
    '''
    def int_to_roman(num):
        r_c = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
        res = ''
        i = 0
        while num:
            d = num % 10
            num = num // 10
            s0 = d % 5
            s1 = d // 5
            if s1:
                if s0 == 4:
                    res = r_c[i]+r_c[i+2] + res
                else:
                    res = r_c[i+1]+r_c[i]*s0 + res
            else:
                if s0 == 4:
                    res = r_c[i]+r_c[i+1] + res
                else:
                    res = r_c[i]*s0 + res
            i += 2

        return res

    '''
    思路：
    时间复杂度：O(1)
    '''
    def int_to_roman2(num):
        I_V = ['', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX']
        X_L = ['', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC']
        C_D = ['', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM']
        M = ['', 'M', 'MM', 'MMM']

        return M[num // 1000] + C_D[(num % 1000) // 100] + X_L[(num % 100) // 10] + I_V[(num % 10)]

    print()
    print(int_to_roman2(40))
