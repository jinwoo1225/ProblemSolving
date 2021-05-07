#include <algorithm>
#include <deque>
#include <iostream>
#include <queue>
#include <string>
#include <vector>

using namespace std;

pair<long long, long long> up_down_heap(
    vector<pair<char, long long>> operations) {
    priority_queue<long long, vector<long long>, greater<long long>> min_heap;
    priority_queue<long long, vector<long long>, greater<long long>>
        min_heap_dump;
    priority_queue<long long, vector<long long>, less<long long>> max_heap;
    priority_queue<long long, vector<long long>, less<long long>> max_heap_dump;

    for (pair<char, long long> operation : operations) {
        if (operation.first == 'I') {
            // insertion
            min_heap.push(operation.second);
            max_heap.push(operation.second);
        } else {
            // deletion
            if (min_heap.size() > 0) {
                if (operation.second == 1) {
                    // max_heap pop
                    min_heap_dump.push(max_heap.top());
                    max_heap.pop();

                } else {
                    // min_heap pop
                    max_heap_dump.push(min_heap.top());
                    min_heap.pop();
                }
            }
        }
        while (min_heap.size() > 0 && min_heap_dump.size() > 0 &&
               min_heap_dump.top() == min_heap.top()) {
            min_heap.pop();
            min_heap_dump.pop();
        }
        while (max_heap.size() > 0 && max_heap_dump.size() > 0 &&
               max_heap_dump.top() == max_heap.top()) {
            max_heap.pop();
            max_heap_dump.pop();
        }
    }
    if (min_heap.size() > 0) {
        return pair(max_heap.top(), min_heap.top());
    } else {
        return pair(0, 0);
    }
}

int main(void) {
    int T, N;
    long long num;
    char operand;
    scanf("%d", &T);

    while (T--) {
        scanf("%d", &N);
        vector<pair<char, long long>> operation;
        while (N--) {
            cin >> operand >> num;
            operation.push_back(pair(operand, num));
        }
        pair<long long, long long> answer = up_down_heap(operation);
        if (answer.first == 0 && answer.second == 0) {
            printf("EMPTY\n");
        } else {
            printf("%lld %lld\n", answer.first, answer.second);
        }
    }
}

/*
1
7
I 16
I -5643
D -1
D 1
D 1
I 123
D -1

1
9
I -45
I 653
D 1
I -642
I 45
I 97
D 1
D -1
I 333


2
7
I 16
I -5643
D -1
D 1
D 1
I 123
D -1
9
I -45
I 653
D 1
I -642
I 45
I 97
D 1
D -1
I 333
333 45
*/