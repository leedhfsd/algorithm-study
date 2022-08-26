import sys
from collections import deque
input = sys.stdin.readline

row, col, v = map(int,input().split())
x, y = map(int,input().split())
dx = [-1,1,0,0]
dy = [0,0,-1,1]
board = [list(map(int,input().split())) for _ in range(row)]
v_board = [[sys.maxsize for _ in range(col)] for _ in range(row)]
visited = [[0 for _ in range(col)] for _ in range(row)]
height, time = 0, 0
vc_set = set([])

vc = deque([])
for _ in range(v):
  vx, vy, vt = map(int,input().split())
  vc.append([vx-1, vy-1, vt])
  v_board[vx-1][vy-1] = vt
  vc_set.add((vx-1, vy-1))
dq = deque([(x-1,y-1,0)])
visited[x-1][y-1] = 1

#화산 처리
while vc:
  vx, vy, vt = vc.popleft()
  for i in range(4):
    nvx = vx + dx[i]
    nvy = vy + dy[i]

    if 0 <= nvx < row and 0 <= nvy < col and v_board[nvx][nvy] > vt+1 :
      v_board[nvx][nvy] = vt + 1
      vc.append((nvx, nvy, vt+1))

while dq:
  x, y, t = dq.popleft()
  if board[x][y] > height:
    height = board[x][y]
    time = t
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny] and (nx,ny) not in vc_set:
      if v_board[nx][ny] > t+1:
        dq.append((nx,ny,t+1))
        visited[nx][ny] = 1

print(height, time)
