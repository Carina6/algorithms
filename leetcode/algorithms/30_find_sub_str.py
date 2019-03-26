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

    '''
    思路：
    时间复杂度：
    '''

    def find_sub_str2(s, words):
        res = []
        if len(words) == 0 or len(s) == 0:
            return res

        words_count = {}
        for i in words:
            words_count[i] = words_count[i] + 1 if i in words_count.keys() else 1

        n = len(words)
        m = len(words[0])
        # len(s)-n*m+1 剩余长度没有达到words总长度，可不必遍历
        for i in range(len(s) - n * m + 1):
            res_dict = {}
            j = 0
            while j < n:
                st = s[i + j * m:i + (j + 1) * m]
                if st in words:
                    res_dict[st] = res_dict[st] + 1 if st in res_dict else 1
                    if res_dict[st] > words_count[st]:
                        break
                else:
                    break
                j += 1
            if j == n:
                res.append(i)
        return res

    print()
    print(find_sub_str2('wordgoodgoodgoodbestword', ["word", "good", "best", "good"]))
