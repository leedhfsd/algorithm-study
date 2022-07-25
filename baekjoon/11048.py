import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
graph = [[0 for _ in range(m+2)] for _ in range(n+2)]
dp = [[0 for _ in range(m+2)] for _ in range(n+2)]

for i in range(1,n+1):
  graph[i][1:m+1] = list(map(int,input().split()))

for i in range(1, n+1):
  for j in range(1, m+1):
    dp[i][j] = max(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + graph[i][j]

print(dp[n][m])
