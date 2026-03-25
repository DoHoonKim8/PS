def max_reward(n: int, tasks: list[tuple[int, int]]) -> int:
    """
    tasks: [(deadline, reward), ...]
    return: 최대 보상 합
    """
    tasks.sort(key=lambda x: -x[1])
    slots = [0] * n
    for deadline, reward in tasks:
        for t in range(deadline, 0, -1):
            if slots[t - 1] == 0:
                slots[t - 1] = reward
                break

    return sum(slots)

import sys

n = int(sys.stdin.readline())
tasks = []
for _ in range(n):
    deadline, reward = map(int, sys.stdin.readline().split())
    tasks.append((deadline, reward))

print(max_reward(n, tasks))
