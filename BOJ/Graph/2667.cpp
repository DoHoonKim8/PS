#include <iostream>
#include <vector>
#include <algorithm>

#define MAX 25

using namespace std;

int map[MAX][MAX];
int visited[MAX][MAX];
int N;

int complexCount;

int dfs(int x, int y) {
    visited[x][y] = true;
    int houseCount = 1;
    if (x >= 1 && !visited[x - 1][y] && map[x - 1][y]) 
        houseCount += dfs(x - 1, y);
    if (x < N - 1 && !visited[x + 1][y] && map[x + 1][y]) 
        houseCount += dfs(x + 1, y);
    if (y >= 1 && !visited[x][y - 1] && map[x][y - 1]) 
        houseCount += dfs(x, y - 1);
    if (y < N - 1 && !visited[x][y + 1] && map[x][y + 1])
        houseCount += dfs(x, y + 1);
    return houseCount;
}

int main() {
    cin >> N;
    for (int i = 0; i < N; i++) {
        char row[N];
        cin >> row;
        for (int j = 0; j < N; j++) {
            map[i][j] = row[j] - '0';
        }
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) visited[i][j] = false;
    }
    vector<int> houseCounts;
    complexCount = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            if (!visited[i][j] && map[i][j] == 1) {
                houseCounts.push_back(dfs(i, j));
                complexCount++;
            }
        }
    }

    cout << complexCount << endl;
    sort(houseCounts.begin(), houseCounts.end());
    for (int n: houseCounts) cout << n << endl;

    return 0;
}
