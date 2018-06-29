#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 30. Substring with Concatenation of All Words
import itertools


def test_find_sub_str():
    '''
    思路：
    时间复杂度：
    '''

    def find_sub_str(s, words):
        words_list = list(itertools.permutations(words))
        wl = []
        res = []
        for w in words_list:
            wl.append(''.join(w))
        # print(wl)

        if len(wl) == 0:
            return res

        m = len(wl[0])
        if m == 0 or len(s) == 0:
            return res

        for i in range(len(s)):
            sub_str = s[i:i + m]
            if len(sub_str) < m:
                break
            if sub_str in wl:
                res.append(i)

        return res

    print()
    print(find_sub_str('barfoothefoobarman', ["foo", "bar"]))
