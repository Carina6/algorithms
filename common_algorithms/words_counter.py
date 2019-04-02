#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-02 22:56
# @Author  : hlliu
import re
from collections import Counter

words = re.findall(r'\w+', open('test.txt').read().lower())

print(Counter(words).most_common(3))
