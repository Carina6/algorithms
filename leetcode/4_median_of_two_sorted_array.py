#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 4. Median of Two Sorted Arrays
def test_find_median_sorted_arrays():
    '''
    思路：创建(m+n)/2 + 1长度的数组arr，存前(m+n)/2 + 1 个最小数，
         如果两数组长度和为奇数，则中位数为arr中的最后一位，为偶数，则为最后两位的平均数
    1.遍历nums1,nums2
    2.选取最小的存在arr
    时间复杂度：O(m+n) 116 ms
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

        imin, imax = 0, m-1
        k = (m + n + 1) // 2
        carry = (m + n) % 2

        while imin <= imax:
            c1 = imin + (imin + imax) // 2
            c2 = k-c1

            if c1 > 0 and A[c1-1] > B[c2]:
                imax = c1-1
            elif c2 > 0 and B[c2-1] > A[c1]:
                imin = c1+1
            else:
                lmax = 0
                if c1 > 0 and c2 > 0:
                    lmax = max(A[c1 - 1], B[c2 - 1])
                elif c1 > 0:
                    lmax = A[c1 - 1]
                elif c2 > 0:
                    lmax = B[c2 - 1]

                if carry == 0:
                    return (lmax + min(A[c1], B[c2])) / 2
                else:
                    return lmax

    print()
    print(find_median_sorted_arrays2([1,3], [2]))
