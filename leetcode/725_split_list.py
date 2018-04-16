#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 725. Split Linked List in Parts
'''未完成'''
def test_split_list():
    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    def split_list2(root, k):
        n = 1
        head = root
        res = []
        while head.next is not None:
            n += 1
            head = head.next
        h, d = n // k, n % k
        for j in range(k):
            res.append(None)
            if j < d:
                temp = root
                for i in range(h+1):
                    root = root.next
                temp.next = None
                res[j] = temp
            else:
                for i in range(h):
                    res[j] = root
                    root = root.next

        return res

    ln = ListNode(1)
    temp = ln
    for i in range(2, 6):
        temp.next = ListNode(i)
        temp = temp.next
    print(split_list2(ln, 2))
