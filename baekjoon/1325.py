import sys
from collections import defaultdict
from collections import deque
input = sys.stdin.readline

graph = defaultdict(list)
vertex, edge = map(int,input().split())
res = defaultdict(list)
ans = -sys.maxsize
for _ in range(edge):
  a, b = map(int,input().split())
  graph[b].append(a)

def bfs(start):
  global vertex, tmp
  visited = [0 for _ in range(vertex+1)]
  dq = deque([start])
  visited[start] = 1
  while dq:
    x = dq.popleft()
    for i in graph[x]:
      if not visited[i]:
        visited[i] = 1
        dq.append(i)
        tmp += 1

for i in range(1, vertex+1):
  tmp = 0
  bfs(i)
  res[tmp].append(i)
  if ans < tmp:
    ans = tmp
print(*res[ans])
