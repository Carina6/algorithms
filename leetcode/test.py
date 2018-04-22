#!/usr/bin/env python
# -*- coding: utf-8 -*-
from models.binary_tree import BinaryTree


def test_a():
    bt = BinaryTree()

    for x in [1,2,2,3,3,None,None,4,4]:
        bt.addNode(x)

    print(bt)