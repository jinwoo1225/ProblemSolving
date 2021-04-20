#include <iostream>
#include <vector>

using namespace std;

int main(void) {
    int N, M;

    scanf("%d %d", &N, &M);

    vector<bool> sieve(M + 1);
    for (int i = 2; i <= M; ++i) {
        if (sieve[i] == false) {
            if (i >= N) {
                printf("%d\n", i);
            }
        }
        for (int j = i; j <= M; j += i) {
            sieve[j] = true;
        }
    }

    return 0;
}