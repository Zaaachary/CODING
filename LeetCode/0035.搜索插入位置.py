"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。
"""
import pdb
from typing import List

class Solution:
    '''
    二分查找，目标为找到第一个大于等于 target 的位置
    执行用时： 28 ms , 在所有 Python3 提交中击败了 97.60% 的用户 内存消耗： 15.7 MB , 在所有 Python3 提交中击败了 5.52% 的用户
    '''
    def searchInsert(self, nums: List[int], target: int) -> int:
        result = len(nums)
        left, right = 0, result -1
        while left <= right:
            mid = (right - left) // 2 + left
            # print(left, mid, right)
            # import pdb; pdb.set_trace()
            temp = nums[mid]
            if temp >= target:
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result



class Solution_2:
    '''
    二分查找，发现存在值就返回，否则结束后根据 left 和 right 给出插入位置
    执行用时： 32 ms , 在所有 Python3 提交中击败了 90.31% 的用户 内存消耗： 15.7 MB , 在所有 Python3 提交中击败了 5.04% 的用户 通过测试用例： 64 / 64
    '''
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (right - left) // 2 + left
            # find target in nums
            temp = nums[mid]
            if temp == target:
                return mid
            elif temp > target:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # insert
            if left > mid:
                return mid + 1
            elif right < mid:
                return mid


class Solution_1:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 36ms 91.22%
        for index, num in enumerate(nums):
            if num < target:
                continue
            elif num > target:
                nums.insert(index, target)
                return index
            else:
                return index
        else:
            # 位置在最尾部
            nums.append(target)
            return len(nums)-1



if __name__ == "__main__":
    test = [1,3,5,6]
    target = 6

    S = Solution()
    print(test)
    index = S.searchInsert(test, target)
    print(index)
    test.insert(index, target)
    print(test)
