import sys
import copy
from collections import deque
input = sys.stdin.readline

def cw():
  global board, n
  one, two, three, four = deque([]), deque([]), deque([]), deque([])
  tmp = [[0 for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if i+j == n-1:
        one.append(board[i][j])
      if j == n//2:
        two.append(board[i][j])
      if i == j:
        three.append(board[i][j])
      if i == n//2:
        four.append(board[i][j])

  for i in range(n):
    for j in range(n):
      flag = False
      if i+j == n-1:
        tmp[i][j] = two.popleft()
        flag = True
      if j == n//2:
        tmp[i][j] = three.popleft()
        flag = True
      if i == j:
        tmp[i][j] = four.popleft()
        flag = True
      if i == n//2:
        tmp[i][j] = one.pop()
        flag = True
      if not flag:
        tmp[i][j] = board[i][j]
  board = copy.deepcopy(tmp)




def ccw():
  global board, n
  one, two, three, four = deque([]), deque([]), deque([]), deque([])
  tmp = [[0 for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      if i+j == n-1:
        one.append(board[i][j])
      if j == n//2:
        two.append(board[i][j])
      if i == j:
        three.append(board[i][j])
      if i == n//2:
        four.append(board[i][j])
  
  for i in range(n):
    for j in range(n):
      flag = False
      if i+j == n-1:
        tmp[i][j] = four.pop()
        flag = True
      if j == n//2:
        tmp[i][j] = one.popleft()
        flag = True
      if i == j:
        tmp[i][j] = two.popleft()
        flag = True
      if i == n//2:
        tmp[i][j] = three.popleft()
        flag = True
      
      if not flag:
        tmp[i][j] = board[i][j]

  board = copy.deepcopy(tmp)


tc = int(input())
for _ in range(tc):
  n, deg = map(int,input().split())
  board = [list(map(int,input().split())) for _ in range(n)]
  if deg > 0 and deg != 360:
    while deg // 45 > 0:
      cw()
      deg -= 45
 
  elif deg < 0 and deg != -360:
    while -deg // 45 > 0:
      ccw()
      deg += 45
  
  for i in range(n):
    print(*board[i])
