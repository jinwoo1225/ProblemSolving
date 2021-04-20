#include <cstring>
#include <iostream>

using namespace std;

int n, triangle[100][100];
int cache[100][100];

int solve(int y, int x) {
    if (y == n - 1) {
        return triangle[y][x];
    }

    int& ret = cache[y][x];
    if (ret != -1) {
        return cache[y][x];
    }

    return ret = max(solve(y + 1, x), solve(y + 1, x + 1)) + triangle[y][x];
}

int main(void) {
    int C;
    int num;
    scanf("%d\n", &C);

    while (C--) {
        memset(cache, -1, sizeof(cache));
        scanf("%d\n", &n);

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < i + 1; j++) {
                scanf("%d", &num);
                triangle[i][j] = num;
            }
        }
        cout << solve(0, 0) << '\n';
    }
}