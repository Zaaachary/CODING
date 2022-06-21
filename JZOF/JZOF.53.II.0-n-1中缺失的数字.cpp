#include <vector>
#include <algorithm>
#include <unordered_set>
using namespace std;

class Solution {
/*
执行用时： 12 ms , 在所有 C++ 提交中击败了 85.17% 的用户 内存消耗： 16.5 MB , 在所有 C++ 提交中击败了 99.90% 的用户
*/
public:
    int missingNumber(vector<int>& nums) {
        int length = nums.size();
        int cur_idx = 0;
        while(cur_idx < length){
            if(cur_idx != nums[cur_idx])
                return cur_idx;
            cur_idx ++;
        }
        return length;
    };

    int missingNumber(vector<int>& nums) {
        sort(nums.begin(), nums.end());
        int n = nums.size() + 1;
        for (int i = 0; i < n - 1; i++) {
            if (nums[i] != i) {
                return i;
            }
        }
        return n - 1;
    };

    int missingNumber_hash(vector<int>& nums) {
        unordered_set<int> set;
        int n = nums.size() + 1;
        for (int i = 0; i < n - 1; i++) {
            set.insert(nums[i]);
        }
        int missing = -1;
        for (int i = 0; i <= n - 1; i++) {
            if (!set.count(i)) {
                missing = i;
                break;
            }
        }
        return missing;
    }

};