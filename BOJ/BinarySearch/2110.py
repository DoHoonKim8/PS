import sys

n, c = map(int, sys.stdin.readline().split())
xs = []
for _ in range(n):
    xs.append(int(sys.stdin.readline()))

xs.sort()

low = 1
high = xs[-1] - xs[0]
answer = 0

while low <= high:
    mid = (low + high) // 2
    num_houses = 1
    last_x = xs[0]
    for next_x in xs[1:]:
        if next_x - last_x < mid:
            continue
        else:
            num_houses += 1
            last_x = next_x
    if num_houses >= c:
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)
