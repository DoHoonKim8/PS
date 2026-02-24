import sys

def solution():
    n = int(sys.stdin.readline())
    budgets = list(map(int, sys.stdin.readline().split()))
    total = int(sys.stdin.readline())

    answer = 0
    low = 0
    high = total
    while low <= high:
        mid = (low + high) // 2
        sum = 0
        for budget in budgets:
            sum += min(budget, mid)
        if sum <= total:
            answer = max(map(lambda b: min(b, mid), budgets))
            low = mid + 1
        else:
            high = mid - 1
    return answer

print(solution())