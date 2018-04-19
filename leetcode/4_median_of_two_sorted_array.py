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

    '''
    思路：创建(m+n)/2 + 1长度的数组arr，存前(m+n)/2 + 1 个最小数，
         如果两数组长度和为奇数，则中位数为arr中的最后一位，为偶数，则为最后两位的平均数
    1.遍历nums1,nums2
    2.选取最小的存在arr
    时间复杂度：O(log(min(m, n))) 108 ms
    '''
    def find_median_sorted_arrays2(nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        # 二分长度较小的数组，使时间复杂度更小
        if m > n:
            nums1, nums2, m, n = nums2, nums1, n, m

        # 二分法的初始最小，最大值
        imin, imax = 0, m
        # 两个数组的中位数的位置
        k = (m + n + 1) // 2
        # 两数组长度是奇数还是偶数
        carry = (m + n) % 2

        # 开始二分算法
        while imin <= imax:
            c1 = (imin + imax) // 2
            c2 = k-c1

            if c1 > 0 and nums1[c1-1] > nums2[c2]:
                # 分割点太大，减少
                imax = c1-1
            elif c1 < m and nums2[c2-1] > nums1[c1]:
                # 分割点太小， 增加
                imin = c1+1
            else:
                # 此时找到分割点c1
                # lmax 为两数组分割点左边的最大数
                if c2 == 0:
                    lmax = nums1[c1 - 1]
                elif c1 == 0:
                    lmax = nums2[c2 - 1]
                else:
                    lmax = max(nums1[c1 - 1], nums2[c2 - 1])

                if carry == 1:
                    return lmax

                # rmin 为两数组分割点右边的最小值
                if c1 == m:
                    rmin = nums2[c2]
                elif c2 == n:
                    rmin = nums1[c1]
                else:
                    rmin = min(nums1[c1], nums2[c2])

                return (lmax + rmin) / 2

    print()
    print(find_median_sorted_arrays2([2], [1]))
