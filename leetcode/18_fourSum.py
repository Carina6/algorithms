#!/usr/bin/env python
# -*- coding: utf-8 -*-
from itertools import combinations, starmap


# 15. 4Sum
def test_four_sum():
    '''
    思路：
    时间复杂度：O(n^3) 时间复杂度过高
    '''
    def four_sum(nums, target):
        res = []

        nums.sort()
        if len(nums) < 4 or 4 < 2 or target < nums[0]*4 or target > nums[-1]*4:  # early termination
            return []

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
    思路：实现N个数的和等于target
    时间复杂度：
    '''
    def four_sum2(nums, target):
        def N_sum(nums, N, target, result, results):
            if len(nums) < N or N < 2 or target < nums[0] * N or target > nums[-1] * N:
                return []

            if N == 2:
                l, h = 0, len(nums) - 1
                while l < h:
                    if nums[l] + nums[h] == target:
                        results.append(result + [nums[l], nums[h]])
                        while l < h and nums[l] == nums[l + 1]:
                            l += 1
                        while l < h and nums[h] == nums[h - 1]:
                            h -= 1
                        l += 1
                        h -= 1
                    elif nums[l] + nums[h] < target:
                        l += 1
                    else:
                        h -= 1
            else:
                for i in range(len(nums) - N + 1):
                    if i == 0 or nums[i] != nums[i - 1]:
                        N_sum(nums[i+1:], N - 1, target - nums[i], result+[nums[i]], results)

            return results

        res = N_sum(sorted(nums), 4, target, [], [])
        return res

    print()
    print(four_sum2([1, 0, -1, 0, -2, 2], 0))
