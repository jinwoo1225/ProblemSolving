#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool match(const string& w, const string& s) {
    int pos = 0;
    while (pos < s.size() && pos < w.size() &&
           (w[pos] == s[pos] || w[pos] == '*')) {
        pos++;
    }
    if (pos == w.size()) {
        return pos == s.size();
    }
    return false;
}

bool have(vector<string> V, string s) {
    for (string id : V) {
        if (id == s) {
            return true;
        }
    }
    return false;
}

bool have(vector<vector<string>> VVS, vector<string> VS) {
    for (vector<string> SV : VVS) {
        if (SV == VS) {
            return true;
        }
    }
    return false;
}

vector<vector<string>> answer;
void check(int level, const vector<string>& chkstr,
           const vector<vector<string>>& a) {
    vector<string> checking = chkstr;
    if (level == a.size()) {
        sort(checking.begin(), checking.end());
        if (!have(answer, checking)) {
            answer.push_back(checking);
        }
        return;
    }

    for (size_t i = 0; i < a[level].size(); i++) {
        if (have(checking, a[level][i])) {
            continue;
        }
        checking.push_back(a[level][i]);
        check(level + 1, checking, a);
        checking.pop_back();
    }
}

int solution(vector<string> user_id, vector<string> banned_id) {
    vector<vector<string>> bannedList(banned_id.size());

    for (size_t bid = 0; bid < banned_id.size(); bid++) {
        for (size_t uid = 0; uid < user_id.size(); uid++) {
            if (match(banned_id[bid], user_id[uid])) {
                bannedList[bid].push_back(user_id[uid]);
            }
        }
    }
    vector<vector<string>> answerList(banned_id.size());

    check(0, vector<string>(), bannedList);

    return answer.size();
}

int main(void) {
    cout << solution({"frodo", "fradi", "crodo", "abc123", "frodoc"},
                     {"fr*d*", "*rodo", "******", "******"})
         << '\n';
    return 0;
}