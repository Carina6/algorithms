#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 34. Find First and Last Position of Element in Sorted Array
def test_search_range():
    '''
    思路：
    时间复杂度：
    '''

    def search_range(nums, target):
        res = []
        try:
            index = nums.index(target)
            res.append(index)
            index += 1
            while index < len(nums) and nums[index] == target:
                index += 1
            res.append(index-1)
            return res
        except ValueError:
            return [-1, -1]

    # 二分法
    def search_range2(nums, target):
        l = len(nums)
        if l == 0:
            return -1
        start, end = 0, l - 1
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[end]:
                start = mid + 1
            else:
                end = mid
        rot = start
        start, end = 0, l - 1
        while start <= end:
            mid = (start + end) // 2
            relmid = (mid + rot) % l
            if nums[relmid] < target:
                start = mid + 1
            elif nums[relmid] > target:
                end = mid - 1
            else:
                return relmid
        return -1

    print()
    print(search_range([5, 7, 7, 8, 8, 10], 8))
