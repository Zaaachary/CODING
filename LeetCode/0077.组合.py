# -*- encoding: utf-8 -*-
'''
@File    :   0077.组合.py
@Time    :   2022/02/20 15:16:03
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   组合

给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

你可以按 任何顺序 返回答案。
待看：
https://leetcode-cn.com/problems/combinations/solution/hui-su-suan-fa-jian-zhi-python-dai-ma-java-dai-ma-/

'''
from typing import List

class Solution:
    '''
    52ms  68.17%
    '''
    def combine(self, n: int, k: int) -> List[List[int]]:
        # import pdb; pdb.set_trace()
        start, end = 1, n
        result_list = Solution.combine_part(start, end, k)
        return result_list
    
    @staticmethod
    def combine_part(start, end, k):
        '''
        遍历当前层的序列(start -> end-k+1), 值与内层序列组合列表拼接并返回。
        '''
        result_list = []
        while start <= end - k + 1:
            if k - 1 >= 1:
                son_list = Solution.combine_part(start+1, end, k-1)
                for son in son_list:
                    son.insert(0, start)
                    result_list.append(son)
            else:
                result_list.append([start])
            start += 1
        return result_list


        
        
        
            
        


from itertools import combinations

class Solution_python:
    '''
    itertools   40ms 90.64%
    '''
    def combine(self, n: int, k: int) -> List[List[int]]:
        from itertools import combinations
        return combinations(range(1,n+1), k)

        
if __name__ == "__main__":

    S = Solution()
    print(S.combine(4, 2))