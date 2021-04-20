#include <iostream>
#include <string>
#include <vector>
using namespace std;

// type, 상대적 위치, [y,x]
const int types[4][3][2] = {{{0, 0}, {1, 0}, {0, 1}},
                            {{0, 0}, {0, 1}, {1, 1}},
                            {{0, 0}, {1, 0}, {1, 1}},
                            {{0, 0}, {1, 0}, {1, -1}}};

bool set(vector<vector<int> >& board, int y, int x, int type, int delta) {
    bool ok = true;
    for (int i = 0; i < 3; i++) {
        const int ny = y + types[type][i][0];
        const int nx = x + types[type][i][1];
        //보드에 존재하는가?
        if (ny < 0 || ny >= board.size() || nx < 0 || nx >= board[0].size()) {
            ok = false;
        } else if ((board[ny][nx] += delta) > 1) {
            ok = false;
        }
    }
    return ok;
}

int cover(vector<vector<int> >& board) {
    int y = -1, x = -1;
    //좌상단 0인경우 찾기
    for (int i = 0; i < board.size(); i++) {
        for (int j = 0; j < board[0].size(); j++) {
            if (board[i][j] == 0) {
                // y, x 헷갈렸음 ㅋㅋㅋㅋㅋㅋ
                y = i;
                x = j;
                break;
            }
        }
        if (y != -1) {
            break;
        }
    }

    if (y == -1) return 1;

    int ret = 0;

    for (int type = 0; type < 4; type++) {
        if (set(board, y, x, type, 1)) {
            ret += cover(board);
        }
        set(board, y, x, type, -1);
    }
    return ret;
}

int main(void) {
    int C;
    short H, W;
    string S;

    cin >> C;

    for (int i = 0; i < C; i++) {
        cin >> H >> W;
        vector<vector<int> > board(H, vector<int>(W, 0));
        int cnt = 0;

        for (int j = 0; j < H; j++) {
            cin >> S;
            for (int k = 0; k < W; k++) {
                if (S[k] == '#') {
                    board[j][k] = 1;
                } else {
                    board[j][k] = 0;
                    cnt++;
                }
            }
        }
        // for (int j = 0; j < H; j++) {
        //     for (int k = 0; k < W; k++) {
        //         cout << board[j][k];
        //     }
        //     cout << endl;
        // }
        if (cnt % 3)
            cout << 0 << '\n';
        else
            cout << cover(board) << '\n';
    }

    return 0;
}
