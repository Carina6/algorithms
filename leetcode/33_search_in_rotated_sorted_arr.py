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
        if l ==0:
            return -1

        pass

    print()
    print(search([4,5,6,7,0,1,2], 0))
