#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 28. Implement strStr()
def test_str_str():
    '''
    思路：
    时间复杂度：
    '''

    def str_str(haystack, needle):
        if len(haystack) < len(needle):
            return -1
        if len(haystack) == len(needle) and len(haystack) == 0:
            return 0

        for i in range(len(haystack)):
            flag = True
            for j in range(len(needle)):
                if i + j >= len(haystack):
                    return -1
                elif haystack[i + j] != needle[j]:
                    flag = False
                    break
            if flag:
                return i

        return -1

    print()
    print(str_str('', ''))
