#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models.generator import list_node_generator


# 19. Remove Nth Node From End of List
def test_remove_nth_from_end():
    '''
    思路：
    时间复杂度：
    '''

    def remove_nth_from_end(head, n):
        t_head_len, t_head = head, head

        length = 0
        while t_head_len:
            length += 1
            t_head_len = t_head_len.next

        i = 0
        while i < length - n - 1:
            t_head = t_head.next
            i += 1
        if t_head == head:
            head = head.next
        else:
            t_head.next = t_head.next.next
        return head

    print()
    head = list_node_generator([1, 2])
    print(head)
    print(remove_nth_from_end(head, 1))
