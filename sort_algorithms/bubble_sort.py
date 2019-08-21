#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-21 22:48
# @Author  : hlliu


class BubbleSort:
    def __int__(self):
        pass

    def sort(self, arr):
        if not arr or len(arr) == 0:
            return
        for i in range(len(arr)):
            for j in range(len(arr) - 1, i, -1):
                if arr[j] < arr[j - 1]:
                    arr[j], arr[j - 1] = arr[j - 1], arr[j]


if __name__ == '__main__':
    bs = BubbleSort()
    arr = [4, 3, 5, 6]
    bs.sort(arr)
    print(arr)
