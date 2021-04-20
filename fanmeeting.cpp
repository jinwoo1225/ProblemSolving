#include <iostream>
#include <string>
#include <vector>

using namespace std;
vector<int> multiply(const vector<int> &a, const vector<int> &b) {
    vector<int> c(a.size() + b.size() + 1, 0);
    for (int i = 0; i < a.size(); ++i) {
        for (int j = 0; j < b.size(); ++j) {
            c[i + j] += a[i] * b[j];
        }
    }
    return c;
}

void addTo(vector<int> &a, const vector<int> &b, int k) {
    a.resize(max(a.size(), b.size() + k));
    for (int i = 0; i < b.size(); ++i) {
        a[k + i] += b[i];
    }
}

void subFrom(vector<int> &a, const vector<int> &b) {
    a.resize(max(a.size(), b.size() + 1));
    for (int i = 0; i < b.size(); ++i) {
        a[i] -= b[i];
    }
}

vector<int> karatsuba(const vector<int> &a, const vector<int> &b) {
    int an = a.size(), bn = b.size();
    if (an < bn) return karatsuba(b, a);
    if (an == 0 || bn == 0) return vector<int>();
    if (an <= 50) return multiply(a, b);

    int half = an / 2;

    vector<int> a0(a.begin(), a.begin() + half);
    vector<int> a1(a.begin() + half, a.end());

    vector<int> b0(b.begin(), b.begin() + min<int>(b.size(), half));
    vector<int> b1(b.begin() + min<int>(b.size(), half), b.end());

    vector<int> z2 = karatsuba(a1, b1);
    vector<int> z0 = karatsuba(a0, b0);

    addTo(a0, a1, 0);
    printf("\n");

    addTo(b0, b1, 0);

    vector<int> z1 = karatsuba(a0, b0);
    subFrom(z1, z0);
    subFrom(z1, z2);

    vector<int> ret;
    addTo(ret, z0, 0);
    addTo(ret, z1, half);
    addTo(ret, z2, half + half);
    return ret;
}

int solve(const string &fans, const string &members) {
    int N = members.size(), M = fans.size();
    // printf("%d %d\n", M, N);
    vector<int> A(N), B(M);
    for (int i = 0; i < N; i++) {
        A[i] = (members[i] == 'M');
    }
    for (int i = 0; i < M; i++) {
        B[i] = (fans[M - i - 1] == 'M');
    }
    vector<int> C = karatsuba(A, B);

    int allHugs = 0;
    for (int i = N - 1; i < M; i++) {
        // printf("%d \n", i);
        if (C[i] == 0) {
            allHugs++;
        }
    }
    return allHugs;
}

int main(void) {
    int C;
    scanf("%d\n", &C);

    string fans, members;

    while (C--) {
        cin >> members;
        cin >> fans;

        cout << solve(fans, members) << '\n';
    }
    return 0;
}