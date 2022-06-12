# -*- encoding: utf-8 -*-
'''
@File    :   0015.medium.三数之和.py
@Time    :   2022/06/09 23:16:37
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   

给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []

        self.nums = nums
        self.current_triple = []
        self.result = set()

        for i in range(0, len(nums)):
            self.DFS(i)
        return list(self.result)

    def DFS(self, index):

        self.current_triple.append(self.nums[index])
        if len(self.current_triple) == 3:
            if sum(self.current_triple) == 0:
                self.result.add(tuple(sorted(self.current_triple)))
        else:
            for i in range(index+1, len(self.nums)):
                self.DFS(i)

        self.current_triple.pop()


if __name__ == "__main__":
    S = Solution()
    print(S.threeSum([3,0,-2,-1,1,2]))