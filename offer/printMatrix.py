#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/8/8 19:20
# @Author: hlliu


class Solution:

    def printMatrix(self, matrix):
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            if matrix:
                res += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res

if __name__ == '__main__':
    s = Solution()
    l = [[1,2,3],[4,5,6],[7,8,9]]
    print(s.printMatrix(l))