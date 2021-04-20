#include <iostream>
#include <string>
#include <vector>

using namespace std;

bool canCross(int howMany, const vector<int> stones, int k) {
    int jump = 0;
    // printf("how many : %d\n", howMany);
    for (int stone : stones) {
        if (stone < howMany) {
            jump++;
        } else {
            jump = 0;
        }
        if (jump == k) {
            return false;
        }
    }
    return true;
}

int solution(vector<int> stones, int k) {
    int answer = 0;
    int lo = 0;
    int hi = 200000000;
    while (lo <= hi) {
        int mid = (lo + hi) / 2;
        if (!canCross(mid, stones, k)) {
            hi = mid - 1;
        } else {
            answer = mid;
            lo = mid + 1;
        }
    }
    return answer;
}

int main(void) { cout << solution({2, 4, 5, 3, 2, 1, 4, 2, 5, 1}, 3) << '\n'; }