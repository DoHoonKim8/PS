#include <iostream>
#include <memory.h>
#include <math.h>
#define MAX 100000

using namespace std;

int dp[MAX + 1];

// n을 제곱수들의 합으로 나타낼 때, 필요한 항의 최소 개수를 구한다
int solve(int n) {
    if (dp[n] != MAX) return dp[n];
    int s = sqrt(n);
    for (int i = s; i >= 1; i--) {
        int num = 0;
        num += n / (i * i);
        int r = n % (i * i);
        if(r) num += solve(r);
        if(num < dp[n]) dp[n] = num;
    }

    return dp[n];
}

int main() {
    int N;
    cin >> N;

    for (int i = 1; i <= N; i++) dp[i] = MAX;

    cout << solve(N) << endl;

    return 0;
}
