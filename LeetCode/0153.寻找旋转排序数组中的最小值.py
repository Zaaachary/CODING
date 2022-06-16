# -*- encoding: utf-8 -*-
'''
@File    :   0153.寻找旋转排序数组中的最小值.py
@Time    :   2022/06/13 13:55:20
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   
已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。

给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/find-minimum-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

class Solution_better:
    def findMin(self, nums: List[int]) -> int:    
        low, high = 0, len(nums) - 1
        while low < high:
            pivot = low + (high - low) // 2
            if nums[pivot] < nums[high]:
                # mid 右侧单调增
                high = pivot - 1
            else:
                low = pivot + 1
        return nums[low]


class Solution:
    '''
    执行用时： 36 ms , 在所有 Python3 提交中击败了 71.44% 的用户 内存消耗： 15.1 MB , 在所有 Python3 提交中击败了 63.43% 的用户
    '''
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        min_nums = nums[-1]
        while left <= right:
            mid = (right - left) // 2 + left
            temp = nums[mid]
            if nums[left] <= temp:
                # mid左侧单调不减
                min_nums = min(min_nums, nums[left])
                left = mid + 1
            else:
                # mid 左侧有断点  e.g. 7 8 9 0 1 2
                min_nums = min(min_nums, temp)
                right = mid - 1

        return min_nums



if __name__ == "__main__":
    S = Solution()
    nums = [0, 1, 2, 3, 4]
    # nums = [7,8,9,0,1,2,3,4,5,6]
    print(S.findMin(nums))