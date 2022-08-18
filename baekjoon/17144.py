import sys
input = sys.stdin.readline
row, col, t = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(row)]
cleaner = []

for i in range(row):
  if board[i][0] == -1:
    cleaner.append(i)
    cleaner.append(i+1)
    break
  

def dust_spread():
  dx = [-1,1,0,0]
  dy = [0,0,-1,1]
  tmp = [[0 for _ in range(col)] for _ in range(row)]

  for i in range(row):
    for j in range(col):
      if board[i][j] > 0:
        res = 0
        for k in range(4):
          nx = i + dx[k]
          ny = j + dy[k]
          if 0 <= nx < row and 0 <= ny < col and board[nx][ny] != -1:
            tmp[nx][ny] += board[i][j] // 5
            res += board[i][j] // 5
        board[i][j] -= res

  for i in range(row):
    for j in range(col):
      board[i][j] += tmp[i][j]

def upper():
  dx = [0,-1,0,1]
  dy = [1,0,-1,0]
  x, y = cleaner[0], 1
  pos = 0
  prev = 0

  while True:
    if x == cleaner[0] and y == 0:
      break
    nx = x + dx[pos]
    ny = y + dy[pos]
    if 0 > nx or nx >= row or 0 > ny or ny >= col: 
      pos += 1
      continue
    board[x][y], prev = prev, board[x][y]
    x = nx
    y = ny

def lower():
  dx = [0,1,0,-1]
  dy = [1,0,-1,0]
  x, y = cleaner[1], 1
  pos = 0
  prev = 0

  while True:
    if x == cleaner[1] and y == 0:
      break
    nx = x + dx[pos]
    ny = y + dy[pos]
    if 0 > nx or nx >= row or 0 > ny or ny >= col: 
      pos += 1
      continue
    board[x][y], prev = prev, board[x][y]
    x = nx
    y = ny
  
while t > 0:
  dust_spread()
  upper()
  lower()
  t -= 1

res = 0
for i in range(row):
  for j in range(col):
    if board[i][j] > 0:
      res += board[i][j]

print(res)
