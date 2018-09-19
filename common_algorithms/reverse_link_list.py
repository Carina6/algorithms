#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models.generator import list_node_generator
from models.list_node import ListNode


def test_a():
    def reverse_link_list(l):
        if l is None:
            return l
        i = ListNode(l.val)
        j = l.next
        while j:
            temp = j.next
            j.next = i
            i = j
            j = temp

        return i

    print(reverse_link_list(list_node_generator([])))
