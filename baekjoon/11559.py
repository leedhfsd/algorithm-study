import copy
from collections import deque

def bfs(i,j,type,arr):
  global remove, visited
  remove_tmp = [(i,j)]
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  dq = deque([(i,j,type,1)])
  
  while dq:
    x, y, color, cnt = dq.popleft()

    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < 6 and 0 <= ny < 12 and not visited[nx][ny]:
        if arr[nx][ny] == color:
          visited[nx][ny] = 1
          remove_tmp.append((nx,ny))
          dq.append((nx,ny,color,cnt+1))

  if len(remove_tmp) >= 4:
    remove += remove_tmp

tmp = [list(input()) for _ in range(12)]
board = []
res = 0
for i in range(5,-1,-1):
  lis = [arr[i] for arr in tmp]
  board.append(lis)

while True:
  tmp = copy.deepcopy(board)
  visited = [[0 for _ in range(12)] for _ in range(6)]
  remove = []
  for i in range(6):
    for j in range(12):
      if tmp[i][j] != "." and not visited[i][j]:
        visited[i][j] = 1
        bfs(i,j,tmp[i][j],tmp)

  if len(remove) > 0:
    for x,y in remove:
      tmp[x][y] = "."
    for i in range(6):
      dot = ""
      not_dot = ""
      for j in range(12):
        if tmp[i][j] == ".":
          dot += "."
        elif tmp[i][j] != ".":
          not_dot += tmp[i][j]
      tmp[i] = list(dot+not_dot)
    board = tmp
  else:
    print(res)
    break
  res += 1
