#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/5/21 9:26
# @Author: hlliu

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from queue import LifoQueue

from models.binary_tree import TreeNode


class Solution:
    def inorderTraversal(self, root):
        res=[]
        stack = LifoQueue()
        cur = root
        while cur is not None or not stack.empty():
            if cur is not None:
                stack.put(cur)
                cur = cur.left
            else:
                cur = stack.get()
                res.append(cur.val)
                cur = cur.right
        return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

s = Solution()
s.inorderTraversal(root)