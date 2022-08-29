board = []
blank = []
for i in range(9):
  tmp = list(map(int,input().split()))
  for j in range(len(tmp)):
    if tmp[j] == 0:
      blank.append((i,j))
  board.append(tmp)
zero = len(blank)

def use_this(x, y):
  res = set([0,1,2,3,4,5,6,7,8,9])
  row = set(board[x])
  col = set([arr[y] for arr in board])
  nine = set([])
  x_idx = x - x % 3
  y_idx = y - y % 3

  for i in range(x_idx, x_idx+3):
    for j in range(y_idx, y_idx+3):
      nine.add(board[i][j])
  res = res - (row | col | nine)
  return list(res)

def recursion(n):
  if n == zero:
    for i in range(9):
      print(*board[i])
    exit(0)
  else:
    x, y = blank[n]
    cand = use_this(x,y)
    for num in cand:
      board[x][y] = num
      recursion(n+1)
      board[x][y] = 0
    
recursion(0)
  
