import sys
input = sys.stdin.readline

direct = [(0,1),(-1,0),(0,-1),(1,0)]
board = [[0 for _ in range(101)] for _ in range(101)]

n = int(input())
res= 0
for _ in range(n):
  y, x, d, gen = map(int,input().split())
 
  board[x][y] = 1
  curve = [d]
  for i in range(gen):
    for j in range(len(curve)-1, -1, -1):
      curve.append((curve[j]+1) % 4)
  
  for i in range(len(curve)):
    dx, dy = direct[curve[i]]
    x = x + dx
    y = y + dy

    board[x][y] = 1

for i in range(100):
  for j in range(100):
    if board[i][j+1] and board[i+1][j] and board[i+1][j+1] and board[i][j]:
      res += 1  

print(res)
