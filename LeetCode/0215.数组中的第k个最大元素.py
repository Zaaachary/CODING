#
# @lc app=leetcode.cn id=215 lang=python3
#
# [215] 数组中的第K个最大元素
#

# @lc code=start
import heapq
from typing import List
class Solution_heap:
    # 86.27%
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]
        heapq.heapify(heap)
        for i in range(k):
            result = heapq.heappop(heap)
        return -result


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        self.nums = nums
        self.quick_sort_find_k(0, len(nums)-1, k)
        return self.nums[len(nums) - k]
        
    def quick_sort_find_k(self, start, end, k):
        if start >= end:
            return
        
        left, right = start, end
        povit = self.nums[left]    # 选取枢轴
        while left < right:
            # 右指针寻找小于povit的位置
            while left < right and self.nums[right] >= povit:
                right -= 1
            # 左指针寻找大于povit的位置
            while left < right and self.nums[left] <= povit:
                left += 1
            # 交换
            if left < right:
                self.nums[left], self.nums[right] = self.nums[right], self.nums[left]

        # 枢轴到合适位置
        self.nums[start] = self.nums[left]
        self.nums[left] = povit

        # 继续对左右部分进行快排（找第k大/小可在此更改）
        if left == len(self.nums) - k :
            # 当前已定位到第k大的数
            return 
        elif left > len(self.nums) - k:
            # k 大的数在左侧
            self.quick_sort_find_k(start, left-1, k)
        else:
            # k 大的数在右侧
            self.quick_sort_find_k(left+1, end, k)
    

if __name__ == "__main__":
    import random
    # nums = [random.randint(0,20) for _ in range(10)]
    nums = [3,2,1,5,6,4]
    print(nums)
    S = Solution()
    print(S.findKthLargest(nums, 2))
    print(nums)
# @lc code=end