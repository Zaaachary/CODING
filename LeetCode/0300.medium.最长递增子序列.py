# -*- encoding: utf-8 -*-
'''
@File    :   0300.medium.最长递增子序列.py
@Time    :   2022/07/06 15:49:55
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
给你一个整数数组 nums ，找到其中最长严格递增子序列的长度。

子序列 是由数组派生而来的序列，删除（或不删除）数组中的元素而不改变其余元素的顺序。例如，[3,6,2,7] 是数组 [0,3,1,6,2,2,7] 的子序列。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
'''
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [] # 定义 dp[i] 为考虑前 i 个元素，以第 i 个数字结尾的最长上升子序列的长度
        for i in range(len(nums)):
            dp.append(1)
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

class Solution_gready:
    def lengthOfLIS(self, nums: List[int]) -> int:
        d = []
        for n in nums:
            if not d or n > d[-1]:
                d.append(n)
            else:
                l, r = 0, len(d) - 1
                loc = r
                while l <= r:
                    mid = (l + r) // 2
                    if d[mid] >= n:
                        loc = mid
                        r = mid - 1
                    else:
                        l = mid + 1
                d[loc] = n
        return len(d)



class Solution_wrong:
    '''
    1 2 4 3  idx < idx - 1, idx > idx - 2
    1 2 4 1  idx < idx - 1,, idx < idx - 2
    此时最大为 idx - 1 的值
    1 2 3 4  idx > idx - 1 > idx - 2
    3 4 1 2  idx > idx - 1, idx < idx - 2
    寻找递增子序列的最后一个节点，如果大于它则 + 1
    '''
    def lengthOfLIS(self, nums: List[int]) -> int:
        print(nums)
        dp = [1] * len (nums)       # 定义 \textit{dp}[i]dp[i] 为考虑前 ii 个元素，以第 ii 个数字结尾的最长上升子序列的长度
        
        for idx in range(1, len(nums)):
            if nums[idx] <= nums[idx - 1]:
                dp[idx] = dp[idx - 1]
            elif dp[idx - 1] == 1:    # idx > idx - 1
                dp[idx] = 2
            else:
                # 寻找等于 dp[idx-1]的第一个节点
                temp = self.binarySearch(dp, 0, idx, dp[idx-1])
                if nums[temp] < nums[idx]:
                    dp[idx] = dp[idx - 1] + 1
                else:
                    dp[idx] = dp[idx - 1]
            print(dp)
        return dp[-1]

    def binarySearch(self, dp, left, right, target):
        # 寻找等于 target 的第一个节点
        result = -1
        while left <= right:
            mid = left + (right - left) // 2
            temp = dp[mid]
            if temp >= target:  # 不存在大于
                result = mid
                right = mid - 1
            else:
                left = mid + 1
        return result

if __name__ == "__main__":
    S = Solution()
    print(S.lengthOfLIS([0,1,0,3,2,3]))