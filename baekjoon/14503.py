import sys
from collections import deque
input = sys.stdin.readline
r, c = map(int,input().split())
x, y, d = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(r)]

def bfs(i,j,d):
  dir = [(-1,0),(0,1),(1,0),(0,-1)]
  res = 1
  dq = deque([(i,j,d)])

  while dq:
    x, y, d = dq.popleft()
    board[x][y] = 2
    tmp = d
    for i in range(4):
      tmp = (tmp-1) % 4
      nx, ny = x + dir[tmp][0], y + dir[tmp][1]

      if 0 <= nx < r and 0 <= ny < c and board[nx][ny] == 0:
        res += 1
        dq.append((nx, ny, tmp))
        break
      
      elif i == 3:
        tmp = (tmp+2)%4
        nx, ny = x + dir[tmp][0], y + dir[tmp][1]
        if board[nx][ny] == 1:
          print(res)
          break
        else:
          dq.append((nx, ny, d))

bfs(x,y,d)
