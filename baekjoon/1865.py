import sys
from collections import defaultdict
input = sys.stdin.readline
INF = sys.maxsize
tc = int(input())

def bellman_ford():
  global v
  dist = [INF for _ in range(v+1)]
  cycle = False
  dist[1] = 0
  for i in range(v):
    for j in range(1, v+1):
      for item in graph[j]:
        vertex, dis = item
        if dist[vertex] > dist[j] + dis:
          dist[vertex] = dist[j] + dis
          if i == v-1:
            cycle = True
  
  if cycle:
    print("YES")
  else:
    print("NO")
          
for _ in range(tc):
  v, e, w = map(int,input().split())
  graph = defaultdict(list)
  for _ in range(e):
    start, end, dis = map(int,input().split())
    graph[start].append((end, dis))
    graph[end].append((start, dis))

  for _ in range(w):
    start, end, dis = map(int,input().split())
    graph[start].append((end, -dis))
  
  bellman_ford()
