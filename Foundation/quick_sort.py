# -*- encoding: utf-8 -*-
'''
@File    :   QuickSort.py
@Time    :   2021/11/28 14:49:52
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   快速排序
'''
from typing import List


def quick_sort(nums: List[int], start=None, end=None):
    # quick_sort(nums)
    start = 0 if start is None else start
    end = len(nums)-1 if end is None else end
        
    if start < end:
        partition_index = partition(nums, start, end)
        # 可以在此处决定快排的方向
        quick_sort(nums, start, partition_index-1)
        quick_sort(nums, partition_index+1, end)

    return nums

def partition(nums, start, end):
    if start > end:
        return start

    # 选取枢轴 pivot，通过交换使得 左边不大于/右边不小于 枢轴值
    pivot = nums[start]
    
    left, right = start, end
    while left < right:
        # 找到右侧小于枢轴的位置和左侧大于枢轴的位置，进行交换
        while left < right and nums[right] >= pivot:
            right -= 1
        while left < right and nums[left] <= pivot:
            left += 1
        if left < right:
            nums[right], nums[left] = nums[left], nums[right]
    
    # 此时 [povit, item1, item2, ..., item_start, ...]
    
    nums[start] = nums[left]
    nums[left] = pivot

    return left


if __name__ == "__main__":
    import random
    nums = [random.randint(0,20) for _ in range(20)]
    # nums = [3, 16, 13, 7, 8]
    print(f'origin nums: {nums}')
    quick_sort(nums)
    print(f'sorted nums: {nums}')

    
