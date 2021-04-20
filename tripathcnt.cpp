#include <cstring>
#include <iostream>

using namespace std;

int C, H, x;
int tri[100][100];
int cache[101][101];
int pathCache[101][101];

int path(int y, int x) {
    if (y == H - 1) {
        return tri[y][x];
    }

    int& ret = pathCache[y][x];
    if (ret != -1) {
        return ret;
    }

    return ret = max(path(y + 1, x), path(y + 1, x + 1)) + tri[y][x];
}

int cnt(int y, int x) {
    if (y == H - 1) {
        return 1;
    }

    int& ret = cache[y][x];
    if (ret != -1) {
        return ret;
    }

    ret = 0;
    if (path(y + 1, x + 1) >= path(y + 1, x)) {
        ret += cnt(y + 1, x + 1);
    }
    if (path(y + 1, x + 1) <= path(y + 1, x)) {
        ret += cnt(y + 1, x);
    }
    return ret;
}

int main(void) {
    scanf("%d\n", &C);

    while (C--) {
        memset(cache, -1, sizeof(cache));
        memset(pathCache, -1, sizeof(pathCache));

        scanf("%d\n", &H);

        for (int i = 0; i < H; i++) {
            for (int j = 0; j < i + 1; j++) {
                scanf("%d", &x);
                tri[i][j] = x;
            }
        }

        cout << cnt(0, 0) << '\n';
    }
}