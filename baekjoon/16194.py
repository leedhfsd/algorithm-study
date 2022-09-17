import sys
n = int(input())
cost = [0] + list(map(int,input().split()))
dp = [0 for _ in range(n+1)]
for i in range(1,n+1):
  res = sys.maxsize
  tmp = sys.maxsize
  for j in range(1, n+1):
    if i-j >= 0:
      tmp = dp[i-j] + cost[j]
      if res > tmp:
        res = tmp
  dp[i] = res

print(dp[n])
