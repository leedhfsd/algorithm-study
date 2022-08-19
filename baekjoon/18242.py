import sys
input = sys.stdin.readline

row, col = map(int,input().split())
idx1, idx2 = -1, -1
board = []
for i in range(row):
  tmp = input().rstrip()
  if tmp.find("#.#") != -1:
    idx1 = i
  elif tmp.find("###") != -1:
    idx2 = i  
  board.append(list(tmp))

if idx1 < idx2 and idx1 != -1:
  print("UP")
elif idx1 > idx2 and idx1 != -1:
  print("DOWN")
else:
  idx1, idx2 = -1, -1
  for i in range(col):
    tmp = []
    for j in range(row):
      tmp.append(board[j][i])
    tmp = "".join(tmp)
    if tmp.find("#.#") != -1:
      idx1 = i
    elif tmp.find("###") != -1:
      idx2 = i
  
  if idx1 < idx2 and idx1 != -1:
    print("LEFT")
  elif idx1 > idx2 and idx1 != -1:
    print("RIGHT")
