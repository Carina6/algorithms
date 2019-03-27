#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 58. Length of Last Word
def test_length_of_last_word():
    '''
    思路：
    时间复杂度：
    '''

    def method1(s):
        count = 0
        s = s.strip()
        for c in s[::-1]:
            if c == ' ':
                return count
            else:
                count += 1
        return count

    def method2(s):
        return len(s.strip().split(' ')[-1])

    print()
    print(method2('hello world  '))
