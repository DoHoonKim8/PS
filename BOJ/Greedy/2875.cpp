#include <iostream>
#include <algorithm>

using namespace std;

int main() {
    int N, M, K;
    cin >> N >> M >> K;

    int teams[K + 1]; // x가 각각 0~K일 때 가능한 팀의 개수

    for (int x = 0; x <= K; x++) {
        teams[x] = min((N - x) / 2, M - (K - x));
    }
    int result = 0;
    for (int i = 0; i <= K; i++) {
        if (teams[i] > result) result = teams[i];
    }
    cout << result << endl;
    return 0;
}
