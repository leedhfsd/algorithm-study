import sys
sys.setrecursionlimit(10**6)

row, col, n = map(int,input().split())
trash = []
visited = [[0 for _ in range(col)] for _ in range(row)]
board = [[0 for _ in range(col)] for _ in range(row)]

for i in range(n):
  a, b = map(int,input().split())
  trash.append((a-1,b-1))
  board[a-1][b-1] = 1
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = 0
def dfs(x,y):
  global res
  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if 0 <= nx < row and 0 <= ny < col and not visited[nx][ny] and board[nx][ny]:
      visited[nx][ny] = 1
      dfs(nx,ny)
      res += 1

for i in trash:
  x, y = i
  res = 1
  if not visited[x][y]:
    visited[x][y] = 1
    dfs(x,y)
    if res > ans:
      ans = res
  res = 1
print(ans)
