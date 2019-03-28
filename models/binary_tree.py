#!/usr/bin/env python
# -*- coding: utf-8 -*-
from queue import Queue


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        q = Queue()
        q.put(self)
        s = ''
        while not q.empty():
            tmp = q.get()
            s = s+str(tmp.val)
            if tmp.left:
                q.put(tmp.left)
            if tmp.right:
                q.put(tmp.right)
        return s


# class BinaryTree(object):
#     """
#     generate binary tree
#     """
#
#     def __init__(self, arr):
#         self.root = tree_node_generator(arr)
#
#     def __str__(self):
#         q = Queue()
#         q.put(self.root)
#         while not q.empty():
#             tmp = q.get()
#             print(tmp.val)
#             if tmp.left:
#                 q.put(tmp.left)
#             if tmp.right:
#                 q.put(tmp.right)
