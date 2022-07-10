# -*- encoding: utf-8 -*-
'''
@File    :   0416.medium.分割等和子集.py
@Time    :   2022/07/09 20:13:12
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   https://leetcode.cn/problems/partition-equal-subset-sum/
给你一个 只包含正整数 的 非空 数组 nums 。请你判断是否可以将这个数组分割成两个子集，使得两个子集的元素和相等。
'''
from typing import List

class Solution_dp_v1:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        dp 执行用时： 3784 ms , 在所有 Python3 提交中击败了 5.91% 的用户 内存消耗： 44.7 MB , 在所有 Python3 提交中击败了 7.06% 的用户
        '''
        if len(nums) <= 1:
            return False
        bag_size, mod = divmod(sum(nums), 2)
        if mod:
            return False
        dp = [[0] * (bag_size + 1) for _ in range(len(nums))]
        for i in range(nums[0], bag_size + 1):
            dp[0][i] = nums[0]
        # print(dp)
        for i in range(len(nums)):
            for j in range(bag_size + 1):
                if nums[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    # max(不放当前, 放当前+剩余空间最大)
                    dp[i][j] = max(dp[i-1][j], nums[i] + dp[i-1][j-nums[i]])
                # print(dp)

        return True if dp[-1][-1] == bag_size else False

class Solution_rolling_dp_v1:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        执行用时： 3028 ms , 在所有 Python3 提交中击败了 13.59% 的用户 内存消耗： 15.3 MB , 在所有 Python3 提交中击败了 56.13% 的用户
        '''
        if len(nums) <= 1:
            return False
        bag_size, mod = divmod(sum(nums), 2)
        if mod:
            return False
        dp = [0] * (bag_size + 1)

        for i in range(len(nums)):
            for j in range(bag_size, -1, -1):
                if nums[i] <= j:
                    # max(不放当前, 放当前+剩余空间最大)
                    dp[j] = max(dp[j], nums[i] + dp[j-nums[i]])

        return True if dp[-1] == bag_size else False

class Solution_dp_v2:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        执行用时： 2340 ms , 在所有 Python3 提交中击败了 42.20% 的用户 内存消耗： 30.4 MB , 在所有 Python3 提交中击败了 19.85% 的用户
        '''
        if len(nums) <= 1:
            return False
        bag_size, mod = divmod(sum(nums), 2)
        if mod:
            return False
        dp = [[True] + [False] * (bag_size) for _ in range(len(nums))]
        if nums[0] <= bag_size:
           dp[0][nums[0]] = True

        # print(dp)
        for i in range(1, len(nums)):
            for j in range(bag_size + 1):
                if nums[i] == j:
                    dp[i][j] = True
                elif nums[i] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-nums[i]] | dp[i-1][j]
                # print(dp)

        return dp[-1][-1]

class Solution_rolling_dp_v1:
    def canPartition(self, nums: List[int]) -> bool:
        '''
        执行用时： 1668 ms , 在所有 Python3 提交中击败了 64.80% 的用户 内存消耗： 15.1 MB , 在所有 Python3 提交中击败了 77.92% 的用户
        '''
        if len(nums) <= 1:
            return False
        bag_size, mod = divmod(sum(nums), 2)
        if mod:
            return False
        # dp = [[True] + [False] * bag_size for _ in range(len(nums))]
        dp = [True] + [False] * bag_size
        if nums[0] <= bag_size:
           dp[nums[0]] = True

        for i in range(1, len(nums)):
            for j in range(bag_size, -1, -1):
                if nums[i] == j:
                    dp[j] = True
                elif nums[i] > j:
                    dp[j] = dp[j]
                else:
                    dp[j] = dp[j-nums[i]] | dp[j]

        return dp[-1]