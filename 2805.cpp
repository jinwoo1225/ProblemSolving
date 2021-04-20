#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main(void) {
    int N, M, logSize;
    scanf("%d %d", &N, &M);
    vector<int> woods(N);
    for (int i = 0; i < N; i++) {
        int tree;
        scanf("%d", &tree);
        woods[i] = tree;
    }

    long long lo = 0, mid, hi = *max_element(woods.begin(), woods.end()), sum,
              ans = 0;
    ;
    while (lo <= hi) {
        mid = (hi + lo) / 2;
        sum = 0;
        for (int i = 0; i < N; i++) {
            if (woods[i] > mid) {
                sum += woods[i] - mid;
            }
        }
        if (sum >= M) {
            lo = mid + 1;
            ans = max(ans, mid);
        } else {
            hi = mid - 1;
        }
    }
    printf("%lld", ans);
    return 0;
}
