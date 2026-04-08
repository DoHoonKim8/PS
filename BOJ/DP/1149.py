import sys

n = int(sys.stdin.readline())
costs = []
for _ in range(n):
    r, g, b = map(int, sys.stdin.readline().split())
    costs.append((r, g, b))

dp = [costs[0]]
for i in range(1, n):
    r_i = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][0]
    g_i = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
    b_i = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]
    dp.append((r_i, g_i, b_i))

print(min(dp[-1]))
