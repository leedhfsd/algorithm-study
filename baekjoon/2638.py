import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
res = 0
flag = False

def check():
  visited = [[0 for _ in range(m)] for _ in range(n)]
  dq = deque([(0, 0)])
  visited[0][0] = 1

  while dq:
    x, y = dq.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]
      
      if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
        if graph[nx][ny] >= 1:
          graph[nx][ny] += 1
        elif graph[nx][ny] == 0:
          visited[nx][ny] = 1
          dq.append((nx, ny))
  
  for i in range(n):
    for j in range(m):
      if graph[i][j] >= 3:
        graph[i][j] = 0
      elif graph[i][j] == 2:
        graph[i][j] = 1
def is_melt():
  for i in range(n):
    for j in range(m):
      if graph[i][j] == 1:
        return False
  return True

while not flag:
  check()
  res += 1
  flag = is_melt()

print(res)
