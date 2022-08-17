import sys
input = sys.stdin.readline
n = int(input())
board = []
for _ in range(n):
  board.append(list(map(int,input().split())))

res = 0

def dfs(x, y, dir):
  global res
  if x == n-1 and y == n-1:
    res += 1
    return 0
  
  if dir == 0 or dir == 1:
    if y < n-1 and not board[x][y+1]:
      dfs(x, y+1, 0)
  
  if dir == 1 or dir == 2:
    if x < n-1 and not board[x+1][y]:
      dfs(x+1, y, 2)
  
  if x < n-1 and y < n-1:
    if not board[x+1][y+1] and not board[x][y+1] and not board[x+1][y]:
      dfs(x+1, y+1, 1)
    
dfs(0,1,0)
print(res)
