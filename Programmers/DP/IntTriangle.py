def solution(triangle):
    answer = 0
    max_partial_sum = []
    max_partial_sum.append(triangle[0])
    for i in range(1, len(triangle)):
        partial_sum = []
        partial_sum.append(max_partial_sum[i-1][0] + triangle[i][0])
        for j in range(1, i):
            partial_sum.append(max(max_partial_sum[i-1][j - 1], max_partial_sum[i-1][j]) + triangle[i][j])
        partial_sum.append(max_partial_sum[i-1][i - 1] + triangle[i][i])
        if i == len(triangle) - 1:
            answer = max(partial_sum)
            break
        max_partial_sum.append(partial_sum)

    return answer
