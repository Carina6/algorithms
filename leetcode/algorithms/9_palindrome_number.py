#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 9. Palindrome Number
def test_palindrome_number():
    '''
    思路：判断是否是回文字符串，从两边往中间比较
    时间复杂度：O(n) 304 ms
    '''
    def is_palindrome(x):
        s = str(x)
        l = len(s)
        if l < 1:
            return False
        i, j = 0, l-1
        while i <= j:
            if s[i] == s[j]:
                i += 1
                j -= 1
            else:
                return False
        return True

    '''
    思路：将数字翻转后与原数子比较是否相同
    此方法在其他语言中（Java，C++等）会造成数字溢出，Python中对大整数做了特殊处理，不会溢出
    Python2的int溢出时，可以自动转换成long(long是一个理论上可以存储无限大数的数据类型)
    Python3中统一用int代替long
    时间复杂度：O(n) 292 ms
    '''
    def is_palindrome2(x):
        if x < 0 or (x != 0 and x % 10 == 0):
            return False
        temp = x
        res = 0
        while temp:
            tail = temp % 10
            # 溢出可能在此处发生
            res = res*10 + tail
            temp = temp // 10
        return res == x

    '''
    思路：将数字x的后半部分翻转后rev与原数字的前半部分x比较是否相同
    时间复杂度：O(n) 292 ms
    '''
    def is_palindrome3(x):
        if x < 0 or (x != 0 and x % 10 == 0):
            return False

        rev = 0
        while x > rev:
            tail = x % 10
            rev = rev*10 + tail
            x = x // 10

        # 如果x为奇数，则rev会比前半部分多一位，则使用rev//10来减少一位
        return x == rev or x == rev // 10

    '''
    思路：将数字x的后半部分翻转后rev与原数字的前半部分x比较是否相同
    时间复杂度：O(n) 292 ms
    '''
    def is_palindrome4(x):
        return str(x)[::-1] == str(x)
        # return repr(x)[::-1] == repr(x)

    print(9223372036854775799)
    print(is_palindrome4(-121))
