#include <deque>
#include <string>
#include <vector>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    int answer = 0;
    deque<deque<int>> newBoard(board.size());
    deque<int> temp(1, -2), basket(1, -1);
    for (size_t i = 0; i < board.size(); i++) {
        for (size_t j = 0; j < board[0].size(); j++) {
            if (board[i][j] != 0) {
                newBoard[j].push_front(board[i][j]);
            }
        }
    }
    for (int m : moves) {
        if (newBoard[m - 1].size()) {
            basket.push_back(newBoard[m - 1].back());
            newBoard[m - 1].pop_back();
        }
    }
    while (basket.size() != 1) {
        temp.push_front(basket.back());
        basket.pop_back();
        while (basket.size() < 0 || basket.back() == temp.front()) {
            printf("%d %d %d %d\n", basket.size(), basket.back(), temp.size(),
                   temp.front());
            getchar();
            answer += 2;
            basket.pop_back();
            temp.pop_front();
        }
    }

    return answer;
}

#include <iostream>
int main(void) {
    cout << solution({{5, 5, 5, 5, 5},
                      {5, 5, 5, 5, 5},
                      {5, 5, 5, 5, 5},
                      {5, 5, 5, 5, 5},
                      {5, 5, 5, 5, 5}},
                     {1, 5, 3, 5, 1, 2, 1, 4, 1})
         << '\n';
}