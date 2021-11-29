# -*- encoding: utf-8 -*-
'''
@File    :   HeapSort.py
@Time    :   2021/11/28 18:23:31
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   堆排序，力扣215

heapq 
https://docs.python.org/zh-cn/3/library/heapq.html?highlight=heapq#module-heapq

heapq.heappush(heap, item)
heapq.heappop(heap)
heapq.heapify(x)    # list 原地转堆
'''
from typing import List
import heapq

def heapsort(nums):
    """利用 heapq 中的堆进行堆排序"""
    h = []
    for item in nums:
        heapq.heappush(h, item)
    return [heapq.heappop(h) for _ in range(len(h))]

def heap_sort_k(nums: List, k):
    import heapq
    heap = [-num for num in nums]
    heapq.heapify(heap)
    for i in range(k):
        result = heapq.heappop(heap)
    return -result



if __name__ == "__main__":
    import random
        
    nums = [random.randint(0,20) for _ in range(20)]
    print(f'origin nums: {nums}')
    sorted_nums = heapsort(nums)
    print(f'sorted nums: {sorted_nums}')
