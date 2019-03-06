#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 31. Next Permutation
def test_next_permutation():
    '''
    思路：
    时间复杂度：
    '''

    def next_permutation(nums):
        index = 0
        nums_len = len(nums)
        for i in range(len(nums) - 1, 0, -1):
            # 从最右边开始遍历，选取第一个小于后一位的数字，记录下标i-1
            if nums[i - 1] < nums[i]:
                # 截取i-1后的数组，并排序
                temp = nums[i - 1:nums_len]
                temp.sort()
                k = 0
                h = i
                flag = True  # flag表示是否找到截取数组中大于nums[i-1]的最小值
                while h <= nums_len-1:
                    # 因为temp 数组已经排序，所以第一个大于nums[i]的数即为截取数组中大于nums[i-1]的最小值
                    if flag and temp[k] > nums[i - 1]:
                        nums[i - 1] = temp[k]
                        flag = False
                    else:
                        # 从小标i开始依次填充数值
                        nums[h] = temp[k]
                        h += 1
                    k += 1
                if k < len(temp):
                    nums[i - 1] = temp[k]
                break
            index = i
        if index == 1:
            nums.reverse()
        return nums

    print()
    print(next_permutation([5, 4, 7, 5, 3, 2]))
