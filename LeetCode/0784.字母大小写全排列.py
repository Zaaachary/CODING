# -*- encoding: utf-8 -*-
'''
@File    :   0784.字母大小写全排列.py
@Time    :   2022/06/05 22:10:42
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   
给定一个字符串 s ，通过将字符串 s 中的每个字母转变大小写，我们可以获得一个新的字符串。

返回 所有可能得到的字符串集合 。以 任意顺序 返回输出。
'''
from typing import List

class Solution:
    """
    深度优先遍历 + 回溯
    执行用时： 44 ms , 在所有 Python3 提交中击败了 81.02% 的用户 内存消耗： 15.7 MB , 在所有 Python3 提交中击败了 80.30% 的用户
    """
    def letterCasePermutation(self, s: str) -> List[str]:
        self.s = s
        self.total_result = []
        self.current_list = []
        if len(s) != 0:
            self.DFS(0)
        return self.total_result    

    def DFS(self, index):
        print(self.current_list)
        current_ch = self.s[index]
        if current_ch.isalpha():
            self.current_list.append(current_ch.lower())
            if len(self.current_list) == len(self.s):
                self.total_result.append(''.join(self.current_list))
            else:
                self.DFS(index+1)
            self.current_list.pop()
            self.current_list.append(current_ch.upper())
            if len(self.current_list) == len(self.s):
                self.total_result.append(''.join(self.current_list))
            else:
                self.DFS(index+1)

        else:
            self.current_list.append(current_ch)
            if len(self.current_list) == len(self.s):
                self.total_result.append(''.join(self.current_list))
            else:
                self.DFS(index+1)
        
        self.current_list.pop()

if __name__ == "__main__":
    S = Solution()
    print(S.letterCasePermutation('a1'))