#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 38. Count and Say
def test_count_and_say():
    '''
    思路：
    时间复杂度：
    '''

    def method1(n):
        pre, curr = [1], []

        for i in range(1, n):
            start = pre[0]
            count = 1
            for j in range(1, len(pre)):
                if pre[j] == start:
                    count += 1
                else:
                    curr.append(count)
                    curr.append(start)
                    start = pre[j]
                    count = 1
            curr.append(count)
            curr.append(start)
            pre, curr = curr, []

        return ''.join(map(str, pre))

    print()
    print(method1(6))
