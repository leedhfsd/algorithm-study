import sys
from collections import deque
import copy
input = sys.stdin.readline
row, col = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(row)]

dx = [-1,1,0,0]
dy = [0,0,-1,1]
t = 0
res = 0
#각 점마다 bfs 실시함. 격자 밖으로 나가면 지워야 되는 치즈임
#아닌거 따로 분류

def bfs(arr, p, q):
  global cand
  visited = [[0 for _ in range(col)] for _ in range(row)]
  dq = deque([(p,q)])
  visited[p][q] = 1
  flag = False
  while dq:
    x, y = dq.popleft()
    if flag:
      break
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if nx == 0 or nx == row-1 or ny == 0 or ny == col-1:
        flag = True
        break
      if 1 <= nx < row-1 and 1 <= ny < col-1 and not visited[nx][ny] and arr[nx][ny] != 1:
        visited[nx][ny] = 1
        dq.append((nx,ny))
  if flag:
    cand.append((p,q))

while True:
  t += 1
  cand = deque([])
  tmp = copy.deepcopy(board)
  for i in range(row):
    for j in range(col):
      if tmp[i][j] == 1:
        bfs(tmp, i, j)
  #공기 닿은 치즈 삭제
  for i in range(len(cand)):
    (x, y) = cand[i]
    tmp[x][y] = 0

  flag = False
  for i in range(row):
    if flag: break
    for j in range(col):
      if tmp[i][j] == 1:
        flag = True
        break
  if flag:
    board = tmp
  else:
    for i in range(row):
      for j in range(col):
        if board[i][j] == 1:
          res += 1
    print(t)
    print(res)
    break
