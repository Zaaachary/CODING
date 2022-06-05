# -*- encoding: utf-8 -*-
'''
@File    :   0004. 寻找两个正序数组的中位数.py
@Time    :   2022/06/02 20:59:21
@Author  :   Zhifeng Li
@Contact :   zaaachary_li@163.com
@Desc    :   
给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。

算法的时间复杂度应该为 O(log (m+n)) 。 难点

'''
from typing import List

class Solution:
    '''
    二分查找的思想，每次排除 一定的元素 O(log(m+n))
    '''
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        def find_kth_element(k):
            index_1, index_2 = 0, 0
            while True:
                if index_1 == m:
                    return nums2[index_2 + k - 1]
                elif index_2 == n:
                    return nums1[index_1 + k - 1]
                if k == 1:
                    return min(nums1[index_1], nums2[index_2])

                new_index_1 = min(m-1, index_1 + k//2 - 1)
                new_index_2 = min(n-1, index_2 + k//2 - 1)

                if nums1[new_index_1] < nums2[new_index_2]:
                    k -= new_index_1 - index_1 + 1
                    index_1 = new_index_1 + 1
                else:
                    k -= new_index_2 - index_2 + 1
                    index_2 = new_index_2 + 1

        m, n = len(nums1), len(nums2)
        k, flag = divmod(m + n, 2)
        if flag:
            return find_kth_element(k+1)
        else:
            return (find_kth_element(k) + find_kth_element(k+1)) / 2

class Solution_1:
    '''
    基础解法，寻找第 k 小的数字
    O((m+n)/2)
    执行用时： 44 ms , 在所有 Python3 提交中击败了 82.75% 的用户 内存消耗： 15 MB , 在所有 Python3 提交中击败了 95.67% 的用户
    '''
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 暴力解，归并排序，过程中维护 mid 和 mid -1 最后根据flag判断返回
        m, n = len(nums1), len(nums2)

        mid, mod_flag = divmod(m + n, 2)    # flag 1 mid  flag 0 [mid] + [mid-1] /2
        prev_val, cur_val, current_index = 0, 0, 0
        i1, i2 = 0, 0

        while current_index <= mid and i1 < m and i2 < n:
            # print(prev_val, current_index)
            prev_val = cur_val
            current_index += 1
            if nums1[i1] < nums2[i2]:
                cur_val = nums1[i1]
                i1 += 1
            else:
                cur_val = nums2[i2]
                i2 += 1

        while current_index <= mid:
            current_index += 1
            if i1 == m:
                prev_val = cur_val
                cur_val = nums2[i2]
                i2 += 1
            elif i2 == n:
                prev_val = cur_val
                cur_val = nums1[i1]
                i1 += 1
        
        if mod_flag:
            return cur_val
        else:
            return (cur_val + prev_val) / 2 

if __name__ == "__main__":
    S = Solution()
    print(S.findMedianSortedArrays([1,3,5,7], [2, 4]))
        