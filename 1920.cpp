#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

int main(void) {
    iostream::ios_base::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    vector<long long> A;
    int N, M;
    long long number, test;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> number;
        A.push_back(number);
    }
    sort(A.begin(), A.end());
    cin >> M;
    for (int i = 0; i < M; i++) {
        cin >> test;
        cout << binary_search(A.begin(), A.end(), test) << '\n';
    }
}