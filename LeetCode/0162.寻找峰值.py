# -*- encoding: utf-8 -*-
'''
@File    :   0162.寻找峰值.py
@Time    :   2022/06/13 14:38:21
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   

峰值元素是指其值严格大于左右相邻值的元素。
给你一个整数数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。
你可以假设 nums[-1] = nums[n] = -∞ 。
你必须实现时间复杂度为 O(log n) 的算法来解决此问题。

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
对于所有有效的 i 都有 nums[i] != nums[i + 1]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/find-peak-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

class Solution:
    """
    执行用时： 32 ms , 在所有 Python3 提交中击败了 90.52% 的用户 内存消耗： 15.1 MB , 在所有 Python3 提交中击败了 41.95% 的用户
    """
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        def get(index):
            if index == -1 or index == n:
                return float('-inf')
            else:
                return nums[index]
        
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            temp = get(mid)
            if get(mid - 1) < temp > get(mid + 1):
                return mid
            elif temp < get(mid + 1):
                left = mid + 1
            else:
                right = mid - 1
        
            