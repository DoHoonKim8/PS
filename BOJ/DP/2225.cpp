#include <iostream>
#include <memory.h>
#define MAX 1000000000

using namespace std;

int dp[400][200];

// n combination r을 계산하면 되는 문제
int solve(int n, int r) {
    if (dp[n][r]) return dp[n][r];
    if (r == 0 || n == r) {
        dp[n][r] = 1;
        return 1;
    }
    dp[n][r] = (solve(n - 1, r - 1) + solve(n - 1, r)) % MAX;
    return dp[n][r];
}

int main() {
    int N, K;
    cin >> N >> K;

    for (int i = 1; i <= N; i++) {
        memset(dp[i], 0, K);
    }

    dp[0][0] = 1;
    cout << solve(N + K - 1, K - 1) << endl;

    return 0;
}
