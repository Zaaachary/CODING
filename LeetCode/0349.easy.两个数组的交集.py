# -*- encoding: utf-8 -*-
'''
@File    :   0349.easy.两个数组的交集.py
@Time    :   2022/07/13 20:32:08
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   https://leetcode.cn/problems/intersection-of-two-arrays/
'''

class Solution:
    '''
    执行用时： 36 ms , 在所有 Python3 提交中击败了 80.54% 的用户 内存消耗： 15.1 MB , 在所有 Python3 提交中击败了 21.41% 的用户
    '''
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        nums1_set = set(nums1)
        for num in nums2:
            if num in nums1_set:
                result.append(num)
                nums1_set.remove(num)
        return result