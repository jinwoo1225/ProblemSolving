#include <algorithm>
#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> solution(string s) {
    vector<int> answer;
    vector<string> tuplesInStr;
    vector<vector<int>> tuples;
    int v = 0;
    for (int i = 1; i < s.size() - 1; i++) {
        if (s[i] == '{') {
            v = i;
        } else if (s[i] == '}') {
            string temp;
            temp.assign(s, v + 1, i - v - 1);
            tuplesInStr.push_back(s.substr(v + 1, i - v - 1) + ',');
        }
    }

    for (string T : tuplesInStr) {
        v = 0;
        vector<int> tuple;
        for (size_t i = 0; i < T.size(); i++) {
            if (T[i] == ',') {
                tuple.push_back(stoi(T.substr(v, i - v)));
                v = i + 1;
            }
        }
        tuples.push_back(tuple);
    }
    sort(tuples.begin(), tuples.end(),
         [](const vector<vector<int>>& a, const vector<vector<int>>& b) {
             return a.size() < b.size();
         });
    for (vector<int> a : tuples) {
        cout << a.size() << '\n';
    }
    return answer;
}

int main(void) {
    string s = "{{123}}";
    solution(s);
}