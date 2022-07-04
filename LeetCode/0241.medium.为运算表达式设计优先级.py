# -*- encoding: utf-8 -*-
'''
@File    :   0241.medium.为运算表达式设计优先级.py
@Time    :   2022/07/01 16:45:16
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
'''

from functools import cache

class Solution:
    '''
    记忆化搜索
    执行用时： 36 ms , 在所有 Python3 提交中击败了 85.06% 的用户 内存消耗： 15.3 MB , 在所有 Python3 提交中击败了 5.45% 的用户
    '''
    def diffWaysToCompute(self, expression: str) -> List[int]:
        nums = []
        operators = []
        temp_num = 0
        for idx, ch in enumerate(expression):
            if ch in ('*', '+', '-'):
                operators.append(ch)
                nums.append(temp_num)
                temp_num = 0
            else:
                temp_num = temp_num * 10 + int(ch)
        else:
            nums.append(temp_num)
        
        @cache
        def DFS(left: int, right: int):
            if left == right:
                return [nums[left]]
            else:
                result = []
                for idx in range(left, right):
                    # 分割点
                    left_nums = DFS(left, idx)
                    right_nums = DFS(idx + 1, right)
                    for l_num in left_nums:
                        for r_num in right_nums:
                            op = operators[idx]
                            if op == "*":
                                result.append(l_num * r_num)
                            elif op == '-':
                                result.append(l_num - r_num)
                            else:
                                result.append(l_num + r_num)
                return result

        print(operators, nums)
        return DFS(0, len(nums) - 1)


class Solution:
    @cache
    def diffWaysToCompute(self, input: str) -> List[int]:
        # 如果只有数字，直接返回
        if input.isdigit():
            return [int(input)]

        res = []
        for i, char in enumerate(input):
            if char in ['+', '-', '*']:
                # 1.分解：遇到运算符，计算左右两侧的结果集
                # 2.解决：diffWaysToCompute 递归函数求出子问题的解
                left = self.diffWaysToCompute(input[:i])
                right = self.diffWaysToCompute(input[i+1:])
                # 3.合并：根据运算符合并子问题的解
                for l in left:
                    for r in right:
                        if char == '+':
                            res.append(l + r)
                        elif char == '-':
                            res.append(l - r)
                        else:
                            res.append(l * r)

        return res
