def solution(money):
    answer = 0
    if (len(money) == 3):
        answer = max(money)
        return answer

    dp = [[0] * len(money), [0] * len(money)]
    for i in range(len(money) - 1):
        if i < 2:
            dp[0][i] = max(money[:i + 1])
        else:
            dp[0][i] = max(dp[0][i - 1], money[i] + dp[0][i - 2])

    for i in range(1, len(money) - 1):
        if i < 3:
            dp[1][i] = max(money[1:i + 1])
        else:
            dp[1][i] = max(dp[1][i - 1], money[i] + dp[1][i - 2])

    last = len(money) - 1
    answer = max(money[last] + dp[1][last - 2], dp[0][last - 1])
    return answer
