import sys
import math
input = sys.stdin.readline

n = int(input())
dp = [sys.maxsize for _ in range(n+1)]

for i in range(1, n+1):
  if i == int(math.sqrt(i)) * int(math.sqrt(i)):
    dp[i] = 1
    continue
  else:
    for j in range(1, int(math.sqrt(i))+1):
      if dp[i] > dp[i-j*j] + 1:
        dp[i] = dp[i-j*j] + 1

print(dp[n])
