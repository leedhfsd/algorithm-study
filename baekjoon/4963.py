import sys
from collections import deque
input = sys.stdin.readline
dx = [-1,1,0,0,-1,-1,1,1]
dy = [0,0,-1,1,-1,1,-1,1]

def bfs(i, j, num):
  dq = deque([(i, j)])
  visited[i][j] = num

  while dq:
    x, y = dq.popleft()
    for i in range(8):
      nx = x + dx[i]
      ny = y + dy[i]    
      if 0 <= nx < h and 0 <= ny < w and not visited[nx][ny] and graph[nx][ny]:
        visited[nx][ny] = num
        dq.append((nx, ny))

while True:
  w, h = map(int,input().split())
  if w == 0 and h == 0: break
  graph = [list(map(int,input().split())) for _ in range(h)]
  visited = [[0 for _ in range(w)] for _ in range(h)]

  num = 2
  for i in range(h):
    for j in range(w):
      if graph[i][j] == 1 and not visited[i][j]:
        bfs(i,j,num)
        num = num + 1
      elif graph[i][j] == 0:
        visited[i][j] = 1
  res = 0
  for i in range(h):
    for j in range(w):
      res = max(res, visited[i][j])

  print(res-1)

  
