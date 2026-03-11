import sys
from collections import defaultdict

word = sys.stdin.readline().lower().strip()

count = defaultdict(int)
for alphabet in word:
    count[alphabet] += 1

answer = ''
sorted_count = sorted(count.items(), key=lambda x: -x[1])

if len(sorted_count) > 1 and sorted_count[0][1] == sorted_count[1][1]:
    answer = '?'
else:
    answer = sorted_count[0][0].upper()

print(answer)
