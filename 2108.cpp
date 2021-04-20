#include <algorithm>
#include <cmath>
#include <iostream>
#include <numeric>
#include <vector>

using namespace std;

int modeV(const vector<int>& V) {
    int A[8001] = {0};

    for (int i = 0; i < V.size(); i++) {
        A[V[i] + 4000] += 1;
    }

    auto maxP = max_element(A, A + 8001);
    int first = *maxP;
    int firstIndex = (maxP - A);
    auto secondMaxP = max_element(maxP + 1, A + 8001);
    int second = *secondMaxP;
    int secondIndex = (secondMaxP - A);

    return first == second ? secondIndex - 4000 : firstIndex - 4000;
}

int main(void) {
    int N, c;
    vector<int> ans;
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%d", &c);
        ans.push_back(c);
    }
    sort(ans.begin(), ans.end());
    int size = ans.size();
    double mean = round(double(accumulate(ans.begin(), ans.end(), 0)) / size);
    cout << int(mean) << '\n';
    cout << ans[size / 2] << '\n';
    cout << modeV(ans) << '\n';
    cout << ans[size - 1] - ans[0] << '\n';
}