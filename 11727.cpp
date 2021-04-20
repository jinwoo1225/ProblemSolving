// #include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

const int MOD = 10007;
int cache[1001];

int tile(int n) {
    if (n <= 1) {
        return 1;
    }

    int& ret = cache[n];
    if (ret != -1) {
        return ret;
    }
    return ret = (tile(n - 1) + (2 * tile(n - 2))) % MOD;
}

int main(void) {
    memset(cache, -1, sizeof(cache));
    int n;
    scanf("%d", &n);
    cout << tile(n) << '\n';
}