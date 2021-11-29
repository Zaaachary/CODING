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

class heap(list):
    """自定义的堆类型，继承自列表，小顶堆。"""
    def __init__(self, *args) -> None:
        super().__init__(*args)
        self.insert(0, len(self))    # 从 1 开始存储，0 标记节点数

    def heapify(self):
        """建堆，自下向上调整"""
        index = (self[0]) // 2 # 最后一个有孩子的节点索引        
        for i in range(index, 0, -1):
            if self[2*i] < self[i]:
                self.swap(2*i, i)
            if 2*i + 1 < self.__len__() and self[2*i+1] < self[i]:
                self.swap(2*i+1, i)
    
    def heappop(self):
        """pop 最小节点，向下调整，每次都和最小的孩子交换"""
        if self[0] == 0:
            return None
        result = self[1]
        self[0] -= 1
        if self[0] == 0:
            return result

        self[1] = self.pop()    # 将最后一个元素放于堆顶
        i = 1
        while 2*i < self.__len__(): # 当 i 有孩子
            j = 2*i # 待交换的孩子
            if j+1 < self.__len__():
                j = j+1 if self[j+1] < self[j] else j
            
            if self[i] > self[j]:
                self.swap(i, j)
            else:
                break # 左右孩子皆比当前 self[i]大，完成调整
        return result

    def heappush(self, x):
        # 简单粗暴法，实际应该是仅对增加进来的节点进行向上调整
        self[0] += 1
        self.append(x)
        self.heapify()

    def swap(self, i, j):
        self[i], self[j] = self[j], self[i]

if __name__ == "__main__":
    import random

    # TODO debug  [6, 19, 14, 1, 0, 3, 18, 2, 16, 5]
    h = heap([random.randint(0,20) for _ in range(10)])
    # h = heap([7, 9, 11, 3, 0])
    print(f'origin nums: {h[1:]}')
    h.heapify()
    print(f'heapified nums: {h[1:]}')
    h.heappush(3)
    print(f'push 3, nums: {h[1:]}')
    # import pdb; pdb.set_trace()
    
    nums = [h.heappop() for _ in range(h[0])]
    print(f'hand write heap sort: {nums}')
    
    # nums = [random.randint(0,20) for _ in range(20)]
    # print(f'origin nums: {nums}')
    # sorted_nums = heapsort(nums)
    # print(f'sorted nums: {sorted_nums}')
