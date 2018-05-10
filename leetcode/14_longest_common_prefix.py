#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 14. Longest Common Prefix
def test_longest_common_prefix():
    '''
    思路：
    时间复杂度：O(n*m) m为最大前缀字符串长度
    '''
    def longest_common_prefix(strs):
        # i 为字符内下标， j 为数组下标
        if len(strs) < 2:
            return strs[0] if len(strs) == 1 else ''

        i, j = -1, 0
        flag = True
        while flag:
            j = 0
            i += 1
            while j < len(strs) - 1:
                try:
                    if strs[j][i] != strs[j+1][i]:
                        flag = False
                        break
                    else:
                        j += 1
                except IndexError:
                    flag = False
                    break

        return strs[0][0:i]


    '''
    思路：
    时间复杂度：O(n*m)
    '''
    def longest_common_prefix2(strs):
        pre = strs[0] if len(strs) > 0 else ''

        i = 1
        while i < len(strs):
            if len(pre) == 0:
                return ''
            if strs[i].find(pre) != 0:
                pre = pre[0:len(pre)-1]
                i = 1
            else:
                i += 1

        return pre

    '''
    思路：
    时间复杂度：O(n)
    '''
    def longest_common_prefix3(strs):
        if not strs:
            return ''
        '''
        *str : unpacking list, 可将list 拆解成多个参数传入函数参数
        zip : 将传入的多个参数对应位置的字符配对
        '''
        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][0:i]

        return min(strs)

    print()
    print(longest_common_prefix3(['fasf', 'fasggg', 'add']))
