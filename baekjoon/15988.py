import sys
input = sys.stdin.readline

tc = int(input())
mod = 1000000009
dp = [0 for _ in range(1000001)]
dp[1], dp[2], dp[3] = 1, 2, 4
for i in range(4,1000001):
    dp[i] = (dp[i-3] + dp[i-2] + dp[i-1]) % mod

for _ in range(tc):
  n = int(input())
  print(dp[n])
