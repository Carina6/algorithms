#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 31. Next Permutation
def test_next_permutation():
    '''
    思路：
    时间复杂度：
    '''

    def next_permutation(nums):
        index = 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i-1]:
                nums[i], nums[i-1] = nums[i-1], nums[i]
                index = i
                break
        if index == len(nums)-1:
            return nums.reverse()
        return nums

    print()
    print(next_permutation([3,2,1]))
