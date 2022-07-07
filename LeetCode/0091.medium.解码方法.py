# -*- encoding: utf-8 -*-
'''
@File    :   0091.medium.解码方法.py
@Time    :   2022/07/05 17:28:44
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
'''

class Solution:
    '''
    执行用时： 36 ms , 在所有 Python3 提交中击败了 78.33% 的用户 内存消耗： 14.9 MB , 在所有 Python3 提交中击败了 65.63% 的用户
    '''
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0

        dp = [0] * len(s)   # 序列的0~idx部分有多少种解码方式
        dp[0] = 1

        for idx in range(1, len(s)):
            # print(dp)
            if s[idx] != '0':
                # idx 位置的s是否可以独立
                temp = dp[idx-1]
            else:
                temp = 0
            
            if s[idx-1] != '0' and 1 <= int(s[idx-1] + s[idx]) <= 26:
                # idx 位置 s 可以和 idx-1 组合
                if idx - 2 >= 0:
                    temp += dp[idx-2]
                else:
                    temp += 1

            dp[idx] = temp

        return dp[-1]