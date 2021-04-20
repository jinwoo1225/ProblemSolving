#include <cstring>
#include <iostream>

using namespace std;

const int INF = 10000001;

int cache[(10 * 10 * 10 * 10 * 10 * 10) + 1];

int solve(int n) {
    if (n == 1) {
        return 0;
    }
    int& ret = cache[n];
    if (ret != -1) {
        return ret;
    }
    ret = INF;
    if (n % 3 == 0) {
        ret = min(ret, solve(n / 3) + 1);
    }
    if (n % 2 == 0) {
        ret = min(ret, solve(n / 2) + 1);
    }
    ret = min(ret, solve(n - 1) + 1);
    return ret;
}

int main(void) {
    memset(cache, -1, sizeof(cache));
    int n, cnt;
    scanf("%d", &n);
    cnt = solve(n);
    printf("%d", cnt);
    return 0;
}