#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 53. Maximum Subarray
def test_max_sub_array():
    '''
    思路：创建dp数组，用来存放nums数组中第i个数时，与i前个数的最大和
    时间复杂度：
    '''

    def method1(nums):
        dp = [0] * len(nums)
        dp[0] = nums[0]

        for i in range(1, len(nums)):
            if dp[i - 1] < 0:
                dp[i] = nums[i]
            else:
                dp[i] = dp[i - 1] + nums[i]
        return max(dp)

    print()
    print(method1([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
