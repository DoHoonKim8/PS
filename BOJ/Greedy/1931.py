import sys

n = int(sys.stdin.readline())
meetings = []
for _ in range(n):
    start, end = map(int, sys.stdin.readline().split())
    meetings.append((start, end))

meetings.sort(key=lambda x: (x[1], x[0]))
last = 0
answer = 0
for start, end in meetings:
    if start >= last:
        last = end
        answer += 1

print(answer)
