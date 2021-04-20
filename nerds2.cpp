#include <algorithm>
#include <iostream>
#include <map>
#include <vector>

using namespace std;

int N;
map<int, int> coords;

bool isDominated(int x, int y) {
    map<int, int>::iterator it = coords.lower_bound(x);
    if (it == coords.end()) return false;
    return y < it->second;
}

void removeDominated(int x, int y) {
    map<int, int>::iterator it = coords.lower_bound(x);

    if (it == coords.begin()) return;
    --it;
    while (true) {
        if (it->second > y) break;
        if (it == coords.begin()) {
            coords.erase(it);
            break;
        } else {
            map<int, int>::iterator jt = it;
            --jt;
            coords.erase(it);
            it = jt;
        }
    }
}

int registered(int x, int y) {
    if (isDominated(x, y)) return coords.size();
    removeDominated(x, y);
    coords[x] = y;
    return coords.size();
}

int main(void) {
    int C;
    scanf("%d", &C);
    while (C--) {
        coords.clear();
        scanf("%d", &N);
        int sum = 0;
        for (int i = 0; i < N; i++) {
            int x, y;
            scanf("%d %d", &x, &y);
            sum += registered(x, y);
        }
        printf("%d\n", sum);
    }
}
