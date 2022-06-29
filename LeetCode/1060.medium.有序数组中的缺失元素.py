# -*- encoding: utf-8 -*-
'''
@File    :   1060.medium.有序数组中的缺失元素.py
@Time    :   2022/06/29 10:27:20
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   

现有一个按 升序 排列的整数数组 nums ，其中每个数字都 互不相同 。

给你一个整数 k ，请你找出并返回从数组最左边开始的第 k 个缺失数字。

'''


class Solution:
    '''
    执行用时： 32 ms , 在所有 Python3 提交中击败了 99.20% 的用户 内存消耗： 19.2 MB , 在所有 Python3 提交中击败了 96.80% 的用户
    '''
    def missingElement(self, nums: List[int], k: int) -> int:
        left, right = 0, len(nums) - 1
        first = nums[0]
        target_idx = -1
        # 目标：寻找第k个缺失数字前一个不缺失的数字
        while left <= right:
            mid = (right - left) // 2 + left
            temp = nums[mid]
            current_k = temp - first - mid + 1    # 当前数字后一个缺失的数字是第current_k个
            if current_k <= k:
                target_idx = mid
                left = mid + 1
            else:
                right = mid - 1

        current_k = nums[target_idx] - first - target_idx + 1
        result = nums[target_idx] + 1 + k - current_k
            
        return result
            