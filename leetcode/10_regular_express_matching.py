#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 10. Regular Expression Matching
def test_regular_express_match():
    '''
    思路：
    时间复杂度：
    '''
    def is_match(s, p):
        sl = len(s)
        pl = len(p)
        if sl == 0 or pl == 0:
            return False

        i, j = 0, 0
        while i < pl and j < sl:
            if p[i] in [s[j], '.']:
                i += 1
                j += 1
            elif p[i] == '*':
                if p[i-1] in [s[j], '.']:
                    j += 1
                elif i+1 < pl and p[i+1] in [s[j], '.']:
                    i += 2
                    j += 1
                else:
                    return False
            elif i+1 < pl and p[i+1] == '*':
                i += 2
            else:
                return False

        if i < pl and p[i] == '*':
            i += 1
            while i < pl:
                if p[i] not in ['*', s[sl - 1]] and p[i + 1] != '*':
                    return False
        if j == sl:
            if i == pl:
                return True

        return False
        # return j == sl

    print()
    print(is_match('aaa', 'ab*a*c*a'))
