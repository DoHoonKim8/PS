#include <iostream>
#include <memory.h>
#define MAX 300

using namespace std;

int scores[MAX + 1];
int dp[MAX + 1];

int solve(int n) {
    if (dp[n]) return dp[n];
    if (solve(n - 3) + scores[n - 1] > solve(n - 2))
        dp[n] = dp[n - 3] + scores[n - 1] + scores[n];
    else dp[n] = dp[n - 2] + scores[n];
    return dp[n];
}

int main() {
    int N;
    cin >> N;
    memset(dp, 0, sizeof(dp));

    for (int i = 1; i <= N; i++) cin >> scores[i];
    dp[1] = scores[1];
    dp[2] = scores[1] + scores[2];
    dp[3] = max(scores[1], scores[2]) + scores[3];
    cout << solve(N) << endl;
}
