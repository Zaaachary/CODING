# -*- encoding: utf-8 -*-
'''
@File    :   0384.medium.打乱数组.py
@Time    :   2022/06/26 21:16:33
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   

给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。打乱后，数组的所有排列应该是 等可能 的。

实现 Solution class:

Solution(int[] nums) 使用整数数组 nums 初始化对象
int[] reset() 重设数组到它的初始状态并返回
int[] shuffle() 返回数组随机打乱后的结果
 



来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/shuffle-an-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''

import random

class Solution:
    '''
    python 标准库实现
    执行用时： 104 ms , 在所有 Python3 提交中击败了 93.36% 的用户 内存消耗： 18.8 MB , 在所有 Python3 提交中击败了 70.48% 的用户
    '''

    def __init__(self, nums: List[int]):
        self.origin = nums[:]
        self.random_list = nums[:]

    def reset(self) -> List[int]:
        self.random_list = self.origin[:]
        return self.random_list

    def shuffle(self) -> List[int]:
        random.shuffle(self.random_list)
        return self.random_list

class Solution:
    '''       
    作者：LeetCode-Solution
    链接：https://leetcode.cn/problems/shuffle-an-array/solution/da-luan-shu-zu-by-leetcode-solution-og5u/
    来源：力扣（LeetCode）
    著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
    '''
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.original = nums.copy()

    def reset(self) -> List[int]:
        self.nums = self.original.copy()
        return self.nums

    def shuffle(self) -> List[int]:
        shuffled = [0] * len(self.nums)
        for i in range(len(self.nums)):
            j = random.randrange(len(self.nums))
            shuffled[i] = self.nums.pop(j)
        self.nums = shuffled
        return self.nums
