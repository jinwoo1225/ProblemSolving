#include <cstring>
#include <iostream>

using namespace std;
const int _mod = 1000000007;
//   2147483648
int C, n;

int cache[101];

int fill(int n) {
    if (n <= 1) {
        return 1;
    }

    int& ret = cache[n];
    if (ret != -1) {
        return ret;
    }

    return ret = (fill(n - 2) + fill(n - 1)) % _mod;
}

int main(void) {
    scanf("%d\n", &C);

    while (C--) {
        memset(cache, -1, sizeof(cache));
        scanf("%d", &n);
        cout << fill(n) << '\n';
    }
}