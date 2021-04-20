#include <iostream>
#include <string>
#include <vector>

using namespace std;

int n, C;
int volume[100], need[100];
string name[100];
int cache[1001][100];

int pack(int capacity, int item) {
    if (item == n) return 0;
    int& ret = cache[capacity][item];
    if (ret != -1) return ret;
    ret = pack(capacity, item + 1);
    if (capacity >= volume[item]) {
        ret = max(ret, pack(capacity - volume[item], item + 1) + need[item]);
    }
    cout << ret;
    return ret;
}

void reconstruct(int capacity, int item, vector<string>& picked) {
    if (item == n) return;
    if (pack(capacity, item) == pack(capacity, item + 1)) {
        reconstruct(capacity, item + 1, picked);
    } else {
        picked.push_back(name[item]);
        reconstruct(capacity - volume[item], item + 1, picked);
    }
}

int main(void) {
    int C;
    vector<string> picked;
    cin >> C;
    while (C--) {
        cin >> n >> C;
        for (int i = 0; i < n; i++) {
            getline(cin, name[i], ' ');
            cin >> volume[i] >> need[i];
        }
        for (int i = 0; i < n; i++) {
            cout << name[i] << '\n';
        }

        cout << pack(C, 0) << '\n';
        reconstruct(C, 0, picked);
        for (string P : picked) {
            cout << P << '\n';
        }
    }
}