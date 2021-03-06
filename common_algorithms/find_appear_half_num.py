#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/4/3 9:57
# @Author: hlliu


def method(nums):
    if len(nums) == 0:
        return None

    count = 1
    compare = nums[0]
    for i in range(1, len(nums)):
        if nums[i] == compare:
            count += 1
        else:
            count -= 1

        if count == 0:
            compare = nums[i]
            count = 1

    # 最后可遍历一遍，统计compare出现的次数，如果小于数组长度的一半，则返回空
    count = 0
    for i in nums:
        if i == compare:
            count += 1

    if count > len(nums)//2:
        return compare
    else:
        return None


if __name__ == '__main__':
    print(method([1, 2, 1, 4, 5, 3, 3]))
