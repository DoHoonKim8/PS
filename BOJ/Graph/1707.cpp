#include <iostream>
#include <vector>
#include <set>

using namespace std;

vector<vector<int>> adj;
vector<bool> visited;
vector<int> group; // 각 인덱스(정점)는 1, -1의 값을 가진다

bool dfs(int groupNum, int V) {
    visited[V] = true;
    group[V] = groupNum;
    bool result = true;
    for (int v: adj[V]) {
        if (group[v] == groupNum) return false;
        else if (!visited[v]) result = result && dfs(groupNum * (-1), v);
        else continue;
    }
    return result;
}

int main() {
    int K, V, E;
    cin >> K;
    for (int i = 0; i < K; i++) {
        cin >> V >> E;

        visited.resize(V + 1);
        adj.resize(V + 1);
        group.resize(V + 1);
        for (int j = 0; j < E; j++) {
            int u, v;
            cin >> u >> v;
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        fill(visited.begin(), visited.end(), false);
        
        bool ans = true;
        for (int i = 1; i <= V; i++) {
            if (!visited[i]) ans = ans && dfs(1, i);
        }
        if (ans) cout << "YES" << endl;
        else cout << "NO" << endl;

        for (int i = 0; i < adj.size(); i++) adj[i].clear();
        visited.clear();
        group.clear();
    }
    return 0;
}
