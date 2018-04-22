#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 5.Longest Palindromic Substring
def test_longest_palindrome():
    '''
    思路：使用'#'字符将字符串长度扩充到2*m+1, 循环遍历，往两边扩，比较两边的字符是否相等
    时间复杂度：O(n^2) 824 ms
    '''
    def longest_palindrome(s):
        # 最大回文的起始索引值
        start = 0
        # 最大回文长度
        max_len = 0
        # 字符串长度
        s_len = len(s)
        for i in range(1, 2*s_len+1):
            # i_len :以当前遍历的字符为中心的回文长度
            if i%2 == 1:
                l = (i-2)//2
                r = (i+2)//2
                i_len = 1
            else:
                l = (i-1)//2
                r = (i+1)//2
                i_len = 0

            while l >=0 and r <s_len:
                if s[l]==s[r]:
                    i_len += 2
                    l -= 1
                    r += 1
                else:
                    break

            if i_len > max_len:
                max_len = i_len
                start = l+1

        return s[start:start+max_len]

    print()
    print(longest_palindrome('bb'))
