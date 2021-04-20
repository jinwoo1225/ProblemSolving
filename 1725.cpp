#include <iostream>
#include <vector>

using namespace std;

vector<int> hist;

int solve(int left, int right) {
    if (left == right) {
        return hist[left];
    }
    int mid = (left + right) / 2;
    int ret = max(solve(left, mid), solve(mid + 1, right));

    int lo = mid, hi = mid + 1;
    int height = min(hist[lo], hist[hi]);
    ret = max(ret, height * 2);

    while (left < lo || hi < right) {
        if (hi < right && (lo == left || hist[lo - 1] < hist[hi + 1])) {
            hi++;
            height = min(height, hist[hi]);
        } else {
            lo--;
            height = min(height, hist[lo]);
        }
        ret = max(ret, height * (hi - lo + 1));
    }
    return ret;
}

int main(void) {
    int N;
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        int j;
        scanf("%d", &j);
        hist.push_back(j);
    }
    cout << solve(0, N) << '\n';
}