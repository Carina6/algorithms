#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 21. Merge Two Sorted Lists
from models.generator import list_node_generator
from models.list_node import ListNode


def test_merge_two_lists():
    '''
    思路：
    时间复杂度：
    '''
    def merge_two_lists(l1, l2):
        t = res = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                res.next = l1
                l1 = l1.next
            else:
                res.next = l2
                l2 = l2.next
            res = res.next

        res.next = l1 or l2
        return t.next

    '''
    思路：递归
    时间复杂度：
    '''
    def merge_two_lists2(l1, l2):
        if not l1 or not l2:
            return l1 or l2

        if l1.val <= l2.val:
            l1.next = merge_two_lists2(l1.next, l2)
            return l1
        else:
            l2.next = merge_two_lists2(l1, l2.next)
            return l2

    l1 = list_node_generator([1, 2, 4])
    l2 = list_node_generator([1, 3, 4])
    print()
    print(merge_two_lists2(l1, l2))
