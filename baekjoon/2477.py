from collections import defaultdict
import sys
input = sys.stdin.readline
board = defaultdict(list)

n = int(input())
tmp = []
for _ in range(6):
  dir, dis = map(int,input().split())
  board[dir].append(dis)
  tmp.append(dis)

row, col = 0, 0
s_row, s_col = 0, 0

for dir, dis in board.items():
  if len(board[dir]) == 1 and (dir == 1 or dir == 2):
    col = dis[0]
  elif len(board[dir]) == 1 and (dir == 3 or dir == 4):
    row = dis[0]

idx = tmp.index(col)
if tmp[(idx+1)%6] != row:
  s_row = row - tmp[(idx+1)%6]
elif tmp[(idx-1)%6] != row:
  s_row = row - tmp[(idx-1)%6]
idx = tmp.index(row)
if tmp[(idx+1)%6] != col:
  s_col = col - tmp[(idx+1)%6]
elif tmp[(idx-1)%6] != col:
  s_col = col - tmp[(idx-1)%6]

print(((row*col)-(s_row*s_col))*n)
