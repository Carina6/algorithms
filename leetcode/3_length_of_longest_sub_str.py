#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 3. Longest Substring Without Repeating Characters
def test_length_of_longest_sub_str():
    '''
    思路：
    时间复杂度：
    '''
    def length_of_longest_sub_str(s):
        dict = {}
        start = end = length = 0
        for i in range(len(s)):
            if s[i] in dict.keys():
                index = dict.get(s[i])
                start1 = min(dict.values())
                end1 = max(dict.values())
                if end1 - start1+1 > length:
                    length = end1 - start1 +1
                    start = start1
                    end = end1
                dict = {}
                for j in range(index+1, i+1):
                    dict[s[j]] = j
            else:
                dict[s[i]] = i

        return s[start:end]

    print()
    print(length_of_longest_sub_str('abcabcbb'))
