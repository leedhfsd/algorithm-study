import sys
from collections import defaultdict
from collections import deque
input = sys.stdin.readline

v = int(input())
e = int(input())
graph = defaultdict(list)
res = 0
for _ in range(e):
  a, b = map(int,input().split())
  graph[a].append(b)
  graph[b].append(a)

def bfs(start):
  global v, res
  visited = [0 for _ in range(v+1)]
  dq = deque([(start, 0)])
  visited[1] = 1

  while dq:
    cur, cnt = dq.popleft()
    if cnt == 2:
      continue
      
    for i in graph[cur]:
      if not visited[i]:
        visited[i] = 1
        dq.append((i, cnt+1))
        res += 1
  
  print(res)

bfs(1)
