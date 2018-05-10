#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 11. Container With Most Water
def test_max_area():
    '''
    思路：暴力遍历计算两两直线面积，选取最大
    时间复杂度：O(N^2)
    '''
    def max_area(height):
        maxa = 0
        for i in range(len(height)-1):
            for j in range(1, len(height)):
                mini = min(height[i], height[j])
                temp = mini * (j-i)
                maxa = max(maxa, temp)

        return maxa

    '''
    思路：
    1.暴力计算时，相当于用该数组组成一个二维数组，N[i][j]为第i个数和第j个数所围成的面积值
    对此进行优化，不必要计算每个N[i][j]
    步骤：
    1.取数组两端开始计算，如果左边较小，则此行最大值即为当前计算的值；如果右边较小，则此列最大值即为当前计算值
    时间复杂度：O(N)
    '''
    def max_area2(height):
        maxa = 0
        i, j = 0, len(height)-1
        while i < j:
            if height[i] < height[j]:
                temp = height[i] * (j-i)
                i += 1
            else:
                temp = height[j] * (j-i)
                j -= 1
            maxa = max(temp, maxa)

        return maxa

    print()
    print(max_area2([1,1]))