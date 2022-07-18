import sys
import heapq
from collections import defaultdict
INF = sys.maxsize
input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())
visited = [0 for _ in range(v+1)]
dist = [INF for _ in range(v+1)]
dist[start] = 0
graph = defaultdict(list)
heap = []
heapq.heappush(heap, (0, start))

for i in range(e):
  start, end, weight = map(int,input().split())
  graph[start].append((end, weight))

while heap:
  curr = heapq.heappop(heap)[1]
  while heapq and visited[curr]:
    curr = heapq.heappop(heap)[1]

  if visited[curr]: break
  visited[curr] = 1

  for i in graph[curr]:
    nxt, dis = i
    if dist[nxt] > dist[curr] + dis:
      dist[nxt] = dist[curr] + dis
      heapq.heappush(heap, (dist[nxt], nxt))

for i in range(1, v+1):
  if dist[i] == INF:
    print("INF")
  else:
    print(dist[i])
