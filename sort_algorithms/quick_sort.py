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


def method2(nums):
    if len(nums) < 2:
        return

    sort(nums, 0, len(nums) - 1)


def sort(nums, start, end):
    if start > end:
        return
    patation = nums[start]
    low = start
    high = end
    while start < end:
        while start < end and nums[end] > patation:
            end -= 1
        nums[start] = nums[end]
        while start < end and nums[start] <= patation:
            start += 1
        nums[end] = nums[start]
    nums[start] = patation
    sort(nums, low, start-1)
    sort(nums, start+1, high)


nums = [3, 4, 6, 2, 4, 9]
method2(nums)
print(nums)