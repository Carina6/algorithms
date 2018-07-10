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
        j = len(nums) - 1
        for i in range(len(nums) - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                nums[i - 1], nums[j] = nums[j], nums[i - 1]
                temp = nums[i-1:j + 1]
                temp.sort()
                k = 0
                h = i
                while h <= j:
                    if temp[k] > nums[i]:

                    nums[h] = temp[k]
                    h += 1
                    k += 1
                break
            index = i
        if index == 1:
            nums.reverse()
        return nums

    print()
    print(next_permutation([2, 3, 1]))
