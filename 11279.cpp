#include <algorithm>
#include <iostream>
#include <queue>
#include <vector>

using namespace std;

int main(void) {
    priority_queue<unsigned long long, vector<unsigned long long>,
                   less<unsigned long long>>
        max_heap;

    int T;

    scanf("%d", &T);

    while (T--) {
        unsigned long long cmd;
        scanf("%lld", &cmd);

        if (cmd == 0) {
            if (max_heap.size() > 0) {
                printf("%lld\n", max_heap.top());
                max_heap.pop();
            } else {
                printf("0\n");
            }
        } else {
            max_heap.push(cmd);
        }
    }
    return 0;
}