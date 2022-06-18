# -*- encoding: utf-8 -*-
'''
@File    :   0713.乘积小于 K 的子数组.py
@Time    :   2022/06/16 19:20:10
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   
给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。
'''
from typing import List
from bisect import bisect_right
from math import log


class Solution:
    '''
    滑窗
    执行用时： 140 ms , 在所有 Python3 提交中击败了 83.45% 的用户 内存消耗： 17.2 MB , 在所有 Python3 提交中击败了 21.97% 的用户
    '''
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        left, current_prod, result = 0, 1, 0
        for right, num in enumerate(nums):
            current_prod *= num
            while left <= right and current_prod >= k:
                current_prod //= nums[left]
                left += 1
            result += right - left + 1
        
        return result
            

class Solution_logbis:
    '''
    二分查找; 引入对数  O(nlogn)
    执行用时： 256 ms , 在所有 Python3 提交中击败了 14.17% 的用户 内存消耗： 17.5 MB , 在所有 Python3 提交中击败了 5.82% 的用户
    '''
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0
        ans, n = 0, len(nums)
        logPrefix = [0] * (n + 1)
        for i, num in enumerate(nums):
            logPrefix[i + 1] = logPrefix[i] + log(num)
        logK = log(k)
        for j in range(1, n + 1):
            l = bisect_right(logPrefix, logPrefix[j] - logK + 1e-10, 0, j)
            ans += j - l
        return ans

class Solution_timeout:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k == 0:
            return 0

        result = 0
        n = len(nums)
        for left in range(n):
            current_dot = nums[left]
            if current_dot >= k:
                continue
            else:
                result += 1
                right = left + 1
                while right < n:
                    current_dot *= nums[right]
                    if current_dot < k:
                        result += 1
                    right += 1
                
        return result

if __name__ == "__main__":
    S = Solution()
    print(S.numSubarrayProductLessThanK([10,5,2,6], 100))