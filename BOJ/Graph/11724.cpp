#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<vector<int>> adj;
vector<bool> visited;

void dfs(int v) {
    visited[v] = true;
    for (int a: adj[v]) {
        if (!visited[a]) dfs(a);
    }
}

int main() {
    int N, M;
    cin >> N >> M;

    adj.resize(N + 1);
    visited.resize(N + 1);

    for (int i = 0; i < M; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    fill(begin(visited), end(visited), false);
    
    int components = 0;
    for (int v = 1; v <= N; v++) {
        if (!visited[v]) {
            dfs(v);
            components++;
        }
    }

    cout << components << endl;

    return 0;
}
