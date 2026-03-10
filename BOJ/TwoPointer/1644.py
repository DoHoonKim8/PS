import sys

n = int(sys.stdin.readline())
is_primes = [True for _ in range(n + 1)]
is_primes[0], is_primes[1] = False, False

for i in range(2, n + 1):
    if is_primes[i]:
        for j in range(2, n // i + 1):
            is_primes[i * j] = False

primes = []
for idx, is_prime in enumerate(is_primes):
    if is_prime:
        primes.append(idx)

if len(primes) == 0:
    print(0)
    exit(0)

left, right = len(primes) - 1, len(primes) - 1
partial_sum = primes[left]
answer = 0

while left >= 0 and right >= 0:
    if partial_sum == n:
        answer += 1
        left -= 1
        right -= 1
        if left >= 0:
            partial_sum += (primes[left] - primes[right + 1])
    elif partial_sum < n:
        left -= 1
        if left >= 0:
            partial_sum += primes[left]
    else:
        right -= 1
        if left > right:
            left = right
            if right >= 0:
                partial_sum = primes[right]
        else:
            partial_sum -= primes[right + 1]

print(answer)
