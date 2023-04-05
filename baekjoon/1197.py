# MST => 프림 알고리즘

from collections import defaultdict
import sys
import heapq
input = sys.stdin.readline

v, e = map(int,input().split())
graph = defaultdict(list)
visited = [0 for _ in range(v+1)]
for _ in range(e):
  s, e, d = map(int,input().split())
  graph[s].append((d,s,e))
  graph[e].append((d,e,s))

def prim():
  visited[1] = 1
  heap = graph[1]
  heapq.heapify(heap)
  mst = []
  weight = 0

  while heap:
    d,s,e = heapq.heappop(heap)
    if not visited[e]:
      visited[e] = 1
      mst.append((s,e))
      weight += d

      for dist,start,end in graph[e]:
        if not visited[end]:
          heapq.heappush(heap,(dist,start,end))
  print(weight)

prim()
