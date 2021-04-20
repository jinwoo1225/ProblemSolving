#include <iostream>
#include <string>

using namespace std;

int H, W;
char board[51][51];
bool testB[8][8];

string correctone1[8] = {"BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB",
                         "BWBWBWBW", "WBWBWBWB", "BWBWBWBW", "WBWBWBWB"};
string correctone2[8] = {"WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW",
                         "WBWBWBWB", "BWBWBWBW", "WBWBWBWB", "BWBWBWBW"};

int main(void) {
    string line;
    scanf("%d %d\n", &H, &W);
    for (int i = 0; i < H; i++) {
        getline(cin, line);
        for (int j = 0; j < W; j++) {
            board[i][j] = line[j];

            // W => False, B => True
        }
    }
    int mini = 987654321;

    for (int i = 0; i <= H - 8; i++) {
        for (int j = 0; j <= W - 8; j++) {
            int count1 = 0;
            int count2 = 0;
            for (int k = 0; k < 8; k++) {
                for (int l = 0; l < 8; l++) {
                    board[i + k][j + l] == correctone1[k][l] ? 0 : count1++;
                    board[i + k][j + l] == correctone2[k][l] ? 0 : count2++;
                }
            }
            mini = min(mini, min(count1, count2));
        }
    }
    printf("%d", mini);
    return 0;
}
