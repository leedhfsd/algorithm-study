import sys
input = sys.stdin.readline

n = int(input())
dp = [0 for _ in range(100001)]
dp[0], dp[1] = 1, 3
for i in range(2, n+1):
  dp[i] = (2*dp[i-1] + dp[i-2]) % 9901

print(dp[n])
