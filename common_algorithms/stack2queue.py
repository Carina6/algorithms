#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/8/5 15:09
# @Author: hlliu
from queue import LifoQueue


class Solution:
    def __init__(self):
        self.a = LifoQueue()
        self.b = LifoQueue()

    def push(self, node):
        # write code here
        while not self.b.empty():
            self.a.put(self.b.get())
        self.a.put(node)

    def pop(self):
        # return xx
        while not self.a.empty():
            self.b.put(self.a.get())
        return self.b.get()


if __name__ == '__main__':
    s = Solution()
    s.push(1)
    print(s.pop())
