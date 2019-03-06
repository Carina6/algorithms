#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 3. Longest Substring Without Repeating Characters
def test_length_of_longest_sub_str():
    '''
    思路：
    1.遍历
    2.存dict（值，下标）
    3.遇到重复
        3.1 取得第一个值下标
        3.2 比较赋值最长子串
        3.3 截取新的计算的子串（即第一个重复下标+1 开始）
    时间复杂度：O(n^2), 596ms
    '''
    def length_of_longest_sub_str1(s):
        dict = {}
        length = 0
        # start = end = 0

        for i in range(len(s)):
            if s[i] in dict.keys():
                index = dict.get(s[i])
                start_temp = min(dict.values())
                end_temp = max(dict.values())
                if end_temp - start_temp + 1 > length:
                    length = end_temp - start_temp + 1
                    # start = start_temp
                    # end = end_temp

                # 添加新的非重复的元素
                dict = {}
                for j in range(index+1, i+1):
                    dict[s[j]] = j
            else:
                dict[s[i]] = i

        if len(dict.items()) > length:
            length = len(dict.items())
            # start = min(dict.values())
            # end = max(dict.values())

        # print(s[start:end+1])
        return length

    '''
    思路：
    1.遍历
    2.存dict（值，下标）
    3.遇到重复
        3.1 获取最新比较子串的起始下标
    4.计算最长的子串
    时间复杂度：O(n), 152ms
    '''
    def length_of_longest_sub_str2(s):
        dict = {}
        # index 为新子串的起始下标
        length = index = 0

        # 每次都计算一次length
        for i in range(len(s)):
            if s[i] in dict.keys():
                index = max(index, dict.get(s[i]) + 1)

            dict[s[i]] = i
            length = max(length, i - index + 1)

        return length


    '''
    思路：
    1.遍历
    2.存dict（值，下标）
    3.遇到重复
        3.1 获取最新比较子串的起始下标
    4.计算最长的子串
    时间复杂度：O(n), 92 ms
    '''
    def length_of_longest_sub_str3(s):
        dict = {}
        # index 为新子串的起始下标
        length = index = 0

        # 当index无变化时计算length
        for i in range(len(s)):
            if s[i] in dict.keys() and index <= dict.get(s[i]):
                index = dict.get(s[i]) + 1
            else:
                length = max(length, i - index + 1)

            dict[s[i]] = i

        return length

    print()
    print(length_of_longest_sub_str3('tmmzuxt'))
