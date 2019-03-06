#!/usr/bin/env python
# -*- coding: utf-8 -*-
from queue import PriorityQueue

from models.generator import list_node_generator
from models.list_node import ListNode


# 23. Merge k Sorted Lists
def test_merge_k_lists():
    '''
    思路：拆分为两个排序链表的算法
    时间复杂度：
    '''

    def merge_k_lists(lists):
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

        if not lists:
            return None

        res = lists[0]
        for i in range(1, len(lists)):
            res = merge_two_lists(res, lists[i])

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
