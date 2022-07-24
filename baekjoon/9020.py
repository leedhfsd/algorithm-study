import sys
input = sys.stdin.readline

is_prime = [1 for _ in range(10001)]

for i in range(2, 10001):
  if not is_prime[i]:
    continue
  j = i * i
  for j in range(j, 10001, i):
    is_prime[j] = 0
is_prime[0], is_prime[1] = 0, 0


n = int(input())
for _ in range(n):
  number = int(input())
  for i in range(number//2, 1, -1):
    if is_prime[i] and is_prime[number-i]:
      print(i, number-i)
      break
