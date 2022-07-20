import sys
from collections import defaultdict
import heapq
input = sys.stdin.readline
INF = sys.maxsize

graph = defaultdict(list)
v, e = map(int,input().split())

for _ in range(e):
  a, b, dis = map(int, input().split())
  graph[a].append((b, dis))
  graph[b].append((a, dis))
v1, v2 = map(int, input().split())

def dijk(start):
  dist = [INF for _ in range(v+1)]
  dist[start] = 0
  visited = [0 for _ in range(v+1)]
  heap = []
  heapq.heappush(heap, (0, start))
  
  while heap:
    curr = heapq.heappop(heap)[1]
    while heap and visited[curr]:
      curr = heapq.heappop(heap)[1]
    if visited[curr]: break
    visited[curr] = 1
  
    for nxt, dis in graph[curr]:
      if dist[nxt] > dist[curr] + dis:
        dist[nxt] = dist[curr] + dis
        heapq.heappush(heap,(dist[nxt], nxt))
  return dist

dist_1 = dijk(1)
dist_v1 = dijk(v1)
dist_v2 = dijk(v2)

res = min(dist_1[v1] + dist_v1[v2] + dist_v2[v], dist_1[v2] + dist_v2[v1] + dist_v1[v])
if res >= INF: print(-1)
else: print(res)
