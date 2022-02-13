#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Graph {

public:
    int N;
    vector<vector<int>> adj;
    vector<bool> visited;

    Graph(): N(0) {

    }
    
    Graph(int n): N(n) {
        adj.resize(N);
        visited.resize(N);
    }

    void addEdge(int u, int v) {
        adj[u].push_back(v);
        adj[v].push_back(u);
    }

    void sortList() {
        for (int i=0; i<N; i++)
            sort(adj[i].begin(), adj[i].end());
    }

    int dfsAll() {
        int components = 0;
        fill(visited.begin(), visited.end(), false);
        for (int i = 0; i < N; i++) {
            if (!visited[i]) {
                cout << "--new DFS begins--" << endl;
                int nodes = dfs(i);
                cout << "size of component: " << nodes << endl;
                components++;
            }
        }
        return components;
    }

private:
    int dfs(int curr) {
        int nodes = 1;
        visited[curr] = true;
        cout << "node " << curr << " visited" << endl;
        for (int next: adj[curr]) {
            if (!visited[next]) {
                nodes += dfs(next);
            }
        }
        return nodes;
    }

};

int main () {
    Graph G(9);
    G.addEdge(0, 1);
    G.addEdge(0, 2);
    G.addEdge(1, 3);
    G.addEdge(1, 5);
    G.addEdge(3, 4);
    G.addEdge(4, 5);
    G.addEdge(2, 6);
    G.addEdge(2, 8);
    G.addEdge(6, 7);
    G.addEdge(6, 8);
    G.sortList();
    G.dfsAll();
    return 0;
}
