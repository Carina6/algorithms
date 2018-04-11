#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 1. 两数之和
def test_two_sum():
    '''
    思路：两两相加，找到即返回下标
    时间复杂度： O(n^2) 5368 ms
    '''
    def two_sum(nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return i, j


    '''
    思路：使用一个dict存储遍历过的值，key:数组值，value：下标；
    如果结果存在，则当遍历到目标第二个值时，dict中定会有一个值与之相加等于目标值
    时间复杂度：O(n)  44 ms
    '''
    def two_sum2(nums, target):
        value_dict = {}
        for i in range(len(nums)):
            if target-nums[i] in value_dict.keys():
                return value_dict.get(target-nums[i]), i
            else:
                value_dict[nums[i]] = i

    print()
    print(two_sum2([2, 7, 11, 15], 17))
