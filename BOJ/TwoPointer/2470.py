import sys

n = sys.stdin.readline()
liquids = sorted(list(map(int, sys.stdin.readline().split())))

left = 0
right = len(liquids) - 1

answer = [liquids[left], liquids[right]]
minimum = abs(liquids[left] + liquids[right])

while left < right:
    combined = liquids[left] + liquids[right]
    if abs(combined) < minimum:
        answer = [liquids[left], liquids[right]]
        minimum = abs(combined)
    if combined > 0:
        right -= 1
    elif combined < 0:
        left += 1
    else:
        break

print(answer[0], answer[1])
