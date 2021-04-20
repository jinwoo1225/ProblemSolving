#include <iostream>
#include <string>
#include <vector>

using namespace std;

const int INF = 9999;

const char linked[10][17] = {
    //   0123456789012345
    "1110000000000000", "0001000101010000", "0000100000100011",
    "1000111100000000", "0000001110101000", "1010000000000011",
    "0001000000000011", "0000110100000011", "0111110000000000",
    "0001110001000100"};

bool areAligned(const vector<int>& clocks) {
    for (int i = 0; i < 16; i++) {
        if (clocks[i] != 12) {
            return false;
        }
    }
    return true;
}

void push(vector<int>& clocks, int swtch) {
    for (int i = 0; i < 16; i++) {
        if (linked[swtch][i] == '1') {
            clocks[i] += 3;
            if (clocks[i] == 15) clocks[i] = 3;
        }
    }
}

int solve(vector<int>& clocks, int swtch) {
    if (swtch == 10) {
        return areAligned(clocks) ? 0 : INF;
    }

    int ret = INF;
    for (int cnt = 0; cnt < 4; cnt++) {
        ret = min(ret, cnt + solve(clocks, swtch + 1));
        push(clocks, swtch);
    }

    return ret;
}

int main(void) {
    int C;

    cin >> C;

    while (C--) {
        vector<int> clock(0);
        short a;
        for (int i = 0; i < 16; i++) {
            cin >> a;
            clock.push_back(a);
        }
        int ans = solve(clock, 0);
        cout << (ans == INF ? -1 : ans) << '\n';
    }
}