import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

a.sort()
for i in range(m):
    answer = 0
    low = 0
    high = len(a) - 1
    while low <= high:
        mid = (low + high) // 2
        if b[i] == a[mid]:
            answer = 1
            break
        if b[i] < a[mid]:
            high = mid - 1
        elif b[i] > a[mid]:
            low = mid + 1
    print(answer)
