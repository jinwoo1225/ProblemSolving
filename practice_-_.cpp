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
        vector<vector<int>> EDGEMAP(newA.size(), vector<int>());
        vector<int> Deg(newA.size(),
                        0);  // Deg[i] i 번째 정점에서 얼마나 간선이 있는가?
        // Deg[i] = 1 이면 i 번째 정점은 최외곽 정점

        for (auto elem : edges) {
            EDGEMAP[elem[0]].push_back(elem[1]);
            Deg[elem[0]]++;
            EDGEMAP[elem[1]].push_back(elem[0]);
            Deg[elem[1]]++;
        }
        queue<int> Q;
        for (int i = 0; i < Deg.size(); i++) {
            if (Deg[i] == 1) Q.push(i);
        }
        long long int cnt = 0;  // 총 움직임 기록
        while (!Q.empty())  // 가지치기 방식 외부의 정점부터 탐색
                            // 위상 정렬과 비슷
        {
            int popItem = Q.front();
            visited[popItem] = true;
            Q.pop();
            cnt += abs(newA[popItem]);  // 가지고 있는 전부를 옮김.
            int next = -1;
            for (auto elem : EDGEMAP[popItem])  // 연결된 정점들중 안간곳(->
                                                // 하나 밖에 없음)을 찾음
            {
                if (!visited[elem]) {
                    next = elem;
                    break;
                }
            }
            if (next == -1)  // 다음 정점이 없다 == 다 도착해서 여기서 모인다.
            {
                cnt -= abs(newA[popItem]);
                break;
            }
            newA[next] += newA[popItem];  // 다음 정점에 넘기자.
            newA[popItem] = 0;
            Deg[next] -= 1;  // 현재 연결되있는 정점의 간선 수 - 1
            if (Deg[next] == 1)  // 최외각 정점이면 추가
                Q.push(next);
        }
        return cnt;
    }
}

int main() { cout << solution({-2, 2}, {{0, 1}}) << endl; }
