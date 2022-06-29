/*
@File    :   0045.medium.跳跃游戏II.cpp
@Time    :   2022/06/26 15:52:04
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
给你一个非负整数数组 nums ，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

假设你总是可以到达数组的最后一个位置。

*/
#include <vector>
#include <iostream>
using namespace std;

class Solution {
public:
    int jump(vector<int>& nums) {
        vector<int> dp(nums.size());
        for (int i = 0; i < dp.size(); i++)
            dp[i] = i;

        int max_idx = 0;

        for (int idx = 0; idx < nums.size(); idx ++){
            int temp = idx + nums[idx];
            if (max_idx < temp){
                for (int jdx = max_idx; jdx < temp +1; jdx++ ){
                    if (jdx < nums.size())
                        dp[jdx] = dp[jdx] > dp[idx] + 1 ? dp[idx] + 1 : dp[jdx];
                    else
                        break;
                }
                max_idx = temp;
            } 
        }
        
        return *(dp.end() - 1);
    }
};

int main(int argc, char const *argv[])
{
    Solution S;
    vector<int> nums{2,3,1,1,4};
    cout << S.jump(nums);
    return 0;
}
