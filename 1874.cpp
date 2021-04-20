#include <iostream>
#include <string>
#include <vector>

using namespace std;

int stack[100002];
vector<int> vecStack;
vector<int> vecStackStr;

int main(void) {
    int n;
    string ret;
    scanf("%d", &n);
    for (int i = 1; i < n + 1; i++) {
        scanf("%d", &stack[i]);
        vecStack.push_back(n + 1 - i);
    }
    int depth = 0;
    vecStackStr.push_back(0);

    for (int i = 1; i < n + 1; i++) {
        while (true) {
            if (vecStackStr.back() != stack[i]) {
                if (vecStack.size() == 0) {
                    printf("NO\n");
                    return 0;
                }

                ret += "+";
                vecStackStr.push_back(vecStack.back());
                vecStack.pop_back();
            } else {
                ret += "-";
                vecStackStr.pop_back();
                break;
            }
        }
    }
    for (int i = 0; i < ret.size(); i++) {
        printf("%c\n", ret[i]);
    }
}