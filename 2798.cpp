#include <algorithm>
#include <iostream>

using namespace std;

int main(void) {
    int N, M, cards[100], maxi = -1;
    scanf("%d %d", &N, &M);
    for (int i = 0; i < N; i++) {
        scanf("%d", &cards[i]);
    }
    sort(cards, cards + N);
    for (int i = 0; i < N; i++) {
        for (int j = i + 1; j < N; j++) {
            for (int k = j + 1; k < N; k++) {
                if (cards[i] + cards[j] + cards[k] <= M) {
                    maxi = max(maxi, cards[i] + cards[j] + cards[k]);
                }
            }
        }
    }
    printf("%d", maxi);
}