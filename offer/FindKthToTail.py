#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/8/8 16:10
# @Author: hlliu


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if not head or k < 0:
            return None
        a = b = head

        while a:
            a = a.next
            if k > 0:
                k -= 1
            else:
                b = b.next

        return None if k > 0 else b
