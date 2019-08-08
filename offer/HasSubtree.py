#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/8/8 18:38
# @Author: hlliu

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        res = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                res = self.Tree1HasTree2(pRoot1, pRoot2)
            if not res:
                res = self.HasSubtree(pRoot1.left, pRoot2) or self.HasSubtree(pRoot1.right, pRoot2)
        return res

    def Tree1HasTree2(self, tree1, tree2):
        if not tree2:
            return True
        if not tree1:
            return False
        if tree1.val == tree2.val:
            return self.Tree1HasTree2(tree1.left, tree2.left) and self.Tree1HasTree2(tree1.right, tree2.right)
        else:
            return False