#include <iostream>
#include <string>

using namespace std;

int main(void) {
    string C("-1");
    cin >> C;

    while (C != "0") {
        bool ans = true;
        for (int i = 0; i < int(C.size() / 2); i++) {
            if (C[i] != C[C.size() - i - 1]) {
                ans = false;
                break;
            }
        }
        cout << (ans ? "yes" : "no") << '\n';
        cin >> C;
    }
}