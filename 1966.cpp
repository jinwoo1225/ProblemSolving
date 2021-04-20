#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

typedef struct printDocu {
    int priority;
    bool target;
} printDocu;

vector<printDocu> printQueue;

bool compareByPriority(const printDocu a, const printDocu b) {
    return a.priority < b.priority;
}

int solve(void) {
    int n = 1;
    vector<printDocu> temp;
    while (printQueue.size() > 0) {
        vector<printDocu>::iterator max_e = max_element(
            printQueue.begin(), printQueue.end(), compareByPriority);
        // for (auto &&i : printQueue) {
        //     printf("(%d,%d), ", i.priority, i.target);
        // }
        // printf("\n");
        if (max_e->target) {
            return n;
        }

        n++;

        if (printQueue.front().priority < max_e->priority) {
            int cnt = max_e - printQueue.begin();
            for (int i = 0; i < cnt; i++) {
                printQueue.push_back(printQueue[i]);
            }
            for (int i = 0; i < cnt + 1; i++) {
                printQueue.erase(printQueue.begin());
            }
            // for (auto &&i : printQueue) {
            //     printf("(%d,%d), ", i.priority, i.target);
            // }
            // printf("\n");
        } else {
            printQueue.erase(printQueue.begin());
        }
    }
    // return 0;
}

int main(void) {
    int C, N, M, q;
    printDocu P;
    P.target = false;
    scanf("%d\n", &C);
    while (C--) {
        printQueue.clear();
        scanf("%d %d", &N, &M);
        for (int i = 0; i < N; i++) {
            scanf("%d", &q);
            P.priority = q;
            printQueue.push_back(P);
        }
        printQueue[M].target = true;
        printf("%d\n", solve());
    }
}