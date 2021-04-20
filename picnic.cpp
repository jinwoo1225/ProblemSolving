#include <iostream>
using namespace std;

int n;
bool areFriends[10][10];

int countPairing(bool taken[10]) {
    int firstFree = -1;

    for (int i = 0; i < n; i++) {
        if (!taken[i]) {
            firstFree = i;
            break;
        }
    }
    // 재귀 상황이므로 기저상황을 처리
    // 이 경우에는 모든짝이 찾아진 경우
    if (firstFree == -1) {
        return 1;
    }

    int ret = 0;

    for (int pairWith = firstFree + 1; pairWith < n; pairWith++) {
        if (!taken[pairWith] && areFriends[firstFree][pairWith]) {
            taken[firstFree] = taken[pairWith] = true;
            ret += countPairing(taken);
            taken[firstFree] = taken[pairWith] = false;
        }
    }

    return ret;
}

int main(void) {
    short C, m;
    short a, b;

    cin >> C;
    for (int i = 0; i < C; i++) {
        cin >> n >> m;

        for (int j = 0; j < 10; j++) {
            for (int k = 0; k < 10; k++) {
                areFriends[j][k] = false;
            }
        }

        for (short i = 0; i < m; i++) {
            cin >> a >> b;
            areFriends[a][b] = areFriends[b][a] = true;
        }

        bool taken[10] = {false};
        cout << countPairing(taken) << endl;
    }

    return 0;
}