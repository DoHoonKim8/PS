import sys

n = sys.stdin.readline()
liquids = list(map(int, sys.stdin.readline().split()))

acids = sorted(filter(lambda x: x >= 0, liquids))
acalis = sorted(filter(lambda x: x < 0, liquids))

if len(acids) == 0:
    print(acalis[-2], acalis[-1])
    exit(0)
if len(acalis) == 0:
    print(acids[0], acids[1])
    exit(0)

answer = []
minimum = 2000000000
if len(acids) >= 2:
    if minimum > abs(acids[0] + acids[1]):
        minimum = abs(acids[0] + acids[1])
        answer = [acids[0], acids[1]]
if len(acalis) >= 2:
    if minimum > abs(acalis[-1] + acalis[-2]):
        minimum = abs(acalis[-1] + acalis[-2])
        answer = [acalis[-1], acalis[-2]]

for acid in acids:
    low = 0
    high = len(acalis) - 1
    while low <= high:
        mid = (low + high) // 2
        combined = acid + acalis[mid]
        if abs(combined) > minimum:
            if combined > 0:
                high = mid - 1
            else:
                low = mid + 1
        else:
            minimum = abs(combined)
            answer = [acalis[mid], acid]
            if combined > 0:
                high = mid - 1
            else:
                low = mid + 1

print(answer[0], answer[1])
