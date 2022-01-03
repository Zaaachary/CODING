# -*- encoding: utf-8 -*-
'''
@File    :   0189.轮转数组.py
@Time    :   2021/12/30 11:14:43
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   
给你一个数组，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。
输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/rotate-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

class Solution:
    """
    环状替换   TODO
    """
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_copy = nums[:]
        for index, num in enumerate(nums_copy):
            insert_idx = (index + k) % len(nums)
            nums[insert_idx] = nums_copy[index]
        


class Solution_1:
    """
    60ms 21.33% 20.7MB
    使用额外的数组存储
    时间 O(n)  空间O(n)
    """
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums_copy = nums[:]
        for index, num in enumerate(nums_copy):
            insert_idx = (index + k) % len(nums)
            nums[insert_idx] = nums_copy[index]

class Solution_2:
    """
    数组翻转
    时间 O(n)  空间O(1)
    """
    def rotate(self, nums: List[int], k: int) -> None:
        move = k % len(nums)    # 明确要 move 的实际长度
        nums.reverse()
        
        # python 特性
        # nums[move:] = reversed(nums[move:])
        # nums[:move] = reversed(nums[:move])

        # 左右指针 挨个调换
        left, right = move, len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left +=1
            right -= 1

        left, right = 0, move-1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left +=1
            right -= 1


if __name__ == "__main__":
    S = Solution()
    l = [1,2,3]
    S.rotate(l, 2)
    print(l)