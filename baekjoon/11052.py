import sys
input = sys.stdin.readline

n = int(input())
price = [0] + list(map(int,input().split()))
dp = [0 for _ in range(n+1)]

for i in range(1,n+1):
  dp[i] = price[i]
  for j in range(1,i//2+1):
    if dp[i] < dp[i-j] + dp[j]:
      dp[i] = dp[i-j] + dp[j]

print(dp[n])
