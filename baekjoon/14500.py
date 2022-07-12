#백트래킹
#무조건 다시 풀어야하는 문제 
import sys
from collections import deque
input = sys.stdin.readline
n, m = map(int, input().split())
graph = []
ans = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for _ in range(n):
  graph.append(list(map(int, input().split())))
visited = [[0 for _ in range(m)] for _ in range(n)]

def dfs(x, y, res, cnt):
  global ans
  #모든값이 최대값이여도 현재 최대값을 넘지 못하면 건너 뛴다. 매우 중요
  if ans >= 1000 * (4 - cnt) + res:
    return
  if cnt == 4: 
    ans = max(ans, res)
    return
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx < 0 or nx >= n or ny < 0 or ny >= m: continue
    if not visited[nx][ny]:
      if cnt == 2:
        visited[nx][ny] = 1
        dfs(x, y, res+graph[nx][ny], cnt+1)
        visited[nx][ny] = 0
      visited[nx][ny] = 1
      dfs(nx, ny, res+graph[nx][ny], cnt+1)
      visited[nx][ny] = 0

for i in range(n):
  for j in range(m):
    visited[i][j] = 1
    dfs(i, j, graph[i][j], 1)
    visited[i][j] = 0
print(ans)
