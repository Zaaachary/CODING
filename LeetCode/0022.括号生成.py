# -*- encoding: utf-8 -*-
'''
@File    :   0022.括号生成.py
@Time    :   2022/06/25 11:34:48
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
'''
from typing import List
class Solution:
    '''
    执行用时： 36 ms , 在所有 Python3 提交中击败了 82.01% 的用户 内存消耗： 15.3 MB , 在所有 Python3 提交中击败了 10.01% 的用户
    '''
    def generateParenthesis(self, n: int) -> List[str]:
        self.current = []
        self.result = []
        self.right = 0
        self.back_tracing(False, n)
        return self.result

    def back_tracing(self, right_bracket, n):
        if self.right == n:
            self.result.append(''.join(self.current))
        else:
            if right_bracket:
                self.current.append(')')
                self.right += 1
            else:
                self.current.append('(')
            if self.right < len(self.current) - self.right:
                self.back_tracing(True, n)
            if len(self.current) - self.right < n:
                self.back_tracing(False, n)
            if self.right == n:
                self.result.append(''.join(self.current))

            self.current.pop()
            self.right = self.right - 1 if right_bracket else self.right

class Solution_better:
    '''
    执行用时： 32 ms , 在所有 Python3 提交中击败了 93.96% 的用户 内存消耗： 15.2 MB , 在所有 Python3 提交中击败了 36.99% 的用户
    '''
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return
            if left < n:
                S.append('(')
                backtrack(S, left+1, right)
                S.pop()
            if right < left:
                S.append(')')
                backtrack(S, left, right+1)
                S.pop()

        backtrack([], 0, 0)
        return ans

if __name__ == "__main__":
    S = Solution()
    print(S.generateParenthesis(3))