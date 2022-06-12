# -*- encoding: utf-8 -*-
'''
@File    :   JZOF.53.I.在排序数组中查找数字i.py
@Time    :   2022/06/12 22:27:45
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   同34题
'''
from typing  import List

class Solution_better:
    '''
    执行用时： 32 ms , 在所有 Python3 提交中击败了 91.90% 的用户 内存消耗： 16.2 MB , 在所有 Python3 提交中击败了 33.04% 的用户
    '''
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        self.nums = nums
        start = self.binarysearch(target, True) # 大于等于 target 的第一个数
        end = self.binarysearch(target, False) # 大于 target 的第一个数
        return end - start


    def binarysearch(self, target, lower=True):
        left, right = 0, len(self.nums) - 1
        result = len(self.nums)
        while left <= right:
            mid = (right - left) // 2 + left
            temp = self.nums[mid]
            if temp > target:
                # 大于 target 的第一个数
                right = mid - 1
                result = mid
            elif lower and temp >= target:
                # lower 大于等于 target 的第一个数
                right = mid - 1
                result = mid
            else:
                left = mid + 1
        return result

class Solution:
    '''
    执行用时： 32 ms , 在所有 Python3 提交中击败了 91.90% 的用户 内存消耗： 16.2 MB , 在所有 Python3 提交中击败了 33.04% 的用户
    '''
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return 0

        self.nums = nums
        start = self.binarysearch(target, True) # 大于等于 target 的第一个数
        end = self.binarysearch(target, False) # 大于 target 的第一个数
        return end - start


    def binarysearch(self, target, lower=True):
        left, right = 0, len(self.nums) - 1
        result = len(self.nums)
        while left <= right:
            mid = (right - left) // 2 + left
            temp = self.nums[mid]
            if lower:
                # 大于等于 target 的第一个数
                if temp >= target:
                    right = mid - 1
                    result = mid
                elif temp < target:
                    left = mid + 1
            else:
                # 大于 target 的第一个数
                if temp > target:
                    right = mid - 1
                    result = mid
                else:
                    left = mid + 1
        return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    target = 1

    S = Solution()
    print(S.search(nums, target))