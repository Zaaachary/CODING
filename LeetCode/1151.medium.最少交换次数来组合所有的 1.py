# -*- encoding: utf-8 -*-
'''
@File    :   1151.medium.最少交换次数来组合所有的 1.py
@Time    :   2022/07/14 17:27:11
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   https://leetcode.cn/problems/minimum-swaps-to-group-all-1s-together/

2134. 最少交换次数来组合所有的 1 II similar
'''

class Solution:
    '''
    执行用时： 140 ms , 在所有 Python3 提交中击败了 77.40% 的用户 内存消耗： 19.1 MB , 在所有 Python3 提交中击败了 13.01% 的用户
    '''
    def minSwaps(self, data: List[int]) -> int:
        one_num = sum(data)
        if not one_num:
            return 0
            
        max_one = 0
        current_one = sum(data[:one_num-1])
        left, right = 0, one_num - 1

        while right < len(data):
            current_one += data[right]
            max_one = max(max_one, current_one)
            current_one -= data[left]
            left += 1
            right += 1

        return one_num - max_one