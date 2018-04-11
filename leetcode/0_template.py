#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 2. 两数相加
def test_add_two_numbers():

    class ListNode:
        def __init__(self, x):
            self.val = x
            self.next = None

    '''
    思路：
    时间复杂度：
    '''
    def add_two_numbers(l1, l2):
        l3 = ListNode(0)

        res = l3
        temp = 0
        while l1 and l2:
            l3.next = ListNode(0)

            l3.val = (l1.val + l2.val) % 10 + temp
            temp = (l1.val + l2.val) // 10

            l1 = l1.next
            l2 = l2.next
            l3 = l3.next

        while l1:
            l3.next = ListNode(0)
            l3.val = (l1.val + l2.val) % 10 + temp
            temp = (l1.val + l2.val) // 10

            l1 = l1.next
            l3 = l3.next
            l2.val = 0

        while l2:
            l3.next = ListNode(0)
            l3.val = (l1.val + l2.val) % 10 + temp
            temp = (l1.val + l2.val) // 10

            l2 = l2.next
            l3 = l3.next
            l1.val = 0

        if temp != 0:
            l3.val = temp
        else:
            l3 = None

        return res

    print()
    t1 = ListNode(0)
    t2 = ListNode(0)
    test1 = t1
    test2 = t2
    for i in range(3):
        t1.val = i
        t1.next = ListNode(0)
        t1 = t1.next

        t2.val = i+5
        t2.next = ListNode(0)
        t2 = t2.next
    print(test1)
    print(test2)
    print()
