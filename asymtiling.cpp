#include <cstring>
#include <iostream>

using namespace std;

const int MOD = 1000000007;
int C, w;
int cache[101];
int cache2[101];

int tile(int n) {
    if (n <= 1) {
        return 1;
    }
    int& ret = cache[n];
    if (ret != -1) {
        return ret;
    }

    return ret = (tile(n - 2) + tile(n - 1)) % MOD;
}
int asymmetric(int width) {
    if (width % 2 == 1) {
        return (tile(width) - tile(width / 2) + MOD) % MOD;
    }
    int ret = tile(width);
    ret = (ret - tile(width / 2) + MOD) % MOD;
    ret = (ret - tile(width / 2 - 1) + MOD) % MOD;
    return ret;
}

int asymmetric2(int width) {
    if (width <= 2) {
        return 0;
    }
    int& ret = cache2[width];
    if (ret != -1) {
        return ret;
    }

    ret = asymmetric2(width - 2) % MOD;
    ret = (ret + asymmetric2(width - 4)) % MOD;
    ret = (ret + tile(width - 3)) % MOD;
    ret = (ret + tile(width - 3)) % MOD;
    return ret;
}

int main(void) {
    scanf("%d\n", &C);

    while (C--) {
        memset(cache, -1, sizeof(cache));
        memset(cache2, -1, sizeof(cache2));
        scanf("%d", &w);

        cout << asymmetric2(w) << '\n';
    }
}