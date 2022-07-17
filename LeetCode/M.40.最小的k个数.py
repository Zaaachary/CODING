# -*- encoding: utf-8 -*-
'''
@File    :   M.40.最小的k个数.py
@Time    :   2022/07/17 20:57:04
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   https://leetcode.cn/problems/zui-xiao-de-kge-shu-lcof/
'''
from typing import List
import heapq

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []

        heap = [-x for x in arr[:k]]
        heapq.heapify(heap)
        for idx in range(k, len(arr)):
            if -heap[0] > arr[idx]:
                heapq.heappush(heap, -arr[idx])
                heapq.heappop(heap)
        
        return [-x for x in heap]
