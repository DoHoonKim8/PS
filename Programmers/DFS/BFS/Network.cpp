#include <iostream>
#include <string>
#include <vector>

using namespace std;

vector<int> visited;

void dfs(int V, vector<vector<int>>& computers) {
    visited[V] = true;
    vector<int> row = computers[V];
    for (int i = 0; i < row.size(); i++) {
        if (row[i] && !visited[i]) dfs(i, computers);
    }
}

int solution(int n, vector<vector<int>> computers) {
    int answer = 0;
    visited.resize(n);
    fill(visited.begin(), visited.end(), false);

    for (int i = 0; i < n; i++) {
        if (!visited[i]) {
            dfs(i, computers);
            answer++;
        }
    }

    return answer;
}

int main() {
    int answer = solution(3, {{ 1, 1, 0 }, { 1, 1, 0 }, { 0, 0, 1 }});

    cout << answer << endl;
    return 0;
}
