#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models.list_node import ListNode


def list_node_generator(nums):
    t = ListNode(nums[0])
    head = t
    for i in range(1, len(nums)):
        t.next = ListNode(nums[i])
        t = t.next
    return head
