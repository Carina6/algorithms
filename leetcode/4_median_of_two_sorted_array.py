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
        carry = (len(nums1) + len(nums2)) % 2

        i1 = i2 = 0
        arr = []
        for i in range(median_len + 1):

            if i1 < len(nums1) and i2 < len(nums2):
                if nums1[i1] < nums2[i2]:
                    arr.append(nums1[i1])
                    i1 += 1
                else:
                    arr.append(nums2[i2])
                    i2 += 1
            elif i1 == len(nums1) and i2 < len(nums2):
                arr.append(nums2[i2])
                i2 += 1
            elif i2 == len(nums2) and i1 < len(nums1):
                arr.append(nums1[i1])
                i1 += 1
            else:
                break

        if len(arr) == 0:
            return 0

        if carry > 0:
            return arr[median_len]
        else:
            return (arr[median_len-1] + arr[median_len]) / 2

    def find_median_sorted_arrays2(nums1, nums2):
        A, B = nums1, nums2
        m = len(A)
        n = len(B)
        if m > n:
            A, B, m, n = B, A, n, m

        k = m+n+1
        i = m+1
        j = k - i

        while True:
            l1 = (i-1)//2
            r1 = i//2
            l2 = (j-1)//2
            r2 = j//2

            if A[l1] > B[r2]:
                i = i//2
                j = k-i
            if B[l2] > A[r1]:
                # todo
                i += 1
                j = k-i
            else:
                return (max(A[l1], B[l2]) + min(A[r1], B[r2])) / 2


    print()
    print(find_median_sorted_arrays([1], [0]))
