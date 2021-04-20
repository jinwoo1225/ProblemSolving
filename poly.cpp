#include <algorithm>
#include <cstring>
#include <iostream>

using namespace std;
const int MOD = 10 * 1000 * 1000;
int C, l;
int cache[101][101];

int poly(int n, int first) {
    if (n == first) {
        return 1;
    }

    int& ret = cache[n][first];
    if (ret != -1) {
        return ret;
    }

    ret = 0;
    for (int second = 1; second <= n - first; second++) {
        int add = second + first - 1;
        add *= poly(n - first, second);
        add %= MOD;
        ret += add;
        ret %= MOD;
    }
    return ret;
}

int solve(int n) {
    int ret = 0;
    for (int i = 1; i <= n; i++) {
        ret += poly(n, i);
        ret %= MOD;
    }
    return ret;
}

int main(void) {
    scanf("%d\n", &C);
    while (C--) {
        memset(cache, -1, sizeof(cache));
        scanf("%d", &l);
        cout << solve(l) << '\n';
    }
}