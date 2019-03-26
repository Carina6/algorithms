#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 27. Remove Element
def test_remove_element():
    '''
    思路：
    时间复杂度：
    '''
    def remove_element(nums, val):
        if len(nums) == 0:
            return 0

        index = 0
        for i in range(len(nums)):
            if nums[i] != val:
                if index < i:
                    nums[index] = nums[i]
                index += 1

        return index

    print()
    print(remove_element([1, 1, 1, 1],1))
