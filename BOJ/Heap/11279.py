import sys
import heapq

n = int(sys.stdin.readline())
h = []
answer = []
for _ in range(n):
    inp = int(sys.stdin.readline())
    if inp == 0:
        if len(h) == 0:
            answer.append(0)
        else:
            answer.append(-heapq.heappop(h))
    else:
        heapq.heappush(h, -inp)

print('\n'.join(map(str, answer)))
