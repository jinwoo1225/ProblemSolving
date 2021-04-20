#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<long long> K;
long long k, n;

int main(void) {
    long long lanCable;

    scanf("%lld %lld", &k, &n);

    for (int i = 0; i < k; i++) {
        scanf("%lld", &lanCable);
        K.push_back(lanCable);
    }
    sort(K.begin(), K.end());
    long long start, end;
    start = 1;
    end = K[K.size() - 1];
    long long mid;
    long long cnt = 0;
    long long MAX = 0;

    while (start <= end) {
        mid = (start + end) / 2;
        cnt = 0;
        for (long long i = 0; i < K.size(); i++) {
            cnt += K[i] / mid;
        }
        if (cnt >= n) {
            start = mid + 1;
            MAX = max(MAX, mid);
        } else {
            end = mid - 1;
        }
    }

    cout << MAX << '\n';
}