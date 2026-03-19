import sys

string = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()

stack = []
for c in string:
    stack.append(c)
    if len(stack) >= len(bomb) and ''.join(stack[-len(bomb):]) == bomb:
        for _ in range(len(bomb)):
            stack.pop()

if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))
