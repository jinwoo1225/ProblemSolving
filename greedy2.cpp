#include <algorithm>
#include <string>
#include <vector>

using namespace std;

const int INF = 987654321;

int solution(string name) {
    int answer = 0;
    string S(name.size(), 'A');
    vector<bool> visited(name.size(), false);
    int cur = 0;
    while (S != name) {
        int next = 0;
        int curDist, nextDist = INF;

        S[cur] = name[cur];
        visited[cur] = true;
        answer += min(name[cur] - 'A', 'Z' - name[cur] + 1);
        for (int i = 0; i < name.size(); i++) {
            if (cur == i || visited[i] || name[i] == 'A') continue;

            curDist = min(abs(i - cur), int(name.size()) - abs(i - cur));
            if (nextDist > curDist) {
                nextDist = curDist;
                next = i;
            }
        }
        cur = next;
        answer += (nextDist < INF ? nextDist : 0);
    }
    return answer;
}