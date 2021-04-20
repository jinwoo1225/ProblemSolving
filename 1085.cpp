#include <iostream>

using namespace std;

int main(void) {
    int x, y, w, h;

    scanf("%d %d %d %d", &x, &y, &w, &h);
    int dx = min(w - x, x);
    int dy = min(h - y, y);
    printf("%d", min(dx, dy));
}