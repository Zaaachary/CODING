class Solution:
    '''
    回溯遍历法  超时
    '''
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.result = 0
        self.back_tracing(0, nums, target, 0)
        return self.result

    def back_tracing(self, idx, nums, target, current_sum):
        if idx == len(nums) and current_sum == target:
            self.result += 1
        elif idx < len(nums):
            self.back_tracing(idx + 1, nums, target, current_sum - nums[idx])
            self.back_tracing(idx + 1, nums, target, current_sum + nums[idx])
            
