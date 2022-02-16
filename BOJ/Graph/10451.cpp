#include <iostream>
#include <vector>

using namespace std;

vector<int> sequence;
vector<bool> visited;
vector<int> cycle;

void makeCycle(int V) {
    cycle.push_back(V);
    visited[V] = true;
    if (sequence[V] == cycle.front()) {
        cycle.clear ();
        return;
    }
    makeCycle(sequence[V]);
}

int main() {
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        int N;
        cin >> N;
        int result = 0;
        sequence.resize(N + 1);
        visited.resize(N + 1);

        fill(visited.begin(), visited.end(), false);
        for (int j = 1; j <= N; j++) {
            cin >> sequence[j];
        }

        for (int j = 1; j <= N; j++) {
            if (!visited[j]) {
                makeCycle (j);
                result++;
            }
        }
        cout << result << endl;
        sequence.clear ();
        visited.clear ();
    }
}
