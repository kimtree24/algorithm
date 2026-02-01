import sys
input = sys.stdin.readline

n = int(input().strip())

is_prime = [True for _ in range(n + 1)]
is_prime[0] = False
is_prime[1] = False

for i in range(2, int(n ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, n + 1, i):
            is_prime[j] = False

primes = []
for i in range(2, n + 1):
    if is_prime[i]:
        primes.append(i)

left, right = 0, 0
cur_sum = 0
ans = 0

while True:
    if cur_sum >= n:
        if cur_sum == n:
            ans += 1
        cur_sum -= primes[left]
        left += 1
    else:
        if right == len(primes):
            break
        cur_sum += primes[right]
        right += 1
print(ans)