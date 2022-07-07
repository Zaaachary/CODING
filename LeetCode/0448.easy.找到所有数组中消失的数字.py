# -*- encoding: utf-8 -*-
'''
@File    :   0448.medium.找到所有数组中消失的数字.py
@Time    :   2022/07/05 21:40:40
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
'''
class Solution:
    '''
    执行用时： 136 ms , 在所有 Python3 提交中击败了 5.63% 的用户 内存消耗： 21.5 MB , 在所有 Python3 提交中击败了 44.80% 的用户
    '''
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # 原地交换  nums[idx] == idx + 1
        ptr = 0
        while ptr <= len(nums) - 1:
            temp = nums[ptr]
            while temp != ptr + 1:
                if nums[temp - 1] != temp:
                    nums[ptr], nums[temp - 1] = nums[temp - 1], temp
                    temp = nums[ptr]
                else:
                    break
            ptr += 1
        
        result = []
        for i in range(len(nums)):
            if nums[i] != i + 1:
                result.append(i + 1)

        return result
