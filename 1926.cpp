#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main(void) {
    priority_queue<unsigned long long, vector<unsigned long long>,
                   greater<unsigned long long>>
        min_heap;

    int T;

    scanf("%d", &T);

    while (T--) {
        unsigned long long cmd;
        scanf("%lld", &cmd);

        if (cmd == 0) {
            if (min_heap.size() > 0) {
                printf("%lld\n", min_heap.top());
                min_heap.pop();
            } else {
                printf("0\n");
            }
        } else {
            min_heap.push(cmd);
        }
    }
    return 0;
}