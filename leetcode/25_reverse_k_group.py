#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 25. Reverse Nodes in k-Group

from models.generator import list_node_generator
from models.list_node import ListNode


def test_reverse_k_group():
    '''
    思路：
    时间复杂度：
    '''
    def reverse_k_group(head, k):
        t = head
        n = 0
        res = temp = ListNode(0)
        while t:
            n += 1
            if n == k:
                tt = t.next
                t.next = None
                temp.next = reversed(head)
                while temp.next:
                    temp = temp.next
                temp.next = reverse_k_group(tt, k)
                return res.next
            else:
                t = t.next

        if head:
            temp.next = head

        return res.next

    l = list_node_generator([1, 2, 3, 4, 5, 6])

    print()
    print(reverse_k_group(l, 3))

