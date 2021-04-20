#include <algorithm>
#include <deque>
#include <iostream>
using namespace std;

int A[8], visited[8] = {false};

int N;
void solve(int M, deque<int> D) {
    if (!M) {
        for (int a : D) {
            printf("%d ", a);
        }
        printf("\n");
        return;
    }
    for (int i = 0; i < N; i++) {
        if (visited[i] == false) {
            visited[i] = true;
            D.push_back(A[i]);
            solve(M - 1, D);
            visited[i] = false;
            D.erase(find(D.begin(), D.end(), A[i]));
        }
    }
    return;
}
int main(void) {
    int sz;

    scanf("%d %d", &N, &sz);
    for (int i = 0; i < N; i++) {
        scanf("%d", &A[i]);
    }
    deque<int> ans;
    sort(A, A + N);
    solve(sz, ans);
}