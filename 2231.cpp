#include <iostream>
#include <string>

using namespace std;

int main(void) {
    int N;
    scanf("%d", &N);

    for (int i = 1; i <= N; i++) {
        int ans = i;
        string digits = to_string(i);

        for (char digit : digits) {
            ans += digit - '0';
        }

        if (ans == N) {
            printf("%d", i);
            return 0;
        }
    }
    printf("0");
    return 0;
}