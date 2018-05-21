#!/usr/bin/env python
# -*- coding: utf-8 -*-


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        s = str(self.val)
        temp = self
        while temp.next:
            s = s + '->' + str(temp.next.val)
            temp = temp.next

        return s

    # def __cmp__(self, other):
    #     if self.val < other.val:
    #         return -1
    #     elif self.val > other.val:
    #         return 1
    #     else:
    #         return 0
    #
    def __lt__(self, other):
        return self.val < other.val
