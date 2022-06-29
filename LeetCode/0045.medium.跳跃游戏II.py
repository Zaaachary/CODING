# -*- encoding: utf-8 -*-
'''
@File    :   0045.medium.跳跃游戏II.py
@Time    :   2022/06/26 16:14:05
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
'''
from typing import List


class Solution_greed:
    '''
    贪心算法，和dp同理，但是不需要矩阵
    '''
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        maxPos, end, step = 0, 0, 0
        for i in range(n - 1):
            if maxPos >= i:
                maxPos = max(maxPos, i + nums[i])
                if i == end:
                    end = maxPos
                    step += 1
        return step


class Solution_dp_v2:
    '''
    dp v2 删除部分操作 执行用时： 56 ms , 在所有 Python3 提交中击败了 51.33% 的用户 内存消耗： 15.9 MB , 在所有 Python3 提交中击败了 26.67% 的用户
    '''
    def jump(self, nums: List[int]) -> int:
        dp = [i for i in range(len(nums))]
        max_idx = 0

        for idx in range(len(nums)):
            temp = idx + nums[idx]
            if max_idx < temp:
                for jdx in range(max_idx, temp+1):
                    if jdx < len(nums):
                        dp[jdx] = min(dp[idx]+1, dp[jdx])
                    else:
                        break
                max_idx = temp

        return dp[-1]


class Solution_dp_v1:
    '''
    dp v1 超时
    '''
    def jump(self, nums: List[int]) -> int:
        dp = [i for i in range(len(nums))]
        max_idx = 0

        for idx in range(len(nums)):
            max_idx = max(max_idx, idx + nums[idx])
            
            for jdx in range(idx+1, max_idx+1):
                if jdx < len(nums):
                    dp[jdx] = min(dp[idx]+1, dp[jdx])
                else:
                    break

        return dp[-1]

if __name__ == "__main__":
    S = Solution()
    print(S.jump([2,3,1,1,4]))
