#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019-04-02 22:56
# @Author  : hlliu
import re
from collections import Counter

with open('test.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    words = re.findall(r'\w+', text.lower())
    count = Counter(words)

print(count.most_common(3))
