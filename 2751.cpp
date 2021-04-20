#include <algorithm>
#include <iostream>

using namespace std;
int main(void) {
    int N;
    int A[1000000];
    scanf("%d", &N);
    for (int i = 0; i < N; i++) {
        scanf("%d", &A[i]);
    }
    sort(A, A + N);
    for (int i = 0; i < N; i++) {
        printf("%d\n", A[i]);
    }
}