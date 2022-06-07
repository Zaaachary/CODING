# -*- encoding: utf-8 -*-
'''
@File    :   0033.搜索旋转排序数组.py
@Time    :   2022/06/07 11:04:35
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   前后局部有序的数组

整数数组 nums 按升序排列，数组中的值 互不相同 。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,5,6,7] 在下标 3 处经旋转后可能变为 [4,5,6,7,0,1,2] 。

给你 旋转后 的数组 nums 和一个整数 target ，如果 nums 中存在这个目标值 target ，则返回它的下标，否则返回 -1 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/search-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
import pdb
from typing import List


class Solution:
    '''
    执行用时： 36 ms , 在所有 Python3 提交中击败了 73.29% 的用户 内存消耗： 15.2 MB , 在所有 Python3 提交中击败了 57.19% 的用户 通过测试用例： 195 / 195
    '''
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (right - left) // 2 + left
            temp = nums[mid]
            if temp == target:
                return mid
            elif nums[0] <= temp:    # mid 左侧皆小于 temp
                if nums[0] <= target < temp:
                    right = mid - 1
                else:
                    left = mid + 1
            else:   # mid 左侧存在轮转分界点
                if temp < target <= nums[-1]: 
                    left = mid + 1
                else:
                    right = mid - 1
        return -1
 


class Solution_1:
    '''
    O(n) 方法 遍历
    执行用时： 40 ms , 在所有 Python3 提交中击败了 45.42% 的用户 内存消耗： 15.2 MB , 在所有 Python3 提交中击败了 42.60% 的用户
    '''
    def search(self, nums: List[int], target: int) -> int:

        for index, num in enumerate(nums):
            if num == target:
                return index
        else:
            return -1
        
if __name__ == "__main__":
    S = Solution()
    print(S.search([1,3,5], 1))