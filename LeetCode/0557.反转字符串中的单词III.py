# -*- encoding: utf-8 -*-
'''
@File    :   0557.反转字符串中的单词III.py
@Time    :   2022/01/04 10:04:03
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
'''

class Solution:
    def reverseWords(self, s: str) -> str:
        s_list = s.split(' ')
        for index, string in enumerate(s_list):
            s_list[index] = ''.join(list(reversed(string)))
        return ' '.join(s_list)

class Solution_1:
    ''''''
    def reverseWords(self, s: str) -> str:
        str_list = list(s)
        left = 0
        for index, value in enumerate(str_list):
            if value == ' ':
                # left -> start of a word; right -> end of a word
                right = index - 1
                while left < right:
                    str_list[left], str_list[right] = str_list[right], str_list[left]
                    left += 1
                    right -= 1
                left = index + 1
        
        right = len(s) - 1
        while left < right:
            str_list[left], str_list[right] = str_list[right], str_list[left]
            left += 1
            right -= 1

        return ''.join(str_list)
                
