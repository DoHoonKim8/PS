#include <iostream>
#include <memory.h>
#define MAX 100

using namespace std;

long dp[MAX + 1];

long solve(int N) {
    if (dp[N]) return dp[N];
    if (N > 5) dp[N] = solve(N - 1) + solve(N - 5);
    return dp[N];
}

int main() {
    int T;
    int N;

    cin >> T;
    for (int i = 0; i < T; i++) {
        cin >> N;
        memset(dp, 0, N + 1);
        dp[1] = 1; dp[2] = 1; dp[3] = 1; dp[4] = 2; dp[5] = 2;
        cout << solve(N) << endl;
    }

    return 0;
}
