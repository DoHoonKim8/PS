def solution(arr):
    answer = -1
    dp_len = len(arr) // 2 + 1
    dp = [[[0, 0]] * dp_len for _ in range(dp_len)]
    for i in range(dp_len):
        dp[i][i] = [int(arr[2 * i]), int(arr[2 * i])]

    for i in range(1, dp_len):
        for j in range(0, dp_len - i):
            interm = []
            for k in range(0, i):
                if arr[2 * (j + k) + 1] == "+":
                    interm.append(dp[j][j + k][0] + dp[j + k + 1][j + i][0])
                    interm.append(dp[j][j + k][0] + dp[j + k + 1][j + i][1])
                    interm.append(dp[j][j + k][1] + dp[j + k + 1][j + i][0])
                    interm.append(dp[j][j + k][1] + dp[j + k + 1][j + i][1])
                else:
                    interm.append(dp[j][j + k][0] - dp[j + k + 1][j + i][0])
                    interm.append(dp[j][j + k][0] - dp[j + k + 1][j + i][1])
                    interm.append(dp[j][j + k][1] - dp[j + k + 1][j + i][0])
                    interm.append(dp[j][j + k][1] - dp[j + k + 1][j + i][1])
            low = min(interm)
            high = max(interm)
            dp[j][j + i] = [low, high]
    answer = dp[0][dp_len - 1][1]

    return answer
