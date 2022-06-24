/*
@File    :   0090.medium.!.子集II.cpp
@Time    :   2022/06/24 11:23:59
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
*/

#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;
/*
执行用时： 0 ms , 在所有 C++ 提交中击败了 100.00% 的用户 内存消耗： 11.3 MB , 在所有 C++ 提交中击败了 7.23% 的用户
*/

class Solution {
public:
    vector<int> current;
    vector<vector<int>> result;

    vector<vector<int>> subsetsWithDup(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        DFS(false, 0, nums);
        return result;
    }

    void DFS(bool choosePrev, int target, vector<int>& nums){
        if(target == nums.size()){
            result.push_back(current);
            return ;
        }
        DFS(false, target + 1, nums);
        if (!choosePrev && target > 0 and nums[target] == nums[target-1])
            return ;
        current.push_back(nums[target]);
        DFS(true, target + 1, nums);
        current.pop_back();
    }
};


int main(int argc, char const *argv[])
{
    Solution S;
    vector<int> nums{1,2,3};
    vector<vector<int>> result;
    result = S.subsetsWithDup(nums);
    for (int i = 0; i < result.size(); i++){
        for (int j = 0; j < result[i].size(); j++)
            cout << result[i][j];
        cout << endl;
    }
   return 0;
}
