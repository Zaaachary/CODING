"""
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
"""
from typing import List

class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        nums = [value ** 2 for value in nums]
        nums.sort()
        return nums


class Solution_1:
    """
    找到 负数0分界点后从中间先两侧归并
    """
    def sortedSquares(self, nums: List[int]) -> List[int]:
        length = len(nums)
        negative = -1
        for index, num in enumerate(nums):
            if num < 0:
                negative = index
            else:
                break

        result = list()
        left, right = negative, negative + 1
        while left >= 0 or right < length:
            if left < 0:
                result.append(nums[right] ** 2)
                right += 1
            elif right == length:
                result.append(nums[left] ** 2)
                left -= 1
            elif nums[left] ** 2 < nums[right] ** 2:
                result.append(nums[left] ** 2)
                left -= 1
            else:
                result.append(nums[right] ** 2)
                right += 1

        return result


class Solution_0:
    '''
    平方后从左右两部分向中间归并 better
    执行用时： 68 ms , 在所有 Python3 提交中击败了 62.45% 的用户 内存消耗： 16.4 MB , 在所有 Python3 提交中击败了 90.91% 的用户
    '''
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for index, num in enumerate(nums):
            nums[index] = num ** 2

        result = [0] * len(nums)
        left, right = 0, len(nums)-1
        index = len(result) - 1
        while left <= right:
            if nums[left] > nums[right]:
                result[index] = nums[left]
                left += 1
            else:
                result[index] = nums[right]
                right -= 1
            index -= 1
            
        return result

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        return sorted(num * num for num in nums)


if __name__ == "__main__":
    S = Solution()
    print(S.sortedSquares([-4,-1,0,3,10]))


