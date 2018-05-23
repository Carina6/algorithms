#!/usr/bin/env python
# -*- coding: utf-8 -*-
from queue import PriorityQueue

from models.generator import list_node_generator
from models.list_node import ListNode


# 24. Swap Nodes in Pairs
def test_swap_pairs():
    '''
    思路：拆分为两个排序链表的算法
    时间复杂度：
    '''

    def swap_pairs(head):
        if head.next is None:
            return head

        res = temp = ListNode(0)
        while head and head.next:
            temp.next = head.next
            temp.next.next = head
            head = head.next.next
            temp = temp.next.next

        if head is None:
            return res.next





        return res


    '''
    思路：采用PriorityQueue实现，PriorityQueue内部使用小堆排序
    时间复杂度：
    '''

    def merge_k_lists2(lists):
        res = temp = ListNode(0)
        q = PriorityQueue()

        for list_node in lists:
            if list_node:
                q.put((list_node.val, list_node))
        while not q.empty():
            # PriorityQueue ：每次get取最小的值
            temp.next = q.get()[1]
            temp = temp.next
            if temp.next:
                q.put((temp.next.val, temp.next))

        return res.next

    req = []
    l3 = list_node_generator([2, 6])
    req.append(l3)
    l1 = list_node_generator([3, 4, 5])
    req.append(l1)
    l2 = list_node_generator([1, 3, 4])
    req.append(l2)

    print()
    print(merge_k_lists2(req))
