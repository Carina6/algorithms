#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
from itertools import combinations, starmap


# 16. 3Sum Closest
def test_three_sum_closest():
    '''
    思路：
    时间复杂度：O(n^3)
    '''
    def three_sum_closest(nums, target):
        res = None
        # 产生不重复的组合
        cbs = list(combinations(nums, 3))
        closest = sys.maxsize
        i = 0
        for item in starmap(add, cbs):
            if abs(item-target) < closest:
                closest = abs(item-target)
                res = item
            i += 1

        return res

    def add(a, b, c):
        return a+b+c

    '''
    思路：
    时间复杂度：O(n^2)
    '''
    def three_sum_closest2(nums, target):
        nums.sort()

        res = 0
        closest = sys.maxsize
        for i in range(len(nums)-2):
            l, h = i+1, len(nums)-1
            while l < h:
                sum = nums[l] + nums[h] + nums[i]
                if sum == target:
                    return sum

                if abs(sum-target) < closest:
                    closest = abs(sum-target)
                    res = sum
                if sum < target:
                    l += 1
                else:
                    h -= 1

        return res

    print()
    print(three_sum_closest2([-1, 2, 1, -4], 3))
