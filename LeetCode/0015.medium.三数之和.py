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
# from itertools import product

class Solution:
    '''
    排序+双指针，O(n2) 通过使得 num1 < num2 < num3 的方式确保不重复，从而避免使用set比较
    执行用时： 484 ms , 在所有 Python3 提交中击败了 90.68% 的用户 内存消耗： 17.7 MB , 在所有 Python3 提交中击败了 96.56% 的用户
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        first_index = 0
        prev_num = None
        while first_index < n - 2:
            current_num = nums[first_index]
            if current_num != prev_num:
                target_sum = -current_num
                left = first_index + 1
                right = n - 1
                while left < right:
                    temp = nums[left] + nums[right]
                    if temp == target_sum:
                        current_second = nums[left]
                        result.append([nums[first_index], current_second, nums[right]])
                        left += 1
                        while left <= right and nums[left] == current_second:
                            left += 1
                    elif temp > target_sum:
                        right -= 1
                    else:
                        left += 1
                prev_num = current_num
            first_index += 1
        return result


class Solution_pass:
    '''
    排序后，转化成两数之和的做法   排序+双指针  weakness 使用set去重
    执行用时： 3420 ms , 在所有 Python3 提交中击败了 10.21% 的用户 内存消耗： 17.2 MB , 在所有 Python3 提交中击败了 99.26% 的用户
    '''
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = set()
        for first_index in range(0, n - 2):
            target_sum = - nums[first_index]
            left = first_index + 1
            right = n - 1
            while left < right:
                temp = nums[left] + nums[right]
                if temp == target_sum:
                    result.add(tuple(sorted([nums[first_index], nums[left], nums[right]])))
                    left += 1
                elif temp > target_sum:
                    right -= 1
                else:
                    left += 1
        return list(result)
            
            


class Solution_1:
    '''
    DFS 枚举
    '''
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