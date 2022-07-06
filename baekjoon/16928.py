import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
ladder = []
snake = []
pos = 1
deque = deque([(1, 0)])
for i in range(n+m):
  start, end = map(int, input().split())
  if i < n:
    ladder.append([start, end])
  else:
    snake.append([start, end])
ladder.sort()
snake.sort()

def bfs():
  visited = [0 for _ in range(101)]
  visited[1] = 1
  ans = sys.maxsize
  ladder_start = [i[0] for i in ladder]
  snake_start = [i[0] for i in snake]
  
  while deque:
    x, count = deque.pop()
    if x == 100:
        return count
    
    for i in range(1,7):
      nx = x + i
      if nx > 100:
        continue
      if visited[nx] == 0:
        if nx in ladder_start:
          visited[nx] = 1
          nx = ladder[ladder_start.index(nx)][1]
          deque.appendleft((nx, count+1))
        elif nx in snake_start:
          visited[nx] = 1
          nx = snake[snake_start.index(nx)][1]
          deque.appendleft((nx, count+1))
        else:
          visited[nx] = 1
          deque.appendleft((nx, count+1))
  return ans
print(bfs())
