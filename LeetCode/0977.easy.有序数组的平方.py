"""
给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。
"""
from typing import List

class Solution:
    """
    找到分界点后归并
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


class Solution_slow:
    '''
    96ms  20%
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


