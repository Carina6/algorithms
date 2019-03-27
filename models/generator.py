#!/usr/bin/env python
# -*- coding: utf-8 -*-
from queue import Queue

from models.binary_tree import Node
from models.list_node import ListNode


def list_node_generator(nums):
    if len(nums) == 0:
        return None
    t = ListNode(nums[0])
    head = t
    for i in range(1, len(nums)):
        t.next = ListNode(nums[i])
        t = t.next
    return head


def tree_node_generator(nums):
    if len(nums) == 0:
        return None
    root = Node(nums[0])
    q = Queue()
    q.put(root)
    for i in range(1,len(nums),2):
        tmp = q.get()
        tmp.left = Node(nums[i])
        q.put(tmp.left)
        try:
            tmp.right = Node(nums[i + 1])
            q.put(tmp.right)
        except IndexError:
            pass

    return root
