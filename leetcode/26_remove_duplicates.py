#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 26. Remove Duplicates from Sorted Array
def test_remove_duplicate():
    '''
    思路：
    时间复杂度：
    '''
    def remove_duplicate(nums):
        if len(nums) == 0:
            return 0

        index = 0
        temp = nums[0]
        for i in nums:
            if temp != i:
                index += 1
                nums[index] = i
                temp = i

        return index+1

    print()
    print(remove_duplicate([1, 1, 2, 3]))
