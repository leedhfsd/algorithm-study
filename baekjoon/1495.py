#2차원 배열 활용, dp[i][j]에서 i는 v의 인덱스, j는 볼륨
# dp[i][j] == 1인 경우는 i번째 순서에서 j의 볼륨이라는 것
# dfs로 풀면 메모리 초과 나옴.

from collections import deque
n, s, m = map(int,input().split())
v = [0] + list(map(int,input().split()))
dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
dp[0][s] = 1
flag = False

for i in range(1, n+1):
  for j in range(m+1):
    if dp[i-1][j] == 1:
      if 0 <= j + v[i] <= m:
        dp[i][j+v[i]] = 1
      if 0 <= j - v[i] <= m:
        dp[i][j-v[i]] = 1

for j in range(m, -1, -1):
  if dp[n][j] == 1:
    print(j)
    flag = True
    break

if not flag:
  print(-1)
