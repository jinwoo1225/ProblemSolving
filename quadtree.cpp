#include <iostream>
#include <string>
#include <vector>

#define MAX_SIZE 20

using namespace std;

bool DECOMPRESSED[MAX_SIZE][MAX_SIZE];
int pointer;
void printBoard() {
    for (int i = 0; i < MAX_SIZE; i++) {
        for (int j = 0; j < MAX_SIZE; j++) {
            printf("%d", DECOMPRESSED[j][i]);
        }
        printf("\n");
    }
}
void fill(int y, int x, int size, char C) {
    bool ans;
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            DECOMPRESSED[y + i][x + j] = (C == 'w');
        }
    }
}
void decompress(const string S, int y, int x, int size) {
    pointer++;
    if (S[pointer] == 'w' || S[pointer] == 'b') {
        fill(y, x, size, S[pointer]);
    } else {
        int half = size / 2;
        decompress(S, y, x, half);
        decompress(S, y, x + half, half);
        decompress(S, y + half, x, half);
        decompress(S, y + half, x + half, half);
    }
}

void compress() {}
string solve(const string Qt) {
    decompress(Qt, 0, 0, 20);
    // compress(Qt)
    printBoard();
    return Qt;
}

string reverse(string::iterator& it) {
    char head = *it;
    it++;
    if (head == 'b' || head == 'w') {
        return string(1, head);
    }
    string upperLeft = reverse(it);
    string upperRight = reverse(it);
    string lowerLeft = reverse(it);
    string lowerRight = reverse(it);

    return string("x") + lowerLeft + lowerRight + upperLeft + upperRight;
}

int main(void) {
    int C;
    string Qt;
    cin >> C;

    while (C--) {
        pointer = -1;
        cin >> Qt;
        string::iterator a = Qt.begin();
        // cout << solve(Qt) << '\n';
        cout << reverse(a) << '\n';
    }
}
