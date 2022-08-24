import sys
from collections import deque
import copy
input = sys.stdin.readline

n, l, r = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(n)]
move = [(-1,0),(0,1),(1,0),(0,-1)]

def bfs(a,b,v_cnt):
  global visited,n,l,r
  dq = deque([(a,b)])
  res = board[a][b]
  cnt = 1
  while dq:
    x, y = dq.popleft()

    for i in range(4):
      nx = x + move[i][0]
      ny = y + move[i][1]

      if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
        if l <= abs(board[x][y]-board[nx][ny]) <= r:
          dq.append((nx,ny))
          visited[nx][ny] = v_cnt
          res += board[nx][ny]
          cnt += 1
  if cnt > 1:
    for i in range(n):
      for j in range(n):
        if visited[i][j] == v_cnt:
          board[i][j] = res // cnt

res = 0
while True:
  visited = [[0 for _ in range(n)] for _ in range(n)]
  v_cnt = 1
  for i in range(n):
    for j in range(n):
      if not visited[i][j]:
        visited[i][j] = v_cnt
        bfs(i,j,v_cnt)
        v_cnt += 1

  if visited[n-1][n-1] == n*n:
    print(res)
    break
  res += 1
