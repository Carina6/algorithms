#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models.generator import list_node_generator
from models.list_node import ListNode


def test_a():
    def reverse_link_list(l):
        i = ListNode(l.val)
        j = l.next
        while j:
            temp = j.next
            j.next = i
            i = j
            j = temp

        return i

    print(reverse_link_list(list_node_generator([1, 2, 3, 4, 5])))
