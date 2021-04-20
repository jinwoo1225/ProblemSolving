#include <cstring>
#include <iostream>

using namespace std;

int cacheTaste[10001];
int cacheNotTaste[10001];
int wine[10001];

int n;
void tastefunc(int w) {
    if (w == n) {
        return;
    }
    int& taste = cacheTaste[w];
    int& notTaste = cacheNotTaste[w];
    tastefunc(w + 1);
    taste =
        wine[w] + max(cacheNotTaste[w + 1], cacheNotTaste[w + 2] + wine[w + 1]);
    notTaste = max(cacheNotTaste[w + 1], cacheTaste[w + 1]);
    // 313131*
    return;
}

int main(void) {
    int w;

    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", &w);
        wine[i] = w;
    }

    cacheNotTaste[n - 1] = wine[n - 1];
    cacheTaste[n - 1] = wine[n - 1];

    tastefunc(0);

    cout << max(cacheTaste[0], cacheNotTaste[0]) << '\n';
}