#include <algorithm>
#include <cstring>
#include <iostream>

using namespace std;

int worth[101], weight[101];
int cache[100000][101];
int N, K;

int pack(int capacity, int item) {
    if (item == N) {
        return 0;
    }
    int& ret = cache[capacity][item];
    if (ret != -1) {
        return ret;
    }
    ret = pack(capacity, item + 1);
    if (capacity >= weight[item]) {
        ret = max(ret, (pack(capacity - weight[item], item + 1) + worth[item]));
    }
    return ret;
}

int main(void) {
    memset(cache, -1, sizeof(cache));
    scanf("%d %d", &N, &K);
    for (int i = 0; i < N; i++) {
        scanf("%d %d", &weight[i], &worth[i]);
    }
    printf("%d", pack(K, 0));
}