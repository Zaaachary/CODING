"""
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

"""
#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
from typing import List


class Solution:
    '''
    更标准的回溯写法
    20220705   执行用时： 40 ms , 在所有 Python3 提交中击败了 60.60% 的用户 内存消耗： 15.1 MB , 在所有 Python3 提交中击败了 65.42% 的用户
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        
        self.result = []
        self.path = []
        self.visited = [False] * len(nums)

        self.backtracing(nums, 0)

        return self.result

    def backtracing(self, nums, place_idx):
        if place_idx == len(nums):
            self.result.append(self.path)
        else:
            for i in range(len(nums)):
                if not self.visited[i]:
                    self.path.append(nums[i])
                    self.visited[i] = True
                    self.backtracing(nums, place_idx + 1)
                    self.visited[i] = False
                    self.path.pop()


class Solution_0222:
    '''
    20220222 DFS   36ms  64.71%
    '''
    def permute(self, nums: List[int]) -> List[List[int]]:
        visited = [False for _ in range(len(nums))]
        permute_result = []

        current_path = []
        def DFS(index):
            visited[index] = True
            current_path.append(nums[index])

            if len(current_path) == len(nums):
                permute_result.append(current_path[:])
            else:
                for neighbor in range(len(nums)):
                    if not visited[neighbor]:
                        DFS(neighbor)
            visited[index] = False
            current_path.pop()

        for index in range(len(nums)):
            DFS(index)

        return permute_result


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 36ms 94.06
        from itertools import permutations
        ans = [list(x) for x in permutations(nums, len(nums))]
        return ans

    def permute2(self, nums):
        # 44ms 63.79% 深度优先遍历
        visited = [False] * len(nums)
        ans = []
        path = []

        def DFS(current):
            path.append(nums[current])
            visited[current] = True

            if len(path) == len(nums):
                # 已经完成了一个排列
                ans.append(path[::])
            else:
                for index in range(len(nums)):
                    if not visited[index]:
                        DFS(index)

            path.pop()
            visited[current] = False

        for index in range(len(nums)):
            DFS(index)
        return ans

    def permute3(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        res = []

        def backtrack(first=0):
            # 所有数都填完了
            if first == n:
                res.append(nums[:])
            for i in range(first, n):
                nums[first], nums[i] = nums[i], nums[first]
                # 继续递归填下一个数
                backtrack(first + 1)
                # 撤销操作
                nums[first], nums[i] = nums[i], nums[first]

        backtrack()
        return res
# @lc code=end


if __name__ == "__main__":
    S = Solution()
    nums = [1, 2, 3]
    print(S.permute3(nums))
