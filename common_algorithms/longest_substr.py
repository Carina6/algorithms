#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-26 23:09
# @Author  : hlliu


# 最大连续子序列
def test_longest_substr():
    def method1(str):
        if str is None or len(str) == 0:
            return 0
        index = max_count = 0
        count_tmp = 1
        for i in range(len(str) - 1):
            if str[i] == str[i + 1]:
                count_tmp += 1
            else:
                if max_count < count_tmp:
                    max_count = count_tmp
                    index = i - max_count + 1
                count_tmp = 1
        return str[index:index + max_count]

    print(method1('amcdddddlaeeefn'))
