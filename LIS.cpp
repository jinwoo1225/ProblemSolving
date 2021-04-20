#include <cstring>
#include <iostream>
#include <vector>

using namespace std;

vector<int> sequence;
int n, cache[500];

int solve(int start) {
    int& ret = cache[start];
    if (ret != -1) {
        return cache[start];
    }

    ret = 1;
    for (int next = start; next < n; next++) {
        if (sequence[start] < sequence[next]) {
            ret = max(ret, solve(next) + 1);
        }
    }
    return ret;
}

int main(void) {
    int C, num;
    scanf("%d\n", &C);

    while (C--) {
        memset(cache, -1, sizeof(cache));
        sequence.clear();
        scanf("%d\n", &n);
        int maxlen = 0;
        for (int i = 0; i < n; i++) {
            scanf("%d", &num);
            sequence.push_back(num);
        }
        for (int i = 0; i < n; i++) {
            maxlen = max(maxlen, solve(i));
        }

        cout << (!sequence.empty() ? maxlen : 0) << '\n';
    }
}