# -*- encoding: utf-8 -*-
'''
@File    :   0017.medium.电话号码的字母组合.py
@Time    :   2022/06/24 21:10:14
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
给定一个仅包含数字 2-9 的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/letter-combinations-of-a-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

class Solution:
    '''
    执行用时： 28 ms , 在所有 Python3 提交中击败了 97.31% 的用户 内存消耗： 15.2 MB , 在所有 Python3 提交中击败了 10.32% 的用户
    '''
    def letterCombinations(self, digits: str) -> List[str]:
        self.result = []
        self.current_str = []
        self.num_dict = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno','7':'pqrs', '8':'tuv', '9':'wxyz' }
        if len(digits) > 0:
            self.back_tracing(digits, 0)
        return self.result

    def back_tracing(self, digits, begin):
        if begin == len(digits):
            self.result.append(''.join(self.current_str))
        else:
            choices = self.num_dict[digits[begin]]
            for choice in choices:
                self.current_str.append(choice)
                self.back_tracing(digits, begin+1)
                self.current_str.pop()

if __name__ == "__main__":
    S = Solution()
    print(S.letterCombinations("23"))