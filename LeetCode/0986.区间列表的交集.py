# -*- encoding: utf-8 -*-
'''
@File    :   0986.区间列表的交集.py
@Time    :   2022/06/16 16:06:03
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   
给定两个由一些 闭区间 组成的列表，firstList 和 secondList ，其中 firstList[i] = [starti, endi] 而 secondList[j] = [startj, endj] 。每个区间列表都是成对 不相交 的，并且 已经排序 。

返回这 两个区间列表的交集 。

形式上，闭区间 [a, b]（其中 a <= b）表示实数 x 的集合，而 a <= x <= b 。

两个闭区间的 交集 是一组实数，要么为空集，要么为闭区间。例如，[1, 3] 和 [2, 4] 的交集为 [2, 3] 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/interval-list-intersections
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

输入：firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
输出：[[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]
'''

from typing import List

class Solution:
    '''
    执行用时： 40 ms , 在所有 Python3 提交中击败了 97.94% 的用户 内存消耗： 15.7 MB , 在所有 Python3 提交中击败了 36.06% 的用户
    '''
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        
        result = []
        index_1 = index_2 = 0
        while index_1 < len(firstList) and index_2 < len(secondList):
            idx_1, idx_2 = firstList[index_1], secondList[index_2]
            # import pdb; pdb.set_trace()
            
            if idx_1[1] < idx_2[0]:
                index_1 += 1
            elif idx_1[0] <= idx_2[1] and idx_1[1] >= idx_2[0]:
                # 有交集
                result.append([max(idx_1[0],idx_2[0]), min(idx_1[1], idx_2[1])])
                if idx_1[1] > idx_2[1]:
                    index_2 += 1
                else:
                    index_1 += 1
            else:
                index_2 += 1

        return result

if __name__ == "__main__":
    S = Solution()
    first = [[5, 10],[11, 15]]
    second = [[16, 20]]
    print(S.intervalIntersection(first, second))