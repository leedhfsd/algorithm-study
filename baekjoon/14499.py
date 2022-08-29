import sys
input = sys.stdin.readline

row, col, x, y, k = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(row)]
dir = list(map(int,input().split()))
move = [(0,1),(0,-1),(-1,0),(1,0)]
dice = [0,0,0,0,0,0]
front = 2
down = 1
right = 5

for i in range(len(dir)):
  (dx, dy) = move[dir[i]-1]
  nx = x + dx
  ny = y + dy
  if 0 <= nx < row and 0 <= ny < col:
    if board[nx][ny] != 0:
      if dir[i] == 1:
        down, right = right, abs(5-down)
        dice[down] = board[nx][ny]
        board[nx][ny] = 0
      elif dir[i] == 2:
        down, right = abs(5-right), down
        dice[down] = board[nx][ny]
        board[nx][ny] = 0
      elif dir[i] == 3:
        front, down = down, abs(5-front)
        dice[down] = board[nx][ny]
        board[nx][ny] = 0
      elif dir[i] == 4:
        front, down = abs(5-down) ,front
        dice[down] = board[nx][ny]
        board[nx][ny] = 0
    
    elif board[nx][ny] == 0:
      if dir[i] == 1:
        down, right = right, abs(5-down)
        board[nx][ny] = dice[down]
      elif dir[i] == 2:
        down, right = abs(5-right), down
        board[nx][ny] = dice[down]
      elif dir[i] == 3:
        front, down = down, abs(5-front)
        board[nx][ny] = dice[down]
      elif dir[i] == 4:
        front, down = abs(5-down) ,front
        board[nx][ny] = dice[down]
    x, y = nx, ny
    print(dice[abs(5-down)])
