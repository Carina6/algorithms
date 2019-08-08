#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/8/8 14:13
# @Author: hlliu


class Solution:
    def reOrderArray(self, array):
        # write code here
        a = []
        b = []
        for i in array:
            if i % 2 == 1:
                a.append(i)
            else:
                b.append(i)
        return a + b

    def reOrderArray2(self, array):
        for i in range(len(array)):
            if array[i] % 2 == 1:
                for j in range(i, -1, -1):
                    if array[j] % 2 == 0:
                        array[j+1], array[j] = array[j], array[j+1]

        return array


if __name__ == '__main__':
    s = Solution()
    array = [1,2,3,4,5,6]
    s.reOrderArray2(array)
    print(array)