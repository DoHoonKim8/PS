#include <iostream>
#include <memory.h>
#define MAX 30

using namespace std;

int dp[MAX + 1];

int solve(int n) {
    if (n % 2 == 1 || dp[n]) return dp[n];
    int result = dp[2] * solve(n - 2);
    for (int i = n - 4; i >= 2; i -= 2) {
        result += 2 * solve(i);
    }
    dp[n] = result + 2;
    return dp[n];
}

int main() {
    int N;
    cin >> N;
    memset(dp, 0, N + 1);
    dp[2] = 3;

    cout << solve(N) << endl;

    return 0;
}
