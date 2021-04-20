#include <algorithm>
#include <iostream>

using namespace std;

int gcd(int a, int b) { return b ? gcd(b, a % b) : a; }

int main(void) {
    int n, m, G;
    scanf("%d %d", &n, &m);
    if (n < m) swap(n, m);
    G = gcd(n, m);
    printf("%d\n%d", G, (n * m) / G);
}