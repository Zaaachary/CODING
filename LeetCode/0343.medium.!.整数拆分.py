# -*- encoding: utf-8 -*-
'''
@File    :   0343.medium.整数拆分.py
@Time    :   2022/07/08 20:53:55
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
https://leetcode.cn/problems/integer-break/
'''

class Solution:
    def integerBreak(self, n: int) -> int:
        '''
        执行用时： 40 ms , 在所有 Python3 提交中击败了 68.93% 的用户 内存消耗： 14.9 MB , 在所有 Python3 提交中击败了 40.36% 的用户
        dp[num] 数字 num 的拆分后的最大乘积
        dp[2] = 1
        dp[3] = 1 * 2 = 2
        dp[4] = 2 * 2 = 4
        dp[5] = 2 * 3 = 6
        dp[6] = 3 * 3 = 9
        dp[7] = 3 * 4 = 12 == 2*dp[5] == 3*dp[4] == 4*dp[3] 
        max(分成两个数字的结果，分成超过两个数字的结果)
        dp[n] = max([j * (i-j) for j in range(1, i)] + [j * dp[i-j] for j in range(1, i)])
        '''
        if n <= 1:
            return -1
        dp = [0] * (n+1)
        dp[0] = dp[1] = -1
        for i in range(2, n+1):
            # 法1
            # for j in range(i):
                # dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
            # 法1 变体
            dp[i] = max([j * (i-j) for j in range(1, i)] + [j * dp[i-j] for j in range(1, i)])

        return dp[-1]

class Solution_optimized:
    def integerBreak(self, n: int) -> int:
        '''
        执行用时： 32 ms , 在所有 Python3 提交中击败了 95.87% 的用户 内存消耗： 15 MB , 在所有 Python3 提交中击败了 15.54% 的用户
        dp[num] 数字 num 的拆分后的最大乘积
        dp[n] = max([j * (i-j) for j in range(1, i)] + [j * dp[i-j] for j in range(1, i)])
        只需要考虑拆分成 2和3 即可
        '''
        if n <= 1:
            return -1
        dp = [0] * (n+1)
        dp[2] = 1
        for i in range(3, n+1):
            dp[i] = max(2*(i-2), 2*dp[i-2], 3*(i-3), 3*dp[i-3])

        return dp[-1]



if __name__ == "__main__":
    S = Solution()
    # for target in range(0, 10):
        # print(target)
    S.integerBreak(58)
        