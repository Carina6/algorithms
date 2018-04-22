#!/usr/bin/env python
# -*- coding: utf-8 -*-
import numpy


# 6. ZigZag Conversion
def test_zigzag_conversion():
    '''
    思路：
    时间复杂度：O(n) 140 ms
    '''
    def zigzag_conversion(s, numRows):
        res = []
        if numRows < 2:
            return s

        column = len(s) // (2 * numRows-2)
        if len(s) % (2*numRows-2) > 0:
            column += 1
        # N1 = numpy.zeros([column, numRows])
        N1 = [[None for x in range(2 * numRows-2)] for y in range(column)]
        for i in range(len(s)):
            row_i = i // (2*numRows-2)
            column_i = i % (2*numRows-2)
            N1[row_i][column_i] = s[i]

        for j in range(numRows):
            for k in range(column):
                if N1[k][j]:
                    res.append(N1[k][j])
                if j % numRows not in [0, numRows-1] and N1[k][2*numRows-2-j]:
                    res.append(N1[k][2*numRows-2-j])

        return ''.join(res)

    print()
    print(zigzag_conversion('ABCDE', 4))
