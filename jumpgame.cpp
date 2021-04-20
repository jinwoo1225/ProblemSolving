#include <string.h>

#include <iostream>

using namespace std;

int H, cache[100][100];
int board[100][100];
string line;

bool jump(int y, int x) {
    if (y >= H || x >= H) {
        return false;
    }

    if (y == H - 1 & x == H - 1) {
        return 1;
    }

    int& ret = cache[y][x];

    if (ret != -1) {
        return ret;
    }

    int size_of_jump = board[y][x];

    return ret = (jump(y + size_of_jump, x) || jump(y, size_of_jump + x));
}

int main(void) {
    int C;
    scanf("%d\n", &C);

    while (C--) {
        memset(cache, -1, sizeof(cache));
        scanf("%d\n", &H);
        for (int i = 0; i < H; i++) {
            getline(cin, line);
            for (int j = 0; j < H; j++) {
                board[i][j] = line[2 * j] - '0';
            }
        }
        cout << (jump(0, 0) ? "YES" : "NO") << '\n';
    }
}