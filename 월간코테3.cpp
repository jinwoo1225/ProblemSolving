#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

struct Node {
    int weight;
    int number;
    bool visited = false;
    vector<int> edge;
};
vector<Node> nodes;
long long sum;

bool everythingZero() {
    for (int i = 0; i < nodes.size(); i++) {
        if (nodes[i].weight) {
            return false;
        }
    }
    return true;
}

long long solve(int n) {
    nodes[n].visited = true;
    for (int i = 0; i < nodes[n].edge.size(); i++) {
        if (nodes[nodes[n].edge[i]].visited != true) {
            nodes[n].weight -= solve(nodes[n].edge[i]);
        }
    }
    sum += abs(nodes[n].weight);
    long long ret = nodes[n].weight;
    printf("adding %d to %d\n", nodes[n].weight, n);
    nodes[n].weight = 0;
    return ret;
}

long long solution(vector<int> a, vector<vector<int>> edges) {
    long long answer = 0;
    Node N;
    sum = 0;
    for (size_t i = 0; i < a.size(); i++) {
        sum += N.weight = a[i];
        N.number = i;
        nodes.push_back(N);
    }
    if (sum != 0) {
        return -1;
    }

    for (size_t i = 0; i < edges.size(); i++) {
        nodes[edges[i][0]].edge.push_back(edges[i][1]);
        nodes[edges[i][1]].edge.push_back(edges[i][0]);
    }

    solve(0);

    return sum;
}

int main(void) {
    // [[0,1],[3,4],[2,3],[0,3]]
    vector<int> a;
    a.push_back(-5);
    a.push_back(0);
    a.push_back(2);
    a.push_back(1);
    a.push_back(2);
    vector<vector<int>> edges(4);
    edges[0].push_back(0);
    edges[0].push_back(1);

    edges[1].push_back(3);
    edges[1].push_back(4);

    edges[2].push_back(2);
    edges[2].push_back(3);

    edges[3].push_back(0);
    edges[3].push_back(3);

    vector<int> b;
    b.push_back(2);
    b.push_back(-2);
    vector<vector<int>> edgesB(1);
    edgesB[0].push_back(0);
    edgesB[0].push_back(1);

    cout << solution(b, edgesB) << '\n';
    return 0;
}