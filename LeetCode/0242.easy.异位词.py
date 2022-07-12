# -*- encoding: utf-8 -*-
'''
@File    :   0242.easy.异位词.py
@Time    :   2022/07/12 17:27:00
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   https://leetcode.cn/problems/valid-anagram/
'''
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        ch_list = [0] * 26
        for ch in s:
            ch_list[ord(ch) - 97] += 1
        
        for ch in t:
            temp = ord(ch) - 97
            ch_list[temp] -= 1
            if ch_list[temp] < 0:
                return False
        
        return True
        
