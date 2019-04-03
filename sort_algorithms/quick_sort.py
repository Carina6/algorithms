#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/4/3 14:03
# @Author: hlliu


def method1(nums):
    if len(nums) < 2:
        return nums
    left = []
    right = []
    mid = [nums[0]]

    for i in range(1, len(nums)):
        if nums[i] < nums[0]:
            left.append(nums[i])
        if nums[i] > nums[0]:
            right.append(nums[i])
        if nums[i] == nums[0]:
            mid.append(nums[i])
    return method1(left) + mid + method1(right)


print(method1([3, 4, 6, 2, 4, 9]))
