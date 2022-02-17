#include <iostream>
#include <vector>

using namespace std;

vector<bool> visited;
vector<bool> finished;
vector<int> choice;
int cnt;

void dfs(int V) {
    visited[V] = true;
    int next = choice[V];
    if (visited[next]) {
        if (!finished[next]) {
            for (int curr = next; curr != V; curr = choice[curr]) cnt++;
            cnt++; 
        }
   } else dfs(next);
    finished[V] = true;
}

int main() {
    int T;
    cin >> T;
    for (int i = 0; i < T; i++) {
        int n;
        cin >> n;

        visited.resize(n + 1);
        finished.resize(n + 1);
        choice.resize(n + 1);
        
        fill(visited.begin(), visited.end(), false);
        fill(finished.begin(), finished.end(), false);

        for (int j = 1; j <= n; j++) cin >> choice[j];

        cnt = 0;
        for (int j = 1; j <= n; j++) {
            if (!visited[j]) dfs(j);
        }
        cout << n - cnt << endl;
    }

    return 0;
}
