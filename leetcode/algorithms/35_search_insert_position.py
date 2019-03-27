#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 35.Search Insert Position
def test_search_insert_position():
    '''
    思路：
    时间复杂度：o(n)
    '''

    def method1(arr, target):
        return len([x for x in arr if x < target])

    '''
    二分法
    '''
    def method2(nums, target):
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid-1
            elif nums[mid] < target:
                low = mid+1
        return low

    print()
    print(method2([1, 3, 5, 6], 5))
