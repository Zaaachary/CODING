/*
@File    :   0079.medium.!.单词搜索.cpp
@Time    :   2022/06/25 20:09:51
@Author  :   Zhifeng Li
@Contact :   li_zaaachary@163.com
@Desc    :   
*/
#include <vector>
#include <string>
using namespace std;


class Solution {
/*
执行用时： 712 ms , 在所有 C++ 提交中击败了 21.80% 的用户 内存消耗： 7.7 MB , 在所有 C++ 提交中击败了 90.40% 的用户
*/
public:
    vector<pair<int, int>> directions{{0, 1},  {1, 0}, {0, -1}, {-1, 0}};
    int m, n;
    string path = "";    
    vector<vector<bool>> visited;

    bool exist(vector<vector<char>>& board, string word) {
        m = board.size();
        n = board[0].size();   
        visited = vector<vector<bool>>(m, vector<bool>(n, false));
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                visited[i][j] = true;
                path.push_back(board[i][j]);
                if (back_tracing_DFS(board, word, i, j))
                    return true;
                path.pop_back();
                visited[i][j] = false;
            }
        }
        return false;
    }

    bool back_tracing_DFS(vector<vector<char>> &board, string word, int i, int j){
        if (path.length() == word.length() && path == word)
            return true;
        else{
            char next_ch = word[path.length()];
            for (const auto& dir: directions) {
                int newi = i + dir.first, newj = j + dir.second;            
                if (0 <= newi && newi < m && 0 <= newj && newj < n 
                    && !visited[newi][newj] && board[newi][newj] == next_ch){
                    path.push_back(board[newi][newj]);
                    visited[newi][newj] = true;
                    if (back_tracing_DFS(board, word, newi, newj))
                        return true;
                    path.pop_back();
                    visited[newi][newj] = false;
                }
            }
            return false;
        }
    }
};

class Solution_leetcode {
public:
    bool check(vector<vector<char>>& board, vector<vector<int>>& visited, int i, int j, string& s, int k) {
        if (board[i][j] != s[k]) {
            return false;
        } else if (k == s.length() - 1) {
            return true;
        }
        visited[i][j] = true;
        vector<pair<int, int>> directions{{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
        bool result = false;
        for (const auto& dir: directions) {
            int newi = i + dir.first, newj = j + dir.second;
            if (newi >= 0 && newi < board.size() && newj >= 0 && newj < board[0].size()) {
                if (!visited[newi][newj]) {
                    bool flag = check(board, visited, newi, newj, s, k + 1);
                    if (flag) {
                        result = true;
                        break;
                    }
                }
            }
        }
        visited[i][j] = false;
        return result;
    }

    bool exist(vector<vector<char>>& board, string word) {
        int h = board.size(), w = board[0].size();
        vector<vector<int>> visited(h, vector<int>(w));
        for (int i = 0; i < h; i++) {
            for (int j = 0; j < w; j++) {
                bool flag = check(board, visited, i, j, word, 0);
                if (flag) {
                    return true;
                }
            }
        }
        return false;
    }
};
