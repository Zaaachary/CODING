# -*- encoding: utf-8 -*-
'''
@File    :   0034.在排序数组中查找元素的第一个和最后一个位置.py
@Time    :   2022/06/07 09:54:33
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   

给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

进阶：

你可以设计并实现时间复杂度为 O(log n) 的算法解决此问题吗？

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

class Solution:
    '''
    两次二分查找，一次寻找开始，一次寻找结束，使用开关+ bs
    执行用时： 36 ms , 在所有 Python3 提交中击败了 76.94% 的用户 内存消耗： 16 MB , 在所有 Python3 提交中击败了 67.72% 的用户
    '''
    def binarysearch(self, lower:bool):
        ans = len(self.nums)
        left, right = 0, ans - 1
        while left <= right:
            mid = (right - left) // 2 + left
            temp = self.nums[mid]
            if temp > self.target:
                # upper mode, find the first num bigger than target
                right = mid - 1
                ans = mid
            elif lower and self.nums[mid] >= self.target:
                # lower mode, find the first target num
                right = mid - 1
                ans = mid
            else:
                left = mid + 1

        return ans

    def searchRange(self, nums: List[int], target: int) -> List[int]:
        self.nums = nums
        self.target = target
        
        start = self.binarysearch(True)
        end = self.binarysearch(False) - 1

        if start <= end and end < len(nums):
            return start, end
        else:
            return -1, -1

class Solution_0:
    '''
    两次二分查找，一次寻找开始，一次寻找结束
    执行用时： 36 ms , 在所有 Python3 提交中击败了 76.94% 的用户 内存消耗： 16 MB , 在所有 Python3 提交中击败了 67.72% 的用户
    '''
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        start, end = len(nums) , -1
        left, right = 0, len(nums) - 1

        # find right
        while left <= right:
            mid = (right - left) // 2 + left
            temp = nums[mid]
            if temp > target:
                right = mid -1
            elif temp < target:
                left = mid + 1
            else:
                end = max(end, mid)
                left = mid + 1

        left, right = 0, len(nums) - 1
        # find start
        while left <= right:
            mid = (right - left) // 2 + left
            temp = nums[mid]
            if temp > target:
                right = mid - 1
            elif temp == target:
                start = min(start, mid)
                right = mid - 1
            elif temp < target:
                left = mid + 1

        if start == len(nums):
            start = -1
        return start, end



if __name__ == "__main__":
    S = Solution()
    print(S.searchRange(nums = [5,7,7,8,8,10], target=8))
    # print(S.searchRange(nums = [0, 0], target=))