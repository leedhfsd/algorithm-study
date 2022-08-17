import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline

v, e, x = map(int,input().split())
graph = defaultdict(list)
for _ in range(e):
  a, b, dis = map(int,input().split())
  graph[a].append((b, dis))

def dijk(start):
  visited = [0 for _ in range(v+1)]
  dist = [sys.maxsize for _ in range(v+1)]
  dist[start] = 0
  heap = []
  heapq.heappush(heap, (0, start))

  while heap:
    cur = heapq.heappop(heap)[1]
    while len(heap) != 0 and visited[cur]:
      cur = heapq.heappop(heap)[1]
    if visited[cur]:
      break
    visited[cur] = 1
    for i in graph[cur]:
      nxt, dis = i
      if dist[nxt] > dist[cur] + dis:
        dist[nxt] = dist[cur] + dis
        heapq.heappush(heap, (dist[nxt], nxt))
  
  return dist

start_x = dijk(x)
ans = 0

for i in range(1, v+1):
  tmp = dijk(i)
  res = tmp[x] + start_x[i]
  if ans < res:
    ans = res
  
print(ans)
