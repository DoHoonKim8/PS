import sys

n, m = map(int, sys.stdin.readline().split())
a = list(map(int, sys.stdin.readline().split()))

left, right = 0, 0
partial_sum = a[0]
answer = 0

while left < len(a) and right < len(a):
    if partial_sum < m:
        right += 1
        if right < len(a):
            partial_sum += a[right]
    elif partial_sum == m:
        answer += 1
        left += 1
        right += 1
        if right < len(a):
            partial_sum += (a[right] - a[left - 1])
    else:
        left += 1
        if right < left:
            right = left
            if left < len(a):
                partial_sum = a[left]
        else:
            partial_sum -= a[left - 1]

print(answer)
