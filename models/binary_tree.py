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


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __str__(self):
        if self is None:
            return
        if self.left is not None:
            self.left.__str__()

        print(self.val)

        if self.right is not None:
            self.right.__str__()
