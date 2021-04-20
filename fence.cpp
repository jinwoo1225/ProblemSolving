#include <iostream>
#include <vector>

using namespace std;
vector<int> fence;

int solve(int left, int right) {
    if (left == right) {
        return fence[left];
    }

    int mid = (left + right) / 2;
    int ret = max(solve(left, mid), solve(mid + 1, right));

    int lo = mid, hi = mid + 1;

    int height = min(fence[lo], fence[hi]);
    ret = max(ret, height * 2);
    while (left < lo || hi < right) {
        if (hi < right && (lo == left || fence[lo - 1] < fence[hi + 1])) {
            hi++;
            height = min(height, fence[hi]);
        } else {
            lo--;
            height = min(height, fence[lo]);
        }

        ret = max(ret, height * (hi - lo + 1));
    }
    return ret;
}

int main(void) {
    int C;

    cin >> C;

    while (C--) {
        int n;
        fence.clear();
        scanf("%d\n", &n);
        for (int i = 0; i < n; i++) {
            int j;
            scanf("%d", &j);
            fence.push_back(j);
        }
        cout << solve(0, n - 1) << '\n';
    }

    return 0;
}