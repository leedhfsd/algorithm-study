import sys
from collections import defaultdict
from collections import deque
input = sys.stdin.readline

v, e, dis, start = map(int,input().split())
graph = defaultdict(list)
for _ in range(e):
  a, b = map(int,input().split())
  graph[a].append(b)

def bfs(start):
  global v, dis
  res = []
  visited = [0 for _ in range(v+1)]
  dq = deque([(start, 0)])
  visited[start] = 1

  while dq:
    cur, cnt = dq.popleft()
    if cnt == dis:
      res.append(cur)
      continue
    for i in graph[cur]:
      if not visited[i]:
        visited[i] = 1
        dq.append((i, cnt+1))
  
  return res

ans = bfs(start)
ans.sort()
if len(ans) == 0:
  print(-1)
else:
  for i in ans:
    print(i)
