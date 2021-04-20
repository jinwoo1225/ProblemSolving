#include <algorithm>
#include <iostream>
#include <string>
#include <unordered_set>
#include <vector>

using namespace std;

bool sortBySize(const string& a, const string& b) {
    if (a.size() < b.size()) {
        return true;
    } else if (a.size() == b.size()) {
        if (a < b) {
            return true;
        }
    }

    return false;
}
int main(void) {
    int C, mini;
    vector<string> list;
    vector<string> ans;

    string word;
    scanf("%d\n", &C);
    for (int i = 0; i < C; i++) {
        cin >> word;
        list.push_back(word);
    }
    unordered_set<string> s(list.begin(), list.end());
    list.assign(s.begin(), s.end());
    sort(list.begin(), list.end(), sortBySize);

    for (int i = 0; i < list.size(); i++) {
        cout << list[i] << '\n';
    }
}