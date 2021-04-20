#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main(void) {
    int N, q, cnt = 0;
    bool ans[1001] = {0};

    bool sieve[1001] = {0};
    for (int i = 2; i <= 1001; ++i) {
        if (sieve[i] == false) {
            ans[i] = true;
        }
        for (int j = i; j <= 1001; j += i) {
            sieve[j] = true;
        }
    }

    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%d", &q);
        if (ans[q] == true) {
            cnt++;
        }
    }
    printf("%d\n", cnt);

    return 0;
}