def solution(s):
    answer = 0

    chars = list(s)
    if len(chars) == 1:
        return 1

    dp = [[] for _ in range(len(chars))]
    dp[0] = [1]
    if chars[0] == chars[1]:
        dp[1] = [1, 2]
    else:
        dp[1] = [1]
    for i in range(2, len(chars)):
        dp[i].append(1)
        for partial_len in dp[i - 1]:
            if partial_len + 1 <= i and chars[i - partial_len - 1] == chars[i]:
                dp[i].append(partial_len + 2)
        if chars[i] == chars[i - 1]:
            dp[i].append(2)

    answer = max([max(dp[i]) for i in range(len(dp))])
    return answer
