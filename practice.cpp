#include <iostream>
#include <queue>
#include <string>
#include <vector>

using namespace std;

long long solution(vector<int> a, vector<vector<int>> edges) {
    vector<long long int> newA;

    long long answer = -2;
    long long S = 0;
    for (long long int elem : a) {
        S += elem;
        newA.push_back(elem);
    }

    if (S != 0)
        return -1;
    else {
        vector<bool> visited(newA.size(), false);
        // 그래프
        vector<vector<int>> EDGEMAP(newA.size(), vector<int>());
        // 간선
        vector<int> Deg(newA.size(), 0);

        for (auto elem : edges) {
            EDGEMAP[elem[0]].push_back(elem[1]);
            Deg[elem[0]]++;
            EDGEMAP[elem[1]].push_back(elem[0]);
            Deg[elem[1]]++;
        }
        // 터미널 노드 큐
        queue<int> Q;
        for (int i = 0; i < Deg.size(); i++) {
            if (Deg[i] == 1) Q.push(i);
        }
        long long int cnt = 0;
        while (!Q.empty()) {
            int popItem = Q.front();
            visited[popItem] = true;
            Q.pop();
            cnt += abs(newA[popItem]);
            int next = -1;
            for (auto elem : EDGEMAP[popItem]) {
                if (!visited[elem]) {
                    next = elem;
                    break;
                }
            }
            if (next == -1) {
                cnt -= abs(newA[popItem]);
                break;
            }
            newA[next] += newA[popItem];
            newA[popItem] = 0;
            Deg[next] -= 1;
            if (Deg[next] == 1) Q.push(next);
        }
        return cnt;
    }
}

int main() {
    cout << solution({-5, 0, 2, 1, 2}, {{0, 1}, {3, 4}, {2, 3}, {0, 3}})
         << endl;
}