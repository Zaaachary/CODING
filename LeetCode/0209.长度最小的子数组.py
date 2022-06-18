"""
给定一个含有 n 个正整数的数组和一个正整数 s ，
找出该数组中满足其和 ≥ s 的长度最小的 连续 子数组，并返回其长度。
如果不存在符合条件的子数组，返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/minimum-size-subarray-sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

class Solution:
    '''
    执行用时： 40 ms , 在所有 Python3 提交中击败了 91.96% 的用户 内存消耗： 16.8 MB , 在所有 Python3 提交中击败了 60.46% 的用户
    '''
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = len(nums) + 1
        
        left, current_sum = 0, 0
        for right, cur_num in enumerate(nums):
            current_sum += cur_num
            while current_sum >= target:
                # print(left, right)
                min_len = min(min_len, right-left+1)
                current_sum -= nums[left]
                left += 1

        if min_len == len(nums) + 1:
            return 0
        else:
            return min_len
        
    
    def minSubArrayLen2(self, s:int, nums:List[int]) -> int:
        # 解析  无需判断len(nums)>1  56ms
        slow=0
        min_len=float('inf')
        nsum=0
        
        for fast in range(len(nums)):
            nsum+=nums[fast]
            
            while nsum>=s:
                min_len = min(min_len,fast-slow+1)
                nsum -= nums[slow]
                slow+=1
        
        return min_len if min_len!=float('inf') else 0



if __name__ == "__main__":
    # nums, s = [1,1], 3
    # nums, s = [1,2,3,4,5], 15
    nums, s = [2,3,1,2,4,3], 7
    S = Solution()
    print(S.minSubArrayLen(s, nums))
