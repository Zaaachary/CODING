"""
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
"""
from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums)-1
        for index, value in enumerate(nums):
            nums[index] = value ** 2

        result = [0] * len(nums)
        index = len(result) - 1
        while left < right:
            if nums[left] > nums[right]:
                result[index] = nums[left]
                left += 1
            else:
                result[index] = nums[right]
                right -= 1
            index -= 1
        return result

if __name__ == "__main__":
    S = Solution()
    print(S.sortedSquares([0,3,10]))


