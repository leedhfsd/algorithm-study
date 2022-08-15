#dfs
from collections import deque
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = -1
visited = [[0 for _ in range(m)] for _ in range(n)]

def dfs(x, y, word):
  global ans
  if ans < len(word):
    ans = len(word)

  for i in range(4):
    nx = x + dx[i]
    ny = y + dy[i]

    if board[nx][ny] in word: continue
    
    if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
      visited[nx][ny] = 1
      dfs(nx, ny, word+board[nx][ny])
      visited[nx][ny] = 0

dfs(0,0,board[0][0])
print(ans)


# bfs set을 쓸 수 있는 이유는 중복된 글자가 있는지 없는지 체크하는 부분이 방문처리 역할을 하기 때문
from collections import deque
n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
ans = -1
def bfs(i,j):
  global ans
  dq = set([(i, j, 1, board[i][j])])

  while dq:
    x, y, res, word = dq.pop()
    if res > ans:
      ans = res
    for i in range(4):
      nx = x + dx[i]
      ny = y + dy[i]

      if 0 <= nx < n and 0 <= ny < m:
        if board[nx][ny] not in word:
          dq.add((nx, ny, res+1, word+board[nx][ny]))
        
bfs(0,0)
print(ans)
