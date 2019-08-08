#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date  : 2019/8/8 17:37
# @Author: hlliu
from models.generator import list_node_generator
from models.list_node import ListNode


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        res = tmp = ListNode(0)
        while pHead1 and pHead2:
            if pHead1.val <= pHead2.val:
                tmp.next = pHead1
                pHead1 = pHead1.next
            else:
                tmp.next = pHead2
                pHead2 = pHead2.next
            tmp = tmp.next
        while pHead1:
            tmp.next = pHead1
            pHead1 = pHead1.next
            tmp = tmp.next
        while pHead2:
            tmp.next = pHead2
            pHead2 = pHead2.next
            tmp = tmp.next

        return res.next


if __name__ == '__main__':
    s = Solution()
    l1 = list_node_generator([1,3,5,7])
    l2 = list_node_generator([2,4,5,6,8])
    print(s.Merge(l1,l2))