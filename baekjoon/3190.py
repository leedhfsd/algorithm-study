import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
m = int(input())
board = [[0 for _ in range(n+1)] for _ in range(n+1)]
apple = set([tuple(map(int,input().split())) for _ in range(m)])
l = int(input())
dir = [input().rstrip().split() for _ in range(l)]
move = [(-1,0),(0,1),(1,0),(0,-1)]
d = 1
t = 0
head_x, head_y = 1, 1
tail_x, tail_y = 1, 1
board[1][1] = 1
visited = [0 for _ in range(len(dir))]
dq = deque([(1,1)])
while True:
  t += 1
  head_x, head_y = head_x + move[d][0], head_y + move[d][1]
  if 1 > head_x or 1 > head_y or n < head_x or n < head_y or board[head_x][head_y]:
    print(t)
    break

  if (head_x, head_y) in apple:
    apple.remove((head_x,head_y))
    board[head_x][head_y] = 1
    dq.append((head_x,head_y))
  else:
    board[head_x][head_y] = 1
    dq.append((head_x,head_y))
    tx, ty = dq.popleft()
    board[tx][ty] = 0

  
  for i in range(len(dir)):
    if int(dir[i][0]) > t:
      break
    if not visited[i]:
      if int(dir[i][0]) == t:
        if dir[i][1] == "D":
          d = (d+1)%4
        elif dir[i][1] == "L":
          d = (d-1)%4
        visited[i] = 1
