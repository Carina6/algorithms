#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 1. two sum
def test_two_sum():
    # 时间复杂度为O(n^2) 5368 ms
    def two_sum(nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j

    # 时间复杂度为O(n) 44 ms
    def two_sum2(nums, target):
        value_dict = {}
        for i in range(len(nums)):
            if target-nums[i] in value_dict.keys():
                return value_dict.get(target-nums[i]), i
            else:
                value_dict[nums[i]] = i
    print()
    print(two_sum2([2, 7, 11, 15], 17))
