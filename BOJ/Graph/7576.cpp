#include <iostream>
#include <vector>
#include <queue>
#include <tuple>
#define MAX 1000

using namespace std;

typedef tuple<int, int> INDEX;

int M, N;
int tomatoes[MAX][MAX];
int visited[MAX][MAX];
queue<INDEX> q;
int result;

vector<INDEX> getZeroAdj(INDEX idx) {
    int x = get<0>(idx);
    int y = get<1>(idx);
    vector<INDEX> result;
    int dx[4] = { 0, 0, 1, -1 };
    int dy[4] = { 1, -1, 0 ,0 };
    for (int i = 0; i < 4; i++) {
        int newX = x + dx[i];
        int newY = y + dy[i];
        if (newX >= 0 && newX < N && newY >= 0 && newY < M
            && !visited[newX][newY] && !tomatoes[newX][newY])
            result.push_back(make_tuple(newX, newY));
    }
    return result;
}

void bfs() {
    while (1) {
        int size = q.size();
        int cnt = 0;
        while (cnt < size) {
            INDEX front = q.front();
            vector<INDEX> adjs = getZeroAdj(front);
            for (INDEX adj: adjs) {
                int adjX = get<0>(adj);
                int adjY = get<1>(adj);
                visited[adjX][adjY] = true;
                q.push(adj);
            }
            q.pop();
            cnt++;
        }
        if (q.empty()) break;
        
        for (int i = 0; i < q.size(); i++) {
            INDEX front = q.front();
            int frontX = get<0>(front);
            int frontY = get<1>(front);
            tomatoes[frontX][frontY] = 1;
            q.push(front);
            q.pop();
        }
        result++;
    }
}

int main() {
    cin >> M >> N;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) cin >> tomatoes[i][j];
    }

    result = 0;
    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) visited[i][j] = false;
    }

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (tomatoes[i][j] == 1) {
                visited[i][j] = true;
                q.push(make_tuple(i, j));
            }
        }
    }

    bfs();

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < M; j++) {
            if (!tomatoes[i][j]) result = -1;
        }
    }

    cout << result << endl;
    return 0;
}
