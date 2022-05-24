# -*- encoding: utf-8 -*-
'''
@File    :   0198.打家劫舍.py
@Time    :   2022/05/23 11:11:26
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   

你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。

给定一个代表每个房屋存放金额的非负整数数组，计算你 不触动警报装置的情况下 ，一夜之内能够偷窃到的最高金额。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/house-robber
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

class Solution:
    '''
    执行用时： 28 ms , 在所有 Python3 提交中击败了 97.63% 的用户 内存消耗： 14.8 MB , 在所有 Python3 提交中击败了 87.80% 的用户
    '''
    def rob(self, nums: List[int]) -> int:
        if len(nums) <= 2:  # nums bigger than 1
            return max(nums)
        r1, r2  = nums[:2]
        for value in nums[2:]:
            if r1 + value >= r2:
                r1, r2 = max(r1, r2), r1 + value
            else:
                r1 = r2
        
        return r2


if __name__ == "__main__":
    S = Solution()
    print(S.rob([2,1,1,2]))