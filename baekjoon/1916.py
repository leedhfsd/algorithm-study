import sys
import heapq
from collections import defaultdict
input = sys.stdin.readline
INF = sys.maxsize

vertex = int(input())
edge = int(input())

visited = [0 for _ in range(vertex+1)]
dist = [INF for _ in range(vertex+1)]
graph = defaultdict(list)
heap = []

for i in range(edge):
  start, end, weight = map(int, input().split())
  graph[start].append((end, weight))

start, end = map(int, input().split())
dist[start] = 0
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
      heapq.heappush(heap, (dist[nxt], nxt))
  
print(dist[end])
