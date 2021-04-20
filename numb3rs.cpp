#include <algorithm>
#include <cstring>
#include <iostream>
#include <vector>

using namespace std;

int C, n, d, p, q;

int connected[51][51], deg[51];
// vector<int> test;
/*
double search(vector<int>& path) {
    if (path.size() == d + 1) {
        if (path.back() != q) {
            return 0.0;
        }
        double ret = 1.0;
        for (int i = 0; i < path.size() - 1; i++) {
            ret /= deg[path[i]];
        }
        return ret;
    }
    double ret = 0;
    for (int there = 0; there < n; there++) {
        if (connected[path.back()][there]) {
            path.push_back(there);
            ret += search(path);
            path.pop_back();
        }
    }
    return ret;
}
*/

double cache[51][101];  // here, days

double search(int here, int days) {
    if (days == 0) {
        return (here == p ? 1.0 : 0.0);
    }

    double& ret = cache[here][days];

    if (ret > -0.5) {
        return ret;
    }

    ret = 0.0;
    for (int there = 0; there < n; there++) {
        if (connected[here][there]) {
            ret += search(there, days - 1) / deg[there];
        }
    }
    return ret;
}

int main(void) {
    scanf("%d\n", &C);
    cout.precision(11);
    while (C--) {
        for (int i = 0; i < 51; i++) {
            for (int j = 0; j < 101; j++) {
                cache[i][j] = -1.0;
            }
        }

        // test.clear();
        int a, t;
        scanf("%d %d %d", &n, &d, &p);
        for (int i = 0; i < n; i++) {
            int cnt = 0;
            for (int j = 0; j < n; j++) {
                scanf("%d", &a);
                connected[i][j] = a;
                if (a == 1) {
                    cnt++;
                }
            }
            deg[i] = cnt;
        }

        scanf("%d", &t);
        for (int i = 0; i < t; i++) {
            scanf("%d", &q);
            cout << search(q, d) << " ";
            // test.push_back(q);
        }
        cout << '\n';
    }
}