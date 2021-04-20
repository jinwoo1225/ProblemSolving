#include <cstdio>
#include <iostream>
// #include <string>
#include <cstring>

using namespace std;

const int dy[8] = {-1, -1, -1, 1, 1, 1, 0, 0};
const int dx[8] = {-1, 0, 1, -1, 0, 1, -1, 1};

char board[8][8];

int main(void) {
    int a;
    scanf("%d", &a);
}

bool inRange(int y, int x) {
    if (y > 8 && y < 0) {
        return false;
    }
    if (x > 8 && x < 0) {
        return false;
    }

    return true;
}

bool hasWord(int y, int x, const string& word) {
    if (!inRange(y, x)) {
        return false;
    }

    if (board[y][x] != word[0]) return false;

    if (word.size() == 1) return true;

    for (int direction = 0; direction < 8; ++direction) {
        int nextY = y + dy[direction], nextX = x + dx[direction];
        if (hasWord(nextY, nextX, word.substr(1))) {
            return true;
        }
    }
}