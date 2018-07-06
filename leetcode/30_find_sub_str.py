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
        res=[]
        if len(words) == 0 or len(s)==0:
            return res

        words_count = {}
        for i in words:
            words_count[i] = 1 if words_count[i] is None else words_count[i]+1

        n = len(words)
        m = len(words[0])
        j = 0
        res_dict = {}
        count = 0
        for i in range(len(s)):
            k = i
            while k < len(s)-m:
                st = s[k:k+j*m]
                if st in words:
                    res_dict[st] = 1 if res_dict[st] is None else res_dict[st]+1
                else:
                    for v in res_dict.values():
                        count+=v
                    if count == n:
                        res.append(i)
                    else:
                        j = 0
                        count = 0
                        res_dict = {}

                if res_dict[st] > words_count[st]:
                    j=0
                    res_dict={}


        return res

    print()
    print(find_sub_str2('barfoothefoobarman', ["foo", "bar"]))
