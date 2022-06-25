/*
@File    :   0047.medium.!.全排列II.cpp
@Time    :   2022/06/24 14:20:16
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
执行用时： 4 ms , 在所有 C++ 提交中击败了 92.04% 的用户 内存消耗： 8.7 MB , 在所有 C++ 提交中击败了 58.65% 的用户
*/
#include <algorithm>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> result;
    vector<int> current;
    vector<bool> visited;

    vector<vector<int>> permuteUnique(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        visited.resize(nums.size());
        DFS(nums, 0);

        return result;
    }

    void DFS(vector<int>& nums, int target_place) {
        if (target_place == nums.size()){
            result.push_back(current);
            return ;
        }

        for (int i = 0; i < nums.size(); i++){
            if (visited[i] || (i > 0 && nums[i] == nums[i-1] && visited[i-1] ))
                continue;    // no.i 和 no.i-1 一样且 no.i-1 已经访问
            visited[i] = true;
            current.emplace_back(nums[i]);
            DFS(nums, target_place+1);
            visited[i] = false;
            current.pop_back();   
        }
    }
};