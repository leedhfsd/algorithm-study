import sys
import heapq
from collections import defaultdict
from collections import deque
input = sys.stdin.readline
INF = sys.maxsize

vertex = int(input())
graph = defaultdict(list)
visited = [0 for _ in range(vertex+1)]
heap = []
dist = [INF] * (vertex+1)
route = [INF] * (vertex+1)

for _ in range(int(input())):
  start, end, weight = map(int,input().split())
  graph[start].append((end, weight))

start, end = map(int, input().split())
dist[start] = 0
heapq.heappush(heap,(0, start))

while heap:
  curr = heapq.heappop(heap)[1]
  while heap and visited[curr]:
    curr = heapq.heappop(heap)[1]
  if visited[curr]:
    break
  visited[curr] = 1
  print(curr)

  for nxt, dis in graph[curr]:
    if dist[nxt] > dist[curr] + dis:
      dist[nxt] = dist[curr] + dis
      heapq.heappush(heap,(dist[nxt], nxt))
      route[nxt] = curr

res = deque([end])
cur = end
while cur != start:
  cur = route[cur]
  res.appendleft(cur)

print(dist[end])
print(len(res))
for i in range(len(res)):
  print(res.popleft(), end=" ")
