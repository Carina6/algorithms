#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/8/8 16:50
# @Author: hlliu
from models.generator import list_node_generator


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        p = None
        l = pHead
        tmp = l.next
        l.next = p
        while tmp:
            p = l
            l = tmp
            tmp = tmp.next
            l.next = p
        return l

if __name__ == '__main__':
    s = Solution()
    l = list_node_generator([1,2,3,4,5,6])
    print(s.ReverseList(l))