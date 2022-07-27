import sys
input = sys.stdin.readline

n = int(input())
dp = [[0 for _ in range(n)] for _ in range(n)]
graph = [list(map(int,input().split())) for _ in range(n)]
dp[0][0] = 1
for i in range(n):
  for j in range(n):
    if i == n-1 and j == n-1: break
    move = graph[i][j]
    if i + move < n:
      dp[i+move][j] += dp[i][j]
    if j + move < n:
      dp[i][j+move] += dp[i][j]

print(dp[n-1][n-1])
