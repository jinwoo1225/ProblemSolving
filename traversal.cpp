#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;
int N;

vector<int> slice(const vector<int> v, int a, int b) {
    return vector<int>(v.begin() + a, v.begin() + b);
}

void printPostOrder(const vector<int>& preorder, const vector<int>& inorder) {
    const int N = preorder.size();

    if (preorder.empty()) {
        return;
    }

    const int root = preorder[0];

    const int L = find(inorder.begin(), inorder.end(), root) - inorder.begin();

    const int R = N - 1 - L;

    printPostOrder(slice(preorder, 1, L + 1), slice(inorder, 0, L));
    printPostOrder(slice(preorder, L + 1, N), slice(inorder, L + 1, N));
    cout << root << " ";
}

int main(void) {
    int C;
    cin >> C;
    vector<int> preorder, inorder;
    while (C--) {
        preorder.clear();
        inorder.clear();
        cin >> N;
        for (int i = 0; i < N; i++) {
            int a;
            cin >> a;
            preorder.push_back(a);
        }
        for (int i = 0; i < N; i++) {
            int a;
            cin >> a;
            inorder.push_back(a);
        }
        printPostOrder(preorder, inorder);
    }
}