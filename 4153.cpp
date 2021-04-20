#include <iostream>

using namespace std;

int main(void) {
    int A, B, C = B = A = -1;
    while (true) {
        // bool ans = false;
        scanf("%d %d %d", &A, &B, &C);
        if (!(A || B || C)) break;
        if (A * A == (B * B + C * C)) {
            printf("right\n");
            continue;
        } else if (B * B == (A * A + C * C)) {
            printf("right\n");
            continue;
        } else if (C * C == (A * A + B * B)) {
            printf("right\n");
            continue;
        }
        printf("wrong\n");
    }
}