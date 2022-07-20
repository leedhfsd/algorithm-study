import sys
import math
input = sys.stdin.readline

n = int(input())
m = int(input())
prime = []

for i in range(n, m+1):
  flag = False
  for j in range(2, int(math.sqrt(i))+1):
    if i % j  == 0:
      flag = True
      break
  if not flag:
    prime.append(i)

if prime:
  if prime[0] == 1: prime.pop(0)
  if prime:
    print(sum(prime))
    print(prime[0])
  else:
    print(-1)
else:
  print(-1)
