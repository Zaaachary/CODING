# -*- encoding: utf-8 -*-
'''
@File    :   JZOF.05.easy.替换空格.py
@Time    :   2022/06/08 22:01:18
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   请实现一个函数，把字符串 s 中的每个空格替换成"%20"。


'''

class Solution:
    def replaceSpace(self, s: str) -> str:
        tes = ''
        for i in s:
            if i == ' ':
                tes += '%20'
            else:
                tes += i
        return tes
