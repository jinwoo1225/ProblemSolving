#include <iostream>
#include <map>

using namespace std;

map<long, long> F;

long fibo(long num) {
    if (F.count(num)) {
        return F[num];
    }
    long k = num / 2;
    if (num % 2) {
        return F[num] = fibo(k) * fibo(k + 1) + fibo(k - 1) * fibo(k);
    } else {
        return F[num] = fibo(k) * fibo(k) + fibo(k - 1) * fibo(k - 1);
    }
}
int main(void) {
    int T;
    long N;
    scanf("%d", &T);
    F[0] = F[1] = 1;
    while (T--) {
        scanf("%ld", &N);
        if (N == 0) {
            cout << 1 << " " << 0 << '\n';
            continue;
        } else if (N == 1) {
            cout << 0 << " " << 1 << '\n';
            continue;
        }
        cout << fibo(N - 2) << " " << fibo(N - 1) << '\n';
    }
    return 0;
}
