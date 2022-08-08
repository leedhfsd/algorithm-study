import sys
input = sys.stdin.readline

n, k = map(int,input().split())
item = [(-1,-1)]
dp = [[0 for _ in range(k+1)] for _ in range(n+1)]

for _ in range(n):
  w, v = map(int,input().split())
  item.append((w,v))

for i in range(1, n+1):
  for j in range(1, k+1):
    w, v = item[i]
    if j < w:
      dp[i][j] = dp[i-1][j]
    else:
      dp[i][j] = max(dp[i-1][j-w] + v, dp[i-1][j])

print(dp[n][k])
