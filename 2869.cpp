#include <cmath>
#include <iostream>

using namespace std;

int main(void) {
    int A, B, V, C;
    scanf("%d %d %d", &A, &B, &V);

    printf("%0.f", ceil(double(V - A) / double(A - B)) + 1);

    return 0;
}