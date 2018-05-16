#!/usr/bin/env python
# -*- coding: utf-8 -*-
from copy import deepcopy
from itertools import combinations, starmap


# 15. 4Sum
def test_four_sum():
    '''
    思路：
    时间复杂度：O(n^3) 时间复杂度过高
    '''
    def four_sum(nums, target):
        res = []
        # 产生不重复的组合
        cbs = list(combinations(nums, 4))
        res_temp = []
        i = 0
        for item in starmap(add, cbs):
            if item == target:
                res_temp.append(cbs[i])
            i += 1

        for i in range(len(res_temp)):
            temp = sorted(res_temp[i])
            if temp not in res:
                res.append(temp)
        return res

    def add(a, b, c, d):
        return a+b+c+d

    '''
    思路：
    时间复杂度：
    '''
    def four_sum2(nums, target):
        nums.sort()

        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            t_nums = deepcopy(nums)
            t_nums.pop(i)
            t_res = three_sum(t_nums, target-nums[i])
            for j in t_res:
                j.append(nums[i])
                res.append(j)

        return res

    def three_sum(nums, target):
        nums.sort()

        res = []
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, h, sum = i+1, len(nums)-1, target-nums[i]
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
    print(four_sum2([1, 0, -1, 0, -2, 2], 0))
