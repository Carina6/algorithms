#!/usr/bin/env python
# -*- coding: utf-8 -*-

from models.generator import list_node_generator
from models.list_node import ListNode


# 24. Swap Nodes in Pairs
def test_swap_pairs():
    '''
    思路：
    时间复杂度：
    '''

    def swap_pairs(head):
        if head is None or head.next is None:
            return head

        res = temp = ListNode(0)
        while head and head.next:
            temp.next = ListNode(head.next.val)
            temp.next.next = ListNode(head.val)
            head = head.next.next
            temp = temp.next.next

        if head is None:
            return res.next

        if head.next is None:
            temp.next = head

        return res.next

    l3 = list_node_generator([1, 2, 3, 4, 5, 6])

    print()
    print(swap_pairs(l3))
