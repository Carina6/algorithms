#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import combinations, starmap


# 15. 3Sum
def test_three_sum():
    '''
    思路：
    时间复杂度：O(n^3)
    '''
    def three_sum(nums):
        res = []
        # 产生不重复的组合
        cbs = list(combinations(nums, 3))
        res_temp = []
        i = 0
        for item in starmap(add, cbs):
            if item == 0:
                res_temp.append(cbs[i])
            i += 1

        for i in range(len(res_temp)):
            temp = sorted(res_temp[i])
            if temp not in res:
                res.append(temp)
        return res

    def add(a, b, c):
        return a+b+c

    '''
    思路：
    时间复杂度：
    '''
    def three_sum2(nums):
        nums.sort()

        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, h, sum = i+1, len(nums)-1, 0-nums[i]
            while l < h:
                if nums[l] + nums[h] == sum:
                    res.append([nums[i], nums[l], nums[h]])
                    while l < h and nums[l] == nums[l+1]:
                        l += 1
                    while l < h and nums[h] == nums[h-1]:
                        h -= 1
                    l += 1
                    h -= 1
                elif nums[l] + nums[h] < sum:
                    l += 1
                else:
                    h -= 1

        return res

    print()
    print(three_sum2([-1, 0, 1, 2, -1, -4]))
