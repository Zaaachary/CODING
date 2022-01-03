"""
给定一个数组nums，
编写一个函数将所有0移动到数组的末尾，
同时保持非零元素的相对顺序

https://leetcode-cn.com/problems/move-zeroes/
"""
from typing import List

class Solution:
    """
    Solution_2 的优雅写法，占用情况相当。
    """
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        left = right = 0
        while right < n:
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
            right += 1

class Solution_2:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        一个蠢蠢的算法，左指针找0，右指针从左指针+已遇到0的个数开始找非0，找到后交换。直到左指针右侧没有0
        64 ms, 在所有 Python3 提交中击败了30.86%的用户
        move one item everytime; space O(1)
        Do not return anything, modify nums in-place instead.
        [1, 2, 0, 4, 5, 6]
        """
        zero_ptr = 0    # items on the left of this ptr are non-zero
        zero_count = 0
        while zero_ptr < len(nums) :
            # find zero item
            while zero_ptr < len(nums) and nums[zero_ptr] != 0:
                zero_ptr += 1
            # find non-zero item behind the zero_ptr
            nonzero_ptr = zero_ptr + 1 + zero_count
            while nonzero_ptr < len(nums) and nums[nonzero_ptr] == 0:
                nonzero_ptr += 1
            
            if nonzero_ptr >= len(nums) or zero_ptr >= len(nums):
                break
            else:
                zero_count = nonzero_ptr - zero_ptr -1
                nums[zero_ptr], nums[nonzero_ptr] = nums[nonzero_ptr], 0         

class Solution_1:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            # nums有0或1个元素 或 没有0元素 返回
            return None

        count_zeros, index = 0, 0
        while index < len(nums):
            # 数0的个数并删除中间出现的0
            if nums[index] == 0:
                del nums[index]
                count_zeros += 1
            else:
                index += 1
        
        for _ in range(count_zeros):
            nums.append(0)
            

if __name__ == "__main__":
    nums = [0,1,0,3,12, -100,0]
    # nums = [0, 1]
    print(nums)
    s = Solution()
    s.moveZeroes(nums)
    print(nums)