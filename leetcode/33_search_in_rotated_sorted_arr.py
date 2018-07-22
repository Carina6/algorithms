#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 33. Search in Rotated Sorted Array
def test_search():
    '''
    思路：
    时间复杂度：
    '''

    def search(nums, target):
        try:
            res = nums.index(target)
            return res
        except ValueError:
            return -1

    # 二分法
    def search2(nums, target):
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
    print(search2([4, 5, 6, 7, 0, 1, 2], 0))
