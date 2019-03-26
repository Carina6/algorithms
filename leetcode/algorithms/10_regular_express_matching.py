#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 10. Regular Expression Matching
def test_regular_express_match():

    '''
    思路：构建动态规划二位数组dp
    dp[i][j]：s 前i位字符 和 p前j位字符 是否匹配
    说明：
    1.p[j]=s[i] or p[j]='.' : dp[i][j]= dp[i-1][j-1]
    2.p[j]='*' :
        2.1 p[j-1]=s[i] or p[j-1]='.' : dp[i][j]=dp[i][j-1] or dp[i-1][j] or dp[i][j-2]
        2.2 其他 ： dp[i][j]=dp[i][j-2]
    时间复杂度：O(m*n)
    '''
    def is_match(s, p):
        sl = len(s)
        pl = len(p)

        # s开头加上空格字符，p开头加上空格字符，以s为行，p为列，构建动态规划数组dp
        dp = [[False for x in range(pl+1)] for y in range(sl+1)]
        dp[0][0] = True

        # 第一行赋值
        for i in range(pl):
            if p[i] == '*' and p[i-1]:
                dp[0][i+1] = dp[0][i-1]

        #
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
    print(is_match('a', '.*..a'))
