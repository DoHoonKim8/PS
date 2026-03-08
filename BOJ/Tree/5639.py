import sys

sys.setrecursionlimit(10**5)

data = list(map(int, sys.stdin.read().split()))

root = data[0]

def find_bigger(data, start, end):
    for i in range(start + 1, end):
        if data[i] > data[start]:
            return i
    return end

def postorder_traverse(data, start, end, postorder):
    if end <= start:
        return postorder
    right_start = find_bigger(data, start, end)
    postorder_traverse(data, start + 1, right_start, postorder)
    postorder_traverse(data, right_start, end, postorder)
    postorder.append(data[start])

postorder = []
postorder_traverse(data, 0, len(data), postorder)

print('\n'.join(map(str, postorder)))
