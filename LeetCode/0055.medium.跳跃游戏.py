# -*- encoding: utf-8 -*-
'''
@File    :   0055.medium.跳跃游戏.py
@Time    :   2022/06/26 13:39:14
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

判断你是否能够到达最后一个位置。
'''

class Solution_reference:
    '''
    执行用时： 92 ms , 在所有 Python3 提交中击败了 71.37% 的用户 内存消耗： 16 MB , 在所有 Python3 提交中击败了 15.71% 的用户
    '''
    def canJump(self, nums: List[int]) -> bool:
        n, rightmost = len(nums), 0
        for i in range(n):
            if i <= rightmost:
                rightmost = max(rightmost, i + nums[i])
                if rightmost >= n - 1:
                    return True
        return False


class Solution_220626:
    '''
    执行用时： 136 ms , 在所有 Python3 提交中击败了 16.50% 的用户 内存消耗： 15.9 MB , 在所有 Python3 提交中击败了 43.03% 的用户
    '''
    def canJump(self, nums: List[int]) -> bool:
        max_idx = 0
        current_idx = 0
        while current_idx <= max_idx and current_idx < len(nums):
            max_idx = max(max_idx, current_idx + nums[current_idx])
            current_idx += 1

        if current_idx == len(nums):
            return True
        else:
            return False

class Solution_20:
    '''
    out of time
    '''
    def canJump(self, nums: list) -> bool:
        # DFS 超时
        self.visited = [False] * len(nums)
        self.nums = nums
        return self.DFS(0)
        
    def DFS(self, start):
        self.visited[start] = True
        if start == len(self.nums) - 1:
            return True
        Neighbor = [start + i for i in range(1, self.nums[start] + 1) if 0 <= start + i < len(self.nums)]
        Neighbor.extend([start - i for i in range(1, self.nums[start] + 1) if 0 <= start - i < len(self.nums)])
        for nb in Neighbor:
            if not self.visited[nb]:
                if self.DFS(nb):
                    return True
        else:
            self.visited[start] = False
            return False