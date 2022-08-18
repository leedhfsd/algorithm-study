import sys
input = sys.stdin.readline

row, col = map(int,input().split())
board = [list(input().rstrip()) for _ in range(row)]
res = [[-1 for _ in range(col)] for _ in range(row)]

for i in range(row):
  tmp = board[i]
  idx = 0
  prev = 0
  while idx < col:
    tmp[idx] = board[i][idx]
    if tmp[idx] == "c":
      res[i][idx] = 0
      prev = "c"
      idx += 1
    elif tmp[idx] != "c" and prev == "c":
      res[i][idx] = res[i][idx-1] + 1
      idx += 1
    elif tmp[idx] != "c" and prev == 0:
      res[i][idx] = -1
      idx += 1

for i in range(len(res)):
  print(*res[i])
