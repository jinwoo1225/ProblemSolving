#include <iostream>
#include <vector>

using namespace std;

int main(void) {
    int N;
    bool flag = true;
    scanf("%d", &N);
    vector<int> cards(N);
    vector<int> temp;
    for (int i = 0; i < N; i++) {
        cards[i] = i + 1;
    }
    while (cards.size() != 1) {
        for (int i = 1; i < cards.size(); i += 2) {
            temp.push_back(cards[i]);
        }
        if (cards.size() % 2) {
            temp.push_back(temp.front());
            temp.erase(temp.begin());
        }
        cards = temp;
        temp.clear();
    }

    printf("%d", cards.front());

    return 0;
}
