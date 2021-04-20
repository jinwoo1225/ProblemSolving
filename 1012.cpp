#include <cstring>
#include <iostream>

using namespace std;

int farm[50][50];
bool visited[50][50];
int MX, MY, K;

bool check(int y, int x) { return !visited[y][x] && farm[y][x]; }

void place(int y, int x) {
    if (check(y, x)) {
        visited[y][x] = true;
        if (y - 1 >= 0) place(y - 1, x);
        if (y + 1 < MY) place(y + 1, x);
        if (x - 1 >= 0) place(y, x - 1);
        if (x + 1 < MX) place(y, x + 1);
    }
}

int main(void) {
    int T;
    scanf("%d", &T);
    while (T--) {
        memset(farm, 0, sizeof(farm));
        memset(visited, false, sizeof(visited));
        scanf("%d %d %d", &MX, &MY, &K);
        for (int i = 0; i < K; i++) {
            int y, x;
            scanf("%d %d", &x, &y);
            farm[y][x] = 1;
        }
        int cnt = 0;
        for (int i = 0; i < MY; i++)
            for (int j = 0; j < MX; j++)
                if (check(i, j)) {
                    place(i, j);
                    cnt++;
                }
        printf("%d\n", cnt);
    }
}