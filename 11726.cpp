#include <cstring>
#include <iostream>

int cache[1001];

const int MOD = 10007;

int tile(int n) {
    if (n <= 1) {
        return 1;
    }

    int& ret = cache[n];
    if (ret != -1) {
        return ret;
    }

    return ret = (tile(n - 1) + tile(n - 2)) % MOD;
}

int main(void) {
    memset(cache, -1, sizeof(cache));
    int n;
    scanf("%d", &n);

    printf("%d\n", tile(n));
    return 0;
}