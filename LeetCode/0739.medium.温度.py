# -*- encoding: utf-8 -*-
'''
@File    :   0739.medium.温度.py
@Time    :   2022/07/12 14:46:06
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   https://leetcode.cn/problems/daily-temperatures/
'''
from typing import List

class Solution_for:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        '''
        暴力法，嵌套 for 循环 （超时
        '''
        result = [0] * len(temperatures)
        for idx in range(len(temperatures)):
            for j in range(idx+1, len(temperatures)):
                if temperatures[j] > temperatures[idx]:
                    result[idx] = j - idx
                    break
            else:
                result[idx] = 0
        
        return result



class Solution_vl2:
    '''
    执行用时： 2216 ms , 在所有 Python3 提交中击败了 5.01% 的用户 内存消耗： 21.7 MB , 在所有 Python3 提交中击败了 73.44% 的用户
    '''
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans, nxt, big = [0] * n, dict(), 10**9
        for i in range(n - 1, -1, -1):
            # 所有温度中大于当前温度且位置最小的索引
            warmer_index = min(nxt.get(t, big) for t in range(temperatures[i] + 1, 102))
            if warmer_index != big:
                ans[i] = warmer_index - i
            nxt[temperatures[i]] = i
        return ans


class Solution_stack:
    '''
    单调栈，栈中存放未找到比自己还大的温度的索引，每次都观察栈顶，为比当前小的元素赋result
    执行用时： 188 ms , 在所有 Python3 提交中击败了 83.37% 的用户 内存消耗： 21.9 MB , 在所有 Python3 提交中击败了 42.51% 的用户
    '''
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []  # 存放未找到比自己还大的温度的索引
        result = [0] * len(temperatures) 
        for idx, temp in enumerate(temperatures):
            print(stack)
            while stack:
                temp_idx = stack[-1]
                if temperatures[temp_idx] < temp:
                    result[temp_idx] = idx - temp_idx
                    stack.pop()
                else:
                    break
            stack.append(idx)

        return result

if __name__ == "__main__":
    S = Solution_stack()
    print(S.dailyTemperatures([73,74,75,71,69,72,76,73]))