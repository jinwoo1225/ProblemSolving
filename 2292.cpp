#include <iostream>

using namespace std;

int main(void) {
    int N, cnt = 1;
    scanf("%d", &N);
    for (int i = 1; i < N; i += 6 * cnt++)
        ;
    printf("%d", cnt);
}
