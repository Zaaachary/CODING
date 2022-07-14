# -*- encoding: utf-8 -*-
'''
@File    :   0455.easy.分发饼干.py
@Time    :   2022/07/14 12:46:53
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   https://leetcode.cn/problems/assign-cookies/
'''


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        '''
        执行用时： 52 ms , 在所有 Python3 提交中击败了 86.19% 的用户 内存消耗： 16.4 MB , 在所有 Python3 提交中击败了 72.60% 的用户
        '''
        s.sort(reverse=True)
        g.sort(reverse=True)
        result = 0
        j = 0
        for i in range(len(g)):
            if j >= len(s):
                break
    
            if g[i] <= s[j]:
                j += 1
                result += 1
            

        return result