#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 4. Median of Two Sorted Arrays
def test_find_median_sorted_arrays():
    '''
    思路：
    时间复杂度：
    '''
    def find_median_sorted_arrays(nums1, nums2):
        median_len = (len(nums1) + len(nums2)) // 2
        min = max = 0

        i1 = i2 = 0
        j1 = len(nums1) - 1
        j2 = len(nums2) - 1
        for i in range(median_len):

            if nums1[i1] <= nums2[i2] and i1 < j1:
                i1 += 1
            else:
                i2 += 1

            if nums1[j1] <= nums2[j2] and j2 > i2:
                j2 -= 1
            else:
                j1 -= 1



    print()
    print()
