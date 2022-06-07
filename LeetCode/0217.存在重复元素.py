# -*- encoding: utf-8 -*-
'''
@File    :   0217.存在重复元素.cpp
@Time    :   2022/05/22 17:47:04
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
给你一个整数数组 nums 。如果任一值在数组中出现 至少两次 ，返回 true ；如果数组中每个元素互不相同，返回 false 。
 

示例 1：

输入：nums = [1,2,3,1]
输出：true
示例 2：

输入：nums = [1,2,3,4]
输出：false
示例 3：

输入：nums = [1,1,1,3,3,4,3,2,4,2]
输出：true
'''

class Solution:
    '''
    执行用时： 52 ms , 在所有 Python3 提交中击败了 89.88% 的用户 内存消耗： 25.6 MB , 在所有 Python3 提交中击败了 47.70% 的用户
    '''
    def containsDuplicate(self, nums: List[int]) -> bool:
        count_set = set()
        for num in nums:
            if num in count_set:
                return True
            else:
                count_set.add(num)
        return False
            
