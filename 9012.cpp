#include <iostream>
#include <string>

using namespace std;

int main(void) {
    int T;
    string PS;
    cin >> T;
    while (T--) {
        cin >> PS;
        int V = 0;
        bool ans = true;
        for (size_t i = 0; i < PS.size(); i++) {
            PS[i] == '(' ? V++ : V--;
            if (V < 0) {
                ans = false;
            }
        }
        if (V != 0) {
            ans = false;
        }
        cout << (ans ? "YES" : "NO") << '\n';
    }
}