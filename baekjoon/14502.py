import sys 
from collections import deque
import copy
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int,input().split())) for _ in range(n)]
virus = []
dx = [-1,1,0,0]
dy = [0,0,-1,1]
for i in range(n):
  for j in range(m):
    if graph[i][j] == 2:
      virus.append((i, j))

def bfs(board):
  temp = copy.deepcopy(board)
  res = 0
  dq = deque([])
  for i in virus:
    dq.append(i)
  
  while dq:
    x, y = dq.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m:
        if temp[nx][ny] == 1:
          continue
        if temp[nx][ny] == 0:
          temp[nx][ny] = 2
          dq.append((nx, ny))
  for i in range(n):
    for j in range(m):
      if temp[i][j] == 0:
        res += 1
  return res

def recursion(level):
  count = 0
  if level == 3:
    return bfs(graph)
  
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 0:
        graph[i][j] = 1
        count = max(count, recursion(level+1))
        graph[i][j] = 0
  
  return count

print(recursion(0))
