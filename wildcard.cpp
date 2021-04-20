#include <string.h>

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool match(const string& w, const string& s) {
    int pos = 0;
    while (pos < s.size() && pos < w.size() &&
           (w[pos] == '?' || w[pos] == s[pos])) {
        pos++;
    }

    if (pos == w.size()) {
        return pos == s.size();
    }

    if (w[pos] == '*') {
        for (int skip = 0; pos + skip <= s.size(); skip++) {
            if (match(w.substr(pos + 1), s.substr(pos + skip))) {
                return true;
            }
        }
    }
    return false;
}

int main(void) {
    int C, n;
    string w, s;
    vector<string> ans;
    scanf("%d\n", &C);

    while (C--) {
        ans.clear();
        getline(cin, w);
        scanf("%d\n", &n);
        for (int i = 0; i < n; i++) {
            getline(cin, s);
            if (match(w, s)) {
                ans.push_back(s);
            }
        }
        sort(ans.begin(), ans.end());
        for (string i : ans) {
            cout << i << '\n';
        }
    }
}