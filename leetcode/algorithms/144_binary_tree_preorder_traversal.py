#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/5/21 14:59
# @Author: hlliu
from queue import LifoQueue

from models.binary_tree import TreeNode


class Solution:
    def preorderTraversal(self, root: TreeNode):
        res = []
        stack = LifoQueue()
        cur = root

        while cur is not None or not stack.empty():
            if cur is not None:
                stack.put(cur)
                res.append(cur.val)
                cur = cur.left
            else:
                cur = stack.get().right
        return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)

s = Solution()
print(s.preorderTraversal(root))