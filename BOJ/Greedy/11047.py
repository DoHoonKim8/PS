import sys

n, k = map(int, sys.stdin.readline().split())
coins = []
for _ in range(n):
    coins.append(int(sys.stdin.readline()))

if len(coins) == 1:
    print(k)
    exit(0)

biggest_coin = 0
next_coins = coins[1:]
next_coins.append(sys.maxsize)
for i, (a, b) in enumerate(zip(coins, next_coins)):
    if a <= k and k < b:
        biggest_coin = i
        break

num_coins = 0
rem = k
for i in range(biggest_coin, -1, -1):
    num_coins += rem // coins[i]
    rem = rem % coins[i]

print(num_coins)
