# -*- encoding: utf-8 -*-
'''
@File    :   0042.hard.接雨水.py
@Time    :   2022/07/17 20:38:04
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   https://leetcode.cn/problems/trapping-rain-water/
'''

class Solution:
    '''
    两个 dp 数组，分别统计 dp[i] 当前节点左侧和右侧最大的高度 （不含当前节点）
    执行用时： 84 ms , 在所有 Python3 提交中击败了 15.11% 的用户 内存消耗： 16.4 MB , 在所有 Python3 提交中击败了 49.14% 的用户
    '''
    def trap(self, height: List[int]) -> int:
        # if len(height) <= 2:
            # return 0

        dp_left = [0] * len(height)
        dp_right = [0] * len(height)
        
        for i in range(1, len(height)):
            dp_left[i] = max(dp_left[i-1], height[i-1])
        
        for i in range(len(height)-2, -1, -1):
            dp_right[i] = max(dp_right[i+1], height[i+1])
        
        result = 0
        for i in range(1, len(height)-1):
            min_height = min(dp_left[i], dp_right[i])
            if min_height > height[i]:
                result += min_height - height[i]
        
        return result


class Solution_2:
    '''
    两个 dp 数组，分别统计 dp[i] 当前节点左侧和右侧最大的高度 （含当前节点）
    '''
    def trap(self, height: List[int]) -> int:

        dp_left = [height[0]] + [0] * (len(height)-1)
        dp_right = [0] * (len(height)- 1) + [height[-1]]
        
        for i in range(1, len(height)):
            dp_left[i] = max(dp_left[i-1], height[i])
        
        for i in range(len(height)-2, -1, -1):
            dp_right[i] = max(dp_right[i+1], height[i])
        
        result = 0
        for i in range(1, len(height)-1):
            min_height = min(dp_left[i], dp_right[i]) - height[i]
            result += min_height
        
        return result