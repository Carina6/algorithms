#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/4/3 14:14
# @Author: hlliu


# 二叉树深度
def method1(t):
    if t is None:
        return 0
    if t.left is None and t.right is None:
        return 1
    left = method1(t.left)
    right = method1(t.right)

    return 1 + max(left, right)
