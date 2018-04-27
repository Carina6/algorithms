#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 10. Regular Expression Matching
def test_regular_express_match():

    '''
    思路：
    时间复杂度：
    '''
    def is_match(s, p):
        sl = len(s)
        pl = len(p)
        if sl == 0 or pl == 0:
            return False

        # s开头加上空格字符，p开头加上空格字符，以s为行，p为列，构建动态规划数组dp
        dp = [[False for x in range(pl+1)] for y in range(sl+1)]
        dp[0][0] = True

        for i in range(pl):
            if p[i] == '*' and p[i-1]:
                dp[0][i+1] = dp[0][i-1]
            elif p[i] == '.':
                dp[0][i+1] = dp[0][i]

        for i in range(sl):
            for j in range(pl):
                if p[j] in [s[i], '.']:
                    dp[i+1][j+1] = dp[i][j]
                elif p[j] == '*':
                    if p[j-1] not in [s[i], '.']:
                        dp[i+1][j+1] = dp[i+1][j-1]
                    else:
                        dp[i+1][j+1] = dp[i+1][j-1] or dp[i][j+1] or dp[i+1][j]

        return dp[sl][pl]

    print()
    print(is_match('', '.*'))
