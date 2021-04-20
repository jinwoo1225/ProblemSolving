#include <iostream>
#include <string>

using namespace std;

bool contain666(int num) {
    int a = num;
    int temp, cnt = 0;
    while (a > 0) {
        temp = a % 10;
        if (temp == 6) {
            cnt++;
        } else {
            cnt = 0;
        }
        if (cnt == 3) {
            return true;
        }
        a /= 10;
    }
    return false;
}

int solve(int n) {
    int cnt = 0, temp;
    int w = 666;
    while (1) {
        if (contain666(w)) {
            cnt++;
        }
        if (cnt == n) {
            return w;
        }
        w++;
    }
}

int main(void) {
    int n;

    scanf("%d", &n);

    cout << solve(n) << '\n';
}