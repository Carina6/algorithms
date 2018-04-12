#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 3. Longest Substring Without Repeating Characters
def test_length_of_longest_sub_str():
    '''
    思路：
    1.0
    时间复杂度：O(n^2), 596ms
    '''
    def length_of_longest_sub_str(s):
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
    1.0
    时间复杂度：O(n), 152ms
    '''
    def length_of_longest_sub_str2(s):
        dict = {}
        length = index = 0

        for i in range(len(s)):
            if s[i] in dict.keys():
                index = max(index, dict.get(s[i]) + 1)

            dict[s[i]] = i
            length = max(length, i - index + 1)

        return length

    print()
    print(length_of_longest_sub_str2('bbbb'))
