#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models.list_node import ListNode


# 2. 两数相加（链表）
def test_add_two_numbers():
    '''
    思路：
    时间复杂度：O(n)
    '''
    def add_two_numbers1(l1, l2):
        l3 = ListNode(0)
        res = l3
        temp = 0
        while l1 and l2:
            l3.val = (l1.val + l2.val + temp) % 10
            temp = (l1.val + l2.val + temp) // 10

            l1 = l1.next
            l2 = l2.next

            if l1 or l2:
                l3.next = ListNode(0)
                l3 = l3.next

        while l1:
            l3.val = (l1.val + temp) % 10
            temp = (l1.val + temp) // 10

            l1 = l1.next

            if l1:
                l3.next = ListNode(0)
                l3 = l3.next

        while l2:
            l3.val = (l2.val + temp) % 10
            temp = (l2.val + temp) // 10

            l2 = l2.next

            if l2:
                l3.next = ListNode(0)
                l3 = l3.next

        if temp > 0:
            l3.next = ListNode(0)
            l3.next.val = temp

        return res

    # 方法一优化
    def add_two_numbers2(l1, l2):
        l3 = ListNode(0)

        res = l3
        carry = 0
        while l1 or l2:
            l3.next = ListNode(0)
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            l3.next.val = carry % 10
            carry = carry // 10

            l3 = l3.next

        if carry > 0:
            l3.next = ListNode(0)
            l3.next.val = carry

        return res.next

    # 方法2 优化，pythonic
    def add_two_numbers3(l1, l2):
        l3 = ListNode(0)
        res = l3
        carry = 0
        while l1 or l2 or carry:
            l3.next = ListNode(0)
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next

            # 获得商和余数
            carry, val = divmod(carry, 10)
            l3.next.val = val

            l3 = l3.next

        return res.next

    print()
    t1 = ListNode(0)
    t2 = ListNode(0)
    test1 = t1
    test2 = t2
    for i in range(1):
        t1.val = i+1
        t1.next = ListNode(2)
        t1 = t1.next

    for i in range(1):
        t2.val = 9
        t2.next = ListNode(9)
        t2 = t2.next
    print(test1)
    print(test2)
    print(add_two_numbers3(test1, test2))
