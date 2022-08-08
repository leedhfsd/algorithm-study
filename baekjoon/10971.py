#내풀이
from collections import defaultdict
import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
graph = defaultdict(list)
ans = sys.maxsize
for i in range(n):
  for j in range(n):
    if board[i][j] != 0:
      graph[i].append(j)

def dfs(start, cur, res, visit):
  global board, ans
  if visit == n:
    if board[cur][start] != 0:
      tmp = res + board[cur][start]
    else:
      return 0
    if tmp < ans:
      ans = tmp
    return 0

  for i in graph[cur]:
    dis = board[cur][i]
    if not visited[i] and dis + res < ans:
      visited[i] = 1
      dfs(start, i, res + dis, visit+1)
      visited[i] = 0

for i in range(n):
  visited = [0 for _ in range(n)]
  visited[i] = 1
  dfs(i, i, 0, 1)

print(ans)

#개선된 다른사람 풀이
#애초에 graph를 새로 만들 필요 없이 그냥 백트래킹 돌리면 됨
import sys
input = sys.stdin.readline

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
visited = [0 for _ in range(n)]
ans = sys.maxsize

def dfs(start, visit, res):
  global ans
  if start == 0 and visit != 0:
    if visit == n:
      if res < ans:
        ans = res
  
  for i in range(n):
    if board[start][i] != 0 and not visited[i] and res + board[start][i] < ans:
      visited[i] = 1
      dfs(i, visit+1, res + board[start][i])
      visited[i] = 0

dfs(0,0,0)
print(ans)
