import sys

equation = list(sys.stdin.readline().split('-'))
answer = sum(map(int, equation[0].split('+')))
for partial in equation[1:]:
    partial_sum = sum(map(int, partial.split('+')))
    answer -= partial_sum

print(answer)
