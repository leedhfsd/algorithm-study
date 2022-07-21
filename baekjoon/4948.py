import sys
input = sys.stdin.readline

is_prime = [1 for _ in range(123456*2+1)]
is_prime[0], is_prime[1] = 0, 0
for i in range(2,123456*2+1):
  if not is_prime[i]: continue
  j = i*i
  for j in range(j,123456*2+1,i):
    is_prime[j] = 0

while True:
  n = int(input())
  if n == 0:
    break
  print(sum(is_prime[n+1:2*n+1]))
  
