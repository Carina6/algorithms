#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 387. First Unique Character in a String
def test_first_uniq_char():

    # java算法最佳 200ms
    def firstUniqChar(s):
        if len(s) == 0:
            return -1
        arr = []
        for i in range(26):
            arr.append(0)
        for i in range(len(s)):
            arr[ord(s[i])-ord('a')] += 1
        for i in range(len(s)):
            if arr[ord(s[i])-ord('a')] == 1:
                return i
        return -1

    # Python算法 最佳， 90+ms
    def firstUniqChar2(s):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        index = [s.index(l) for l in letters if s.count(l) == 1]
        return min(index) if len(index) > 0 else -1

    print(firstUniqChar2('aadadaad'))
