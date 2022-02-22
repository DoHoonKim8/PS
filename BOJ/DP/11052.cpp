#include <iostream>
#define MAX 1000

using namespace std;

int N;
int price[MAX + 1];
int dp[MAX + 1];

int solve(int N) {
    if (dp[N]) return dp[N];
    int result = price[N];
    for (int i = 1; i <= N / 2; i++) {
        int next = solve(N - i) + solve(i);
        if (next > result) result = next;
    }
    dp[N] = result;
    return dp[N];
}

int main() {
    int N;
    cin >> N;

    for (int i = 1; i <= N; i++) {
        cin >> price[i];
        dp[i] = 0;
    }

    dp[1] = price[1];

    cout << solve(N) << endl;

    return 0;
}
