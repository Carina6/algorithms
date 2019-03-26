#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 6. ZigZag Conversion
def test_zigzag_conversion():
    '''
    思路：
    时间复杂度：O(n) 168 ms
    '''
    def zigzag_conversion(s, numRows):
        res = []
        if numRows < 2:
            return s

        # 二维数组的行数，numRows + numRows -2
        row = 2 * numRows-2
        # 二维数组列数
        column = len(s) // row
        if len(s) % row > 0:
            column += 1

        # 初始化二维数组，row x column
        N = [[None for x in range(column)] for y in range(row)]

        for i in range(len(s)):
            column_i = i // row
            row_i = i % row
            N[row_i][column_i] = s[i]

        for j in range(numRows):
            for k in range(column):
                if N[j][k]:
                    res.append(N[j][k])
                if j % numRows not in [0, numRows-1] and N[row-j][k]:
                    res.append(N[row-j][k])

        return ''.join(res)

    '''
    思路：使用numRows个数组存字符串值
    时间复杂度：O(n) 108 ms
    '''
    def zigzag_conversion2(s, numRows):
        if numRows < 2:
            return s

        L = [[]]*numRows
        j = 0
        while j < len(s):
            for k in range(numRows):
                if j < len(s):
                    L[k].append(s[j])
                    j += 1
            for h in range(numRows-2, 0, -1):
                if j < len(s):
                    L[h].append(s[j])
                    j += 1
        res = ''
        for i in range(numRows):
            res += ''.join(L[i])

        return res

    '''
    思路：使用numRows个字符串，按照Z字形存储字符
    时间复杂度：O(n) 80 ms
    '''
    def zigzag_conversion3(s, numRows):
        if numRows < 2:
            return s

        # 定义numRows个数组
        L = ['']*numRows

        index, step = 0, 1
        for x in s:
            L[index] += x
            # 当Z字形向下时，step = 1
            if index == 0:
                step = 1
            # 当Z字形向上时，step = -1
            elif index == numRows-1:
                step = -1
            index += step

        return ''.join(L)


    print()
    print(zigzag_conversion3('PAYPALISHIRING', 3))
