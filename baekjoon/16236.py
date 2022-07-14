import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
visited = [[0 for _ in range(n)] for _ in range(n)]
graph = []
fish = []
res = 0
size = 2
eat = 0
for i in range(n):
  graph.append(list(map(int, input().split())))

def check(i, j, size):
  global visited
  visited[i][j] = 1
  temp = []
  dx = [-1,0,0,1]
  dy = [0,-1,1,0]
  dq = deque([(i, j, 0)])

  while dq:
    x, y, dist = dq.popleft()
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
        if graph[nx][ny] == 0 or graph[nx][ny] == size:
          visited[nx][ny] = 1
          dq.append((nx, ny, dist+1))
        elif 1 <= graph[nx][ny] < size :
          temp.append((nx, ny, dist+1))
          visited[nx][ny] = 1
          dq.append((nx, ny, dist+1))
        
  
  temp.sort(key = lambda x: (-x[2], -x[0], -x[1]))
  visited = [[0 for _ in range(n)] for _ in range(n)]
  return temp

for i in range(n):
  flag = False
  if flag: break
  for j in range(n):
    if graph[i][j] == 9:
      graph[i][j] = 0
      x, y = i, j
      flag = True
      break

while True:
  fish = check(x, y, size)
  if len(fish) == 0: break

  eat += 1
  if size == eat:
    size += 1
    eat = 0
  x, y, dist = fish.pop()
  graph[x][y] = 0
  res += dist

print(res)
