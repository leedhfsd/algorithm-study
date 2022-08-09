import sys
input = sys.stdin.readline

board = [list(map(int,input().split())) for _ in range(5)]
removed = []
for i in range(5):
  removed += list(map(int,input().split()))

def check(arr):
  res = 0
  for i in range(5):
    if arr[i][:] == [0,0,0,0,0]:
      res += 1
  for i in range(5):
    if list(zip(*arr))[i] == (0,0,0,0,0):
      res += 1
  if [arr[0][0], arr[1][1], arr[2][2], arr[3][3], arr[4][4]] == [0,0,0,0,0]:
    res += 1
  if [arr[0][4], arr[1][3], arr[2][2], arr[3][1], arr[4][0]] == [0,0,0,0,0]:
    res += 1
  return res

for i in range(25):
  inp = removed[i]
  for j in range(5):
    for k in range(5):
      if board[j][k] == inp:
        board[j][k] = 0
        cnt = check(board)
        if cnt >= 3:
          print(i+1)
          exit(0)
