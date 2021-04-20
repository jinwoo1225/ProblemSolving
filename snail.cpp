#include <cmath>
#include <cstring>
#include <iostream>

using namespace std;

int C, m, n;

double cache[1000][2001];

double climb(int days, int climbed) {
    if (days == m) {
        return climbed >= n ? 1 : 0;
    }
    double &ret = cache[days][climbed];
    if (ret != -1.0) {
        return ret;
    }
    return ret = (0.75 * climb(days + 1, climbed + 2)) +
                 (0.25 * climb(days + 1, climbed + 1));
}

int main(void) {
    scanf("%d\n", &C);

    while (C--) {
        for (int i = 0; i < 1000; i++) {
            for (int j = 0; j < 2001; j++) {
                cache[i][j] = -1;
            }
        }

        scanf("%d %d", &n, &m);
        cout.precision(11);
        cout << climb(0, 0) << '\n';
    }
}
