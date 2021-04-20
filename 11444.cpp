#include <cstring>
#include <iostream>
#include <map>

using namespace std;
const int MOD = 1000000007;

map<long long, long long> fibo;

long long reverseFibo(long long fib) {
    if (fibo.count(fib)) {
        return fibo[fib];
    }
    long long k = fib / 2;
    if (fib % 2) {
        return fibo[fib] = (reverseFibo(k) * reverseFibo(k + 1) +
                            reverseFibo(k - 1) * reverseFibo(k)) %
                           MOD;
    } else {
        return fibo[fib] = (reverseFibo(k) * reverseFibo(k) +
                            reverseFibo(k - 1) * reverseFibo(k - 1)) %
                           MOD;
    }
}

int main(void) {
    long long N;
    fibo[0] = fibo[1] = 1;
    scanf("%lld", &N);
    printf("%lld", N == 0 ? 0 : reverseFibo(N - 1));
}
