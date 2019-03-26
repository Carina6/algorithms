#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-03-26 22:00
# @Author  : hlliu
from models.generator import list_node_generator
from models.list_node import ListNode


# 单链表反转
def test_reverse_link():
    '''
    空间换时间，使用数组存储链表中的值
    :return:
    '''

    def method1(ln):
        if ln is None or ln.next is None:
            return ln

        arr = []
        while ln.next:
            arr.append(ln.val)
            ln = ln.next
        arr.append(ln.val)

        ll = res = ListNode(0)
        for i in arr[::-1]:
            res.next = ListNode(i)
            res = res.next

        return ll.next

    '''
    使用三个指针，交换位置
    '''

    def method2(ln):
        if ln is None or ln.next is None:
            return ln

        res = ln
        tail = ln.next
        res.next = None
        while tail:
            tmp = tail.next
            tail.next = res
            res = tail
            tail = tmp

        return res

    l1 = list_node_generator([])
    l2 = list_node_generator([1, 3, 4, 9, 0, 7])
    print()
    print(method1(l1))
    print(method2(l2))
