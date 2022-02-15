#include <iostream>
#include <vector>
#include <queue>
#include <algorithm>

using namespace std;

vector<vector<int>> adj;
vector<bool> visited;

void dfs(int V) {
    if (!visited[V]) {
        cout << V << ' ';
        visited[V] = true;
        for (int next: adj[V]) dfs(next);
    }
}

void bfs(int V) {
    queue<int> vs;
    vs.push(V);
    visited[V] = true;
    while (!vs.empty()) {
        int curr = vs.front ();
        cout << curr << ' ';
        vs.pop ();
        for (int a: adj[curr]) {
            if (!visited[a]) {
                vs.push(a);
                visited[a] = true;
            }
        }
    }
}

int main() {
    int N, M, V; // 정점의 개수, 간선의 개수, 시작할 정점의 번호
    cin >> N >> M >> V;
    
    adj.resize(N + 1);
    visited.resize(N + 1);

    for (int i = 1; i <= M; i++) {
        int u, v;
        cin >> u >> v;
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    for (int i = 1; i <= N; i++) {
        sort(begin(adj[i]), end(adj[i]));
    }

    fill(begin(visited), end(visited), false);
    dfs(V);
    cout << endl;
    fill(begin(visited), end(visited), false);
    bfs(V);

    return 0;
}
