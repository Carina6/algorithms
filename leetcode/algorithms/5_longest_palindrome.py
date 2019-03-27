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
        for i in range(1, 2 * s_len + 1):
            # i_len :以当前遍历的字符为中心的回文长度
            if i % 2 == 1:
                l = (i - 2) // 2
                r = (i + 2) // 2
                i_len = 1
            else:
                l = (i - 1) // 2
                r = (i + 1) // 2
                i_len = 0

            while l >= 0 and r < s_len:
                if s[l] == s[r]:
                    i_len += 2
                    l -= 1
                    r += 1
                else:
                    break

            if i_len > max_len:
                max_len = i_len
                start = l + 1

        return s[start:start + max_len]

    '''
    分奇偶回文，遍历每个数组，朝两边扩
    '''
    def method2(str):
        if len(str) <= 1:
            return str
        res = ''
        for i in range(len(str)):
            tmp = longest_palind(str, i, i)
            res = tmp if len(tmp) > len(res) else res
            tmp = longest_palind(str, i, i+1)
            res = tmp if len(tmp) > len(res) else res
        return res

    def longest_palind(s, l, r):
        while l >= 0 and r <= len(s) - 1 and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

    print()
    # print(longest_palindrome('bb'))

    print(method2('ababc'))
