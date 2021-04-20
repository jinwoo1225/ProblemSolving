#include <iostream>

using namespace std;

long long pow(long long a, long long n) {
    long long ret = 1;
    for (long long i = 0; i < n; i++) {
        ret *= a;
    }
    return ret;
}

int main(void) {
    int N, r, c;
    scanf("%d %d %d", &N, &r, &c);
    long long size, sum = 0;
    long long y, x = y = 0;

    while (true) {
        if (N == 1) break;
        size = pow(2, N);
        N--;
        // printf("%d %d\n", y, x);
        if (r < y + size / 2 && c < x + size / 2) {
            // 1사분면
        } else if (r < y + size / 2 && c >= x + size / 2) {
            sum += size * size / 4;
            x += size / 2;
        } else if (r >= y + size / 2 && c < x + size / 2) {
            sum += size * size / 2;
            y += size / 2;
        } else {
            sum += 3 * size * size / 4;
            x += size / 2;
            y += size / 2;
        }
    }
    long long ans =
        (r == y ? (c == x ? sum : sum + 1) : (c == x ? sum + 2 : sum + 3));
    printf("%lld\n", ans);
    return 0;
}