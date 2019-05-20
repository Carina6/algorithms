#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/5/20 16:13
# @Author: hlliu


class Solution:

    # 计算每个颜色出现的次数，然后重组nums数组
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero = one = two = 0
        for i in nums:
            if i == 0:
                zero += 1
            elif i == 1:
                one += 1
            elif i == 2:
                two += 1

        for i in range(len(nums)):
            if i < zero:
                nums[i] = 0
            elif i < zero + one:
                nums[i] = 1
            else:
                nums[i] = 2
        # nums = [0] * zero + [1] * one + [2] * two

    # 三个指针，一个表示0的index，一个表示2的index，一个遍历数组nums
    # 1.选出数组值为2的放到数组尾部
    # 2.数组前部分交换0,1的位置
    def sortColors2(self, nums):
        zero = 0
        two = len(nums) - 1
        i = 0
        # nums[two]以上的数组已经排好
        while i <= two:
            if nums[i] == 0:
                nums[zero], nums[i] = nums[i], nums[zero]
                zero += 1
                i += 1
            elif nums[i] == 1:
                i += 1
            elif nums[i] == 2:
                nums[two], nums[i] = nums[i], nums[two]
                two -= 1


obj = Solution()
nums = [2, 1, 2, 0, 0, 1]
obj.sortColors2(nums)
print(nums)
